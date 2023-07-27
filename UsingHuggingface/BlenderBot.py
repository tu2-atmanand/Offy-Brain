
# TODO : Read Transformer Readme, theres lot of resources there for models and all. Also for this blenderbot see projects on github, till you find better model.

# Blenderbot - 730 mb

# Import the model class and the tokenizer
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import os
os.environ['TRANSFORMERS_CACHE'] = 'E:\Models\huggingface'

# Download and setup the model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained(
    "facebook/blenderbot-400M-distill", cache_dir="E:\Models\huggingface")
model = BlenderbotForConditionalGeneration.from_pretrained(
    "facebook/blenderbot-400M-distill")
while True:
    utterance = input("User : ")
    if utterance != "kill":
        inputs = tokenizer(utterance, return_tensors="pt")
        res = model.generate(**inputs)
        print(tokenizer.decode(res[0]))
    else:
        break
