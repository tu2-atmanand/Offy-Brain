from UsingChatterbot.entities.ent_enabled_module import EnabledModule
from UsingChatterbot.entities.ent_chat_keyword import ChatKeyword
from UsingChatterbot.modules.get_welcome_msg.get_welcome_msg import get_welcome_msg

ENABLED_MODULE = EnabledModule(
    class_name=get_welcome_msg().getStrClassName(),
    custom_json_settings={}
)

""" TODO: Remove chat keywords and use chatterbot yaml (make own files
for each module and then train the bot for this file. :) """

CHAT_KEYWORDS = [
    ChatKeyword(chat_keyword="weather in")
]

# Dependencies of the module
DEPENDENCIES = []