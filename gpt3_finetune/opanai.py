import openai

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
FINE_TUNE_JOB_ID = os.getenv('OPENAI_FINTUNE_JODID_1')
openai.api_key = OPENAI_APIKEY

response = openai.FineTune.list_fine_tunes()

model_name = None

for fine_tune in response['data']:
    if fine_tune['fine_tune_id'] == FINE_TUNE_JOB_ID:
        model_name = fine_tune['model_name']
        break

print(model_name)