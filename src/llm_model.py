# Use a pipeline as a high-level helper
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from utils.prompts import prompt_one

def model_calling(input_text):



    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")

    prompt = prompt_one+ input_text

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=200)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))


# model_calling('''
# Name of Candidate - Maryam (ML)
# Time of interview - 10:00 AM PST
# Mode of Interview-  MS Meeting 
# Client- Fractal
# The candidate will attend the interviews from- Home
# Date - 4/22/2025

# Recruiter Call
# ''')

t1 = '''Name of Candidate - Narasimulu  (ML)
Time of interview - 7:30 AM PST
Mode of Interview-  MS Meeting 
Client- LYNA Cam
The candidate will attend the interviews from- Home
Date - 4/22/2025

Recruiter Call'''

model_calling(t1)