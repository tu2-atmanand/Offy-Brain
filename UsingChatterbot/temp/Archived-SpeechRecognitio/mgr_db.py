import sys
from peewee import *

# TODO: Import all modules dynamically
from UsingChatterbot.modules.get_welcome_msg.get_welcome_msg import get_welcome_msg
from UsingChatterbot.modules.get_random_question.get_random_question import get_random_question
from UsingChatterbot.modules.get_random_fact.get_random_fact import get_random_fact
from UsingChatterbot.entities.ent_enabled_module import EnabledModule

def db_loadEnabledModules():
    enabled_modules = []
    for module in EnabledModule.select():
        enabled_modules.append(
            # str to class
            getattr(sys.modules[__name__], module.class_name)() # make instance out of class
        )
    return enabled_modules



