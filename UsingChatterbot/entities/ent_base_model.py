from peewee import *
from UsingChatterbot.starterkit.fallback_module.conf import db

# Create base model to keep code leaner
class BaseModel(Model):
    class Meta:
        # Determine which db to use
        database = db
