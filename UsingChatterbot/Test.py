# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# chatbot = ChatBot('Ron Obvious')
#
# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)
#
# # Train the chatbot based on the english corpus
# trainer.train("chatterbot.corpus.english")
#
# # Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")


#
# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# # Create a new chat bot named Charlie
# chatbot = ChatBot('Charlie')
# trainer = ListTrainer(chatbot)
# trainer.train([
# 'Hi, can I help you?',
# 'Sure, I would like to book a flight to Iceland.',
# 'Your flight has been booked.'
# ])
#
# response = chatbot.get_response('I would like to book a flight.')


# TODO : I have two options now:
# 1. Chatterbot which im using
# 2. Spacy which im learning here.


import spacy
nlp = spacy.load('en_core_web_sm')
def chatbot(statement):
  weather = nlp("Current weather in a city")
  statement = nlp(statement)
  print(weather)


weather = nlp("Current weather in a city")
print(weather)