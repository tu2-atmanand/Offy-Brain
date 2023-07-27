
# Using Huggingface

At present we are using Blenderbot model by facebook.

Blender Bot is a cutting-edge chatbot that leverages the Transformer architecture to engage in dynamic and contextually rich conversations. It is trained on a vast corpus of diverse data from the internet, enabling it to generate human-like responses and exhibit an understanding of context and nuanced language.

## Our Goal

The primary goal of this project is to fine-tune Blender Bot to meet specific requirements and optimize its performance for our unique use case. We aim to tailor the model to remember past conversations, enhance its efficiency to run seamlessly on low-end PCs, and refine its responses to ensure high-quality interactions.

In this repository, you'll find all the necessary code, scripts, and configuration files to fine-tune Blender Bot and embark on an exciting journey of building a highly efficient and context-aware conversational AI.

## Conclusion
>
> It woked, so only thing its a pretrained model, you can directly use it in your project but it takes 4 sec or more to reply but uses only 50% of CPU, so if you can do anything with this than it might help, and its not giving like an AI answers, it will give you answer for almost everything like a human would have given but since it does not have a memory, it cannot rememeber my past conversation and react accordingly.



## How to use :
1. Install Transformer : pip install Transformer
2. Install pytorch : pip3 install torch torchvision torchaudio
3. Crate a file and run it : 
```python
# Import the model class and the tokenizer
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
# Download and setup the model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained(
    "facebook/blenderbot-400M-distill")
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

```
4. Enjoy!

### Contribution

We encourage active collaboration and contributions from the community to improve the performance and capabilities of our conversational AI. If you have any ideas, enhancements, or bug fixes, please feel free to submit a pull request or open an issue.

Let's dive into the world of conversational AI and create an extraordinary user experience with Blender Bot!
