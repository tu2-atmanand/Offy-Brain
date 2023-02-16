import os, sys
from global_constants import DB_NAME

from starterkit.fallback_module.get_smart_answer import get_smart_answer
from mgr.mgr_db import db_loadEnabledModules

ENABLED_MODULES = db_loadEnabledModules() # do only once for better performance
FALLBACK_MODULE = get_smart_answer() # shouldn't be changed, unless you know what you are doing


# Catch before other imports to avoid confusing error msgs
if not os.path.exists(DB_NAME):
    sys.exit("ERROR: No database detected. Please execute setup.py first!")

# from mgr.mgr_voices import live_speech
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
