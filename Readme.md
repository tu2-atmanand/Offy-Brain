# AI Bot
This project is an part of the main project [Offy](https://github.com/tu2-atmanand/offy). In this project i am going to build the final model, and use it there.
The main functionality of this AI model is to work kind of like a friendly chatbot, mimic a real human as much accurately as possible, but not neccessary need to have expertise in any field to provide information or anything. This model should give me output which are very similar to the human answers.
Also, i want to integrate the functionality of Assistant for doing basic tasks on pc, in this project.

So main goal of this project :
1. To build the final ML model for the main project.
2. Also create the logic (python code) for Assistant functionality.

For now this project will only be in Terminal Based, but for the internet functionality, ill need to create GUI interface.

## Overview
This project contains two sub projects, which uses different techologies to train model : 
1. **UsingTensorflow** : This uses simple Machine learning technology to train a model on a labeled data. This is the disadvatage, labeled data is not easily available so i have to use other techniques to train on unlabeled data. This model creates a chat_model as its final output which i can use in other projects with only one scripts and some pickle files. The main working code is in Main directory.

2. UsingChatterBot : This uses chatterbot module to train and build model. This creates a database file as its final output. This is under test. It do not create a good model as of now.


## Contribution
1. I need large and clean dataset to train the model. The data should be like the normal human speech, so the AI could give human like relatable reply. So please if anybody can provide large dataset to train the model, it will be helpful.

2. I searched everywhere if there is any prebuilt model, i didnt found any. So if you know any model which i can use directly in my main [[Offy]] project, please help.






## TODO
0. Use **GPT** Technology to build models.
1. If the AI didnt know the answer than it should reply in a way how humans reply.
2. If we are quit for long time than, the AI can ask something or start conversation.
3. Creating the Assistant functionality which includes basic tasks on PC.
4. Bringing data from internet and showing it in a intuitive and interesting format, using GUI in future.
