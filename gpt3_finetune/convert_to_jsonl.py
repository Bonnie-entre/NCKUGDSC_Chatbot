import json

import os
current_dir = os.getcwd()

def json_to_jsonl(input_file, output_file):
    with open(input_file, 'r') as json_file:
        data = json.load(json_file)

    with open(output_file, 'w') as jsonl_file:
        for item in data:
            jsonl_line = json.dumps(item)
            jsonl_file.write(jsonl_line + '\n')

# 指定輸入的 JSON 文件路徑和輸出的 JSONL 文件路徑
input_json_file = os.path.join(current_dir, "faq_data.json")
output_jsonl_file = os.path.join(current_dir, "faq_data.jsonl")

# 呼叫函式進行轉換
json_to_jsonl(input_json_file, output_jsonl_file)
