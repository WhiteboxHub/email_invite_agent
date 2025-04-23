

# prompt_one = '''




# Extract the following fields from the input text and return a JSON:
# - candidate name
# - time in 24h format
# - date in YYYY-MM-DD


# example Text:
# Name of Candidate - andy (ML)
# Time of interview - 10:00 PM PST
# Mode of Interview-  MS Meeting 
# Client- google
# The candidate will attend the interviews from - Home
# Date - 4/22/2025
# Recruiter call

# example output :
#   "candidate": "andy",
#   "time": "22:00",
#   "DATE": "2025-04-22",
#   "client": "google",
#   "description": "Recruiter call scheduled for andy on 2025-04-22 by client, google"


# input TEXT: {text}

# '''


prompt_one = '''
Extract the following fields from the input text and return a JSON:
- candidate name
- time in 24h format
- date in YYYY-MM-DD
- client
- description

example 1:
Text:
Name of Candidate - Andy (ML)
Time of interview - 10:00 PM PST
Mode of Interview - MS Meeting
Client - Google
The candidate will attend the interviews from - Home
Date - 4/22/2025
Recruiter call

Output:
{
  "candidate": "Andy",
  "time": "22:00",
  "DATE": "2025-04-22",
  "client": "Google",
  "description": "Recruiter call scheduled for Andy on 2025-04-22 by client, Google"
}

example 2:
Text:
Name of Candidate - Priya
Time of interview - 11:30 AM PST
Mode of Interview - Zoom
Client - Meta
The candidate will attend the interviews from - Office
Date - 5/01/2025
technical call

Output:
{
  "candidate": "Priya",
  "time": "11:30",
  "DATE": "2025-05-01",
  "client": "Meta",
  "description": "technical call scheduled for Priya on 2025-05-01 by client, Meta"
}

Now, extract information from the following text and return the JSON.

Input TEXT:
{text}
'''

finetuned_model_prompt = '''TEXT: {text}'''



prompt_llama = '''
Extract the following fields from the input text and return a JSON:
- candidate name
- time in 24h format
- date in YYYY-MM-DD
- client
- description

example 1:
Text:
Name of Candidate - Andy (ML)
Time of interview - 10:00 PM PST
Mode of Interview - MS Meeting
Client - Google
The candidate will attend the interviews from - Home
Date - 4/22/2025
Recruiter call

Output:
{
  "candidate": "Andy",
  "time": "22:00",
  "DATE": "2025-04-22",
  "client": "Google",
  "description": "Recruiter call scheduled for Andy on 2025-04-22 by client, Google"
}

example 2:
Text:
Name of Candidate - Priya
Time of interview - 11:30 AM PST
Mode of Interview - Zoom
Client - Meta
The candidate will attend the interviews from - Office
Date - 5/01/2025
technical call

Output:
{
  "candidate": "Priya",
  "time": "11:30",
  "DATE": "2025-05-01",
  "client": "Meta",
  "description": "technical call scheduled for Priya on 2025-05-01 by client, Meta"
}

example 3:
Text:
Name of Candidate - John Doe
Time of interview - 2:45 PM PST
Mode of Interview - Google Meet
Client - Amazon
The candidate will attend the interviews from - Home
Date - 6/15/2025
HR Round

Output:
{
  "candidate": "John Doe",
  "time": "14:45",
  "DATE": "2025-06-15",
  "client": "Amazon",
  "description": "HR Round scheduled for John Doe on 2025-06-15 by client, Amazon"
}

example 4:
Text:
Name of Candidate - Sarah Smith
Time of interview - 8:15 AM PST
Mode of Interview - Phone Call
Client - Microsoft
The candidate will attend the interviews from - Office
Date - 7/20/2025
Final Round

Output:
{
  "candidate": "Sarah Smith",
  "time": "08:15",
  "DATE": "2025-07-20",
  "client": "Microsoft",
  "description": "Final Round scheduled for Sarah Smith on 2025-07-20 by client, Microsoft"
}

example 5:
Text:
Name of Candidate - David Brown
Time of interview - 5:00 PM PST
Mode of Interview - In-Person
Client - Apple
The candidate will attend the interviews from - Office
Date - 8/10/2025
Managerial Round

Output:
{
  "candidate": "David Brown",
  "time": "17:00",
  "DATE": "2025-08-10",
  "client": "Apple",
  "description": "Managerial Round scheduled for David Brown on 2025-08-10 by client, Apple"
}

Now, extract information from the following text and return the JSON.

Input TEXT:
{text}
'''
