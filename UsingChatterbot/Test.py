import os, sys
from UsingChatterbot.starterkit.fallback_module.global_constants import DB_NAME
from starterkit.fallback_module.get_smart_answer import get_smart_answer
from UsingChatterbot.entities.ent_enabled_module import EnabledModule

def db_loadEnabledModules():
    enabled_modules = []
    for module in EnabledModule.select():
        enabled_modules.append(
            # str to class
            getattr(sys.modules[__name__], module.class_name)() # make instance out of class
        )
    return enabled_modules


ENABLED_MODULES = db_loadEnabledModules() # do only once for better performance
FALLBACK_MODULE = get_smart_answer() # shouldn't be changed, unless you know what you are doing

# Catch before other imports to avoid confusing error msgs
if not os.path.exists(DB_NAME):
    sys.exit("ERROR: No database detected. Please execute setup.py first!")

# from Archived-SpeechRecognitio.mgr_voices import live_speech
# from peewee import *

def getAssistantResponse(phrase):
    # print(str(phrase))
    have_answered = False
    answer = "Unknown error"
    for module in ENABLED_MODULES:
        # text should be always a str, bc. we validated this in Train.py
        if any(x in str(phrase) for x in module.getChatKeywords()):
            answer = str(module.getAnswer(phrase))
            have_answered = True

    # Outside of for, so if nothing is returned we get a smart answer, but only if nothing answered until now
    if not have_answered: answer = str(FALLBACK_MODULE.getAnswer(phrase))

    print("Assistant : \""+answer+"\"")
    # assistantVoice.say(answer)
    # assistantVoice.runAndWait()


def main():
    # Start Voice Recognition
    # live_speech()
    while(1):
        text = input("You : ")
        if text == "kill":
            break
        getAssistantResponse(text)


if __name__ == '__main__':
    main()



# Code using the ChatterBotCorpusTrainer module
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

while 1:
  inp = input("User : ")
  if inp=="kill":
    break
  response = chatbot.get_response('I would like to book a flight.')
  print(response)

'''


# Code using the ListTrainer module
'''

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')
trainer = ListTrainer(chatbot)
trainer.train([
'Hi, can I help you?',
'Sure, I would like to book a flight to Iceland.',
'Your flight has been booked.'
])


'''

# simple code to run
'''
import spacy
nlp = spacy.load('en_core_web_sm')
def chatbot(statement):
  # weather = nlp("Current weather in a city")
  statement = nlp(statement)
  print(statement)


while 1:
  inp = input("User : ")
  if inp=="kill":
    break
  weather = nlp(inp)
  print(weather)

'''

