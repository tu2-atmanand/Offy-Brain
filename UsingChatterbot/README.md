# Chatbot Using Chatterbot  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Easy to use *modular* chatbot to talk to, get information from etc. (depends on enabled modules) and the best of all **keeping your data private/locally**. Therefore, the assistant can operate offline except by the use of some modules (e.g. weather module, etc.). Would love to see some reactions (issues, pull-requests, etc.). Please note, that this project is young and has not all featured functionalities.
This application uses the Chatterbot framework.  

## How to get started
0. Use **python 3.8**
1. Run : ```Pip install -r requirements.txt```
2. Also download the some packages :
    ```python -m spacy download en_core_web_sm```
    ```python -m spacy download en```
3. Open file : venv/Lib/site-packages/chatterbot/languages.py, and on line 583 somewhere, change this code : 

```
class ENG:
ISO_639_1 = 'en'
ISO_639 = 'eng'
ENGLISH_NAME = 'English'
```
to this : 
```
class ENG:
ISO_639_1 = 'en_core_web_sm'
ISO_639 = 'eng'
ENGLISH_NAME = 'English'
```
4. Now run the setup.py file
5. And now run main.py and enjoy!

