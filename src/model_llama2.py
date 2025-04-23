from transformers import AutoTokenizer, LlamaForCausalLM,AutoModelForCausalLM
from utils.prompts import prompt_llama
import transformers
import torch
def model_llama2(input_text):

    # tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
    # model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")

    model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
    prompt = prompt_llama.format(text= input_text)
        
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate
    generate_ids = model.generate(inputs.input_ids, max_length=30)
    print(tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
    # model_id = "meta-llama/Meta-Llama-3-8B"

    # pipeline = transformers.pipeline("text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
    # print(pipeline(prompt))
    


t1 = '''Name of Candidate - Narasimulu  (ML)
Time of interview - 7:30 AM PST
Mode of Interview-  MS Meeting 
Client- LYNA Cam
The candidate will attend the interviews from- Home
Date - 4/22/2025

Recruiter Call'''

model_llama2(t1)