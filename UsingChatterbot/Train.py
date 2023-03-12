from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize the chatbot
chatbot = ChatBot("first")

# Create a list trainer for the chatbot
list_trainer = ListTrainer(chatbot)

# Load the training data from the 'dialogs.txt' file
with open('output.txt', 'r') as file:
    training_data = file.readlines()

# Train the chatbot using the training data
for statement in training_data:
    list_trainer.train(statement)


# Below is the code using ChatterBotCorpusTrainer module : 

# # from chatbot import chatbot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot import ChatBot
# from chatterbot_corpus import data
#
# chatbot = ChatBot('first')
#
# trainer = ChatterBotCorpusTrainer(chatbot)
#
# trainer.train(
#     "chatterbot.corpus.english"
# )


# Incase if you want to save the trained model as *.h5 file (YOu dont need this as database is also nice but stiil train and see what are the results) :

"""

Here is an updated version of the code to train and save the chatbot using the ListTrainer class and save the model as a .h5 file:


import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tensorflow as tf

# Initialize the chatbot
chatbot = ChatBot("My Chatbot")

# Create a list trainer for the chatbot
list_trainer = ListTrainer(chatbot)

# Load the training data from the 'dialogs.txt' file
with open('dialogs.txt', 'r') as file:
    training_data = file.readlines()

# Train the chatbot using the training data
for statement in training_data:
    list_trainer.train(statement)

# Save the trained model as a .h5 file
model_directory = 'model/'
if not os.path.exists(model_directory):
    os.makedirs(model_directory)
model_file = 'model/model.h5'
chatbot.trainer.storage.sync(model_file)

# Test the chatbot with some input
response = chatbot.get_response("I would like to book a flight to Madrid")
print("Chatbot: ", response)

In this updated code, the trained chatbot model is saved as a .h5 file using the sync method of the storage adapter. The path to the model file is specified using the model_directory and model_file variables. Before saving the model, the code checks if the model directory exists and creates it if it does not exist. 

"""

# Now to use the above saved model : 

"""

To use the saved .h5 model to talk with the chatbot, you need to create a new ChatBot instance and load the saved model into it. Here is an example of how you can do this:

python
Copy code
import os
from chatterbot import ChatBot
import tensorflow as tf

# Load the trained model from the .h5 file
model_file = 'model/model.h5'
model = tf.keras.models.load_model(model_file)

# Initialize the chatbot using the trained model
chatbot = ChatBot(
    "My Chatbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer',
    training_data=[]
)

chatbot.set_trainer(ListTrainer)
chatbot.trainer.storage.tensorflow_backend.model = model

# Test the chatbot with some input
response = chatbot.get_response("I would like to book a flight to Madrid")
print("Chatbot: ", response)
In this code, the saved .h5 model is loaded using the load_model method from the tf.keras.models module. The loaded model is then used to initialize a new ChatBot instance. The set_trainer method is used to set the trainer for the chatbot, and the storage.tensorflow_backend.model property is set to the loaded model. The chatbot can now be used to respond to user inputs as usual.

"""