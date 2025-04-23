from pathlib import Path

import modal


VOL_MOUNT_PATH = Path('/t5_vol_v2')

model_name = "google/flan-t5-base"

appname = "t5-model-fine_v2"

op_volume_name = "t5-v1-wei"
image = (modal.Image.debian_slim(python_version="3.10").pip_install(
    "accelerate",
    "transformers",
    "torch",
    "tensorboard",
    "datasets"
    ).add_local_dir(local_path='./src/dataset',remote_path='/root',copy= True)
    )
app = modal.App(name=appname,image=image)

output_vol = modal.Volume.from_name(op_volume_name,create_if_missing=True)

# json_file = modal.File.from_local('dataset/fineTune_data.json')
    
# json_test_file = modal.File.from_local('dataset/finetune_test.json')

@app.function(
    gpu='A100-40GB:2',
    timeout=7200,
    volumes={VOL_MOUNT_PATH: output_vol}
)




def finetune_t5( num_train_epochs: int = 1, test_size_percentage: int = 10):

    from transformers import (
        AutoModelForSeq2SeqLM,
        AutoTokenizer,
        DataCollatorForSeq2Seq,
        Seq2SeqTrainer,
        Seq2SeqTrainingArguments,
    )
    from datasets import load_dataset
    def load_fineTune_data(jsonfile ):
        data = load_dataset("json",data_files =jsonfile, split= 'train')
        return data
    
    data_set = load_fineTune_data('fineTune_data.json')
    test_dataset = load_fineTune_data('finetune_test.json')


    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


    padding_token_id = -100

    batch_size = 8

    def batch_proceessing(dataset):
            
      

        inputs = ["TEXT:"+ doc for doc in dataset['text'] ]

        model_inputs = tokenizer(
            inputs,
            max_length = 512,
            truncation = True,
            padding = "max_length"
        )

        outputs = []
        for output in dataset['output']:
            # Convert the dictionary to a single string
            output_str = f"'candidate': '{output['candidate']}', 'time': '{output['time']}', 'date': '{output['DATE']}', 'client':' {output['client']}', 'description': '{output['description']} at {output['time']}'"
            outputs.append(str("{"+output_str+"}"))

        labels = tokenizer(
            outputs,
            max_length = 256,
            padding = 'max_length'
        )

        labels['input_ids'] = [
            [ l if l != tokenizer.pad_token_id else padding_token_id for l in label] for label in labels['input_ids']
        ]

        model_inputs['labels'] = labels['input_ids']

        return model_inputs
    

    tokenized_train_dataset = data_set.map(
        batch_proceessing,
        batched = True,
        remove_columns = ['text','output']
    )

    tokenized_test_dataset = test_dataset.map(
        batch_proceessing,
        batched = True,
        remove_columns = ['text','output']
    )

    data_collector = DataCollatorForSeq2Seq(
        tokenizer,
        model = model,
        label_pad_token_id=padding_token_id,
        pad_to_multiple_of= batch_size
    )

    training_args = Seq2SeqTrainingArguments(
        per_device_train_batch_size = batch_size,
        per_device_eval_batch_size = batch_size,
        predict_with_generate=True,
        learning_rate=3e-5,
        num_train_epochs= 1,
        logging_strategy="steps",
        logging_steps=100,
        eval_strategy = "steps",
        save_strategy="steps",
        save_steps=100,
        save_total_limit=2,
        load_best_model_at_end=True

    )

    trainer = Seq2SeqTrainer(
        model = model,
        args = training_args,
        data_collator=data_collector,
        train_dataset=tokenized_train_dataset,
        eval_dataset = tokenized_test_dataset
    )

    try:
        print("starting the model finetueing")
        trainer.train()
    
    except KeyboardInterrupt:
        trainer.save_state()
        trainer.save_model()
        raise

    model.save_pretrained(str(VOL_MOUNT_PATH/"model"))
    tokenizer.save_pretrained(str(VOL_MOUNT_PATH/"model"))
    output_vol.commit()
    print("done finetuning the model")