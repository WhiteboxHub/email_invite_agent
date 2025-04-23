from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.prompts import finetuned_model_prompt,prompt_one 


def model_calling(input_text):

    finetune_model_weights = './m2/model'

    tokenizer = AutoTokenizer.from_pretrained(finetune_model_weights)
    model = AutoModelForSeq2SeqLM.from_pretrained(finetune_model_weights)



    # prompt = finetuned_model_prompt.format(text=input_text)
    prompt = prompt_one + input_text

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))



t1 = '''Name of Candidate - Narasimulu  (ML)\nTime of interview - 7:30 PM PST\nMode of Interview-  MS Meeting \nClient- LYNA Cam\nThe candidate will attend the interviews from - Home\nDate - 4/22/2025\nRecruiter Call'''
t2 = "Name of Candidate - Riya\nTime of interview - 4:30 PM PST\nMode of Interview - Zoom\nClient - Infosys\nThe candidate will attend the interviews from - Office\nDate - 26/09/2025\ntechnical call"

t3 = "Name of Candidate - Ved\nTime of interview - 9:30 AM PST\nMode of Interview - Skype\nClient - Accenture\nThe candidate will attend the interviews from - Home\nDate - 25/09/2025\ntechnical call"


t4 =  "Name of Candidate - Nikhil\nTime of interview - 12:00 PM EST\nMode of Interview - Google Meet\nClient - Dell\nThe candidate will attend the interviews from - Home\nDate - 23/09/2025\ntechnical call"

model_calling(t1)
model_calling(t2)
model_calling(t3)
model_calling(t4)