# Offy-Brain
This project is an part of the main project [Offy](https://github.com/tu2-atmanand/offy). In this project i am going to build the final model or the main Brain for the AI i am building in offy project.
The main functionality of this AI model is to work kind of like a friendly chatbot, mimic a real human as much accurately as possible, and not neccessary need to have expertise in any field to provide information or anything. This model should give me output which are very similar to the human answers.
Also, i want to integrate the functionality of Assistant for doing basic tasks on pc, in this project. Another main objective of this project is to keep track of all the approaches and technologies i have used till now to get the desired result. This will also help to see the history and learn from it.

So main goal of this project :
1. To build the final ML model for the main project.
2. Also create the logic (python code) for Assistant functionality.

For now this project will only be in Terminal Based, but for the internet functionality, ill need to create GUI interface.

## Overview
This repository contains subprojects or approaches i have tried till now to reach to the final model. The earlier methods are kept because they might have some scope in future. So the first two approaches were to train our own ML model, but this wont be beneficial, hence going for the third approach of using prebuilt model from hugging face.
Following are the approaches :

1. **Using Chatterbot** : This project uses Chatterbot and spacy packages of python to collect and train our own model. But this is a Rule Based model and wont be suitable for conversational purposes, hence needs to be archived soon.

2. **Using Tensorflow** : This is another approach to train our own model, but after building a model i realized that, to build a good model there is requirement of ML knowledge and good computing resources, and i have none. So i moved for prebuilt model, which can run efficiently on even computers which dont have GPUs. So moving on to the next and current approach.

3. **Using Huggingface** : In this project i have learnt lot of programming as well as ML concepts, so will be a good opportunity to continue with this. After experimenting with multiple models, suprisingly i have found few models which can run efficiently on even low end computer, but will need some fine tuning. After working with multiple LLM, there is another approach can be followed, i can use this small model for conversational purpose, and then i can ask the Assistant to serach the current query in a large model, which is very close to ChatGPT. So in this same project this approach will be followed. See Readme for further details.


## Contribution

### For Using Chatterbot Method
	1. I need large and clean dataset to train the model. The data should be like the normal human speech, so the AI could give human like relatable reply. So please if anybody can provide large dataset to train the model, it will be helpful.

	2. I searched everywhere if there is any prebuilt model, i didnt found any. So if you know any model which i can use directly in my main [[Offy]] project, please help.






## TODO
1. If the AI didnt know the answer than it should reply in a way how humans reply.
2. If we are quit for long time than, the AI can ask something or start conversation.
3. Creating the Assistant functionality which includes basic tasks on PC.
4. Bringing data from internet and showing it in a intuitive and interesting format, using GUI.
