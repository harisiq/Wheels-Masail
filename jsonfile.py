import csv
import json
import os

csv_file_path = '/home/haris/Desktop/Web Scraping/finetune/modified_file.csv'
cleaned_data = []

with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        for cell in row:
            try:
                cell = cell.replace('["', '').replace('"]', '').replace('\\"', '"')

                cell_json = json.loads(cell)

                cleaned_data.append(cell_json)
            except json.JSONDecodeError as e:
                print(f"JSON decode error for cell '{cell}': {e}")

jsonl_file_path = '/home/haris/Desktop/Web Scraping/finetune/techinaldataset.jsonl'
with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
    for item in cleaned_data:
        jsonl_file.write(json.dumps(item) + '\n')