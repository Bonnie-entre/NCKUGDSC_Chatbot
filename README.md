# GDSC Chatbot

This is the project for NCKU chatbot.
<br>


## Table of Contents
- [Development](#development)
- [Resource](#resource)
<br>
<br>


## Development
1. prepare data
2. API key
3. Command, create the finetune model

[OPENAI Finetune Document](https://platform.openai.com/docs/guides/fine-tuning)

```
#
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>

#can use other parameter to customize your model_name
openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>

# check process
openai api fine_tunes.follow -i ft-F6SoPx0VkI3QNIkmqNNODk81
```

**result**
```
my file ID: file-mt5FrvoTz3IaNIFufRyX2esg

[2023-05-24 12:09:36] Created fine-tune: ft-F6XXXXXXXXXXXXXXXXXXX
[2023-05-24 12:11:12] Fine-tune costs $0.07
[2023-05-24 12:23:27] Uploaded model: curie:ft-personal-2023-05-24-04-23-27
[2023-05-24 12:23:28] Uploaded result file: file-N871oXXXXXXXXXXXXXX
[2023-05-24 12:23:28] Fine-tune succeeded
```

4. run `gui.py`, after modify the model_name
<br>
<br>

## Resource
* [How to Fine Tune GPT3 | Beginner's Guide to Building Businesses w/ GPT-3](https://www.youtube.com/watch?v=3EdEw4gyr-s)
<br>