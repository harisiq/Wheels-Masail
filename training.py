import openai
import csv
import json
import os
import numpy as np
from collections import defaultdict
import tiktoken
import gradio as gr

openai.api_key = "api-key"


training_file_name = '/home/haris/Desktop/Web Scraping/finetune/techinaldatasetfinal.jsonl'

training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine-tune"
)
training_file_id = training_response["id"]

print("Training file id:", training_file_id)

suffix_name = "wheelsmasail"

response = openai.FineTuningJob.create(
    training_file=training_file_id,
    model="gpt-3.5-turbo",
    suffix=suffix_name,
)

job_id = response["id"]

print(response)



