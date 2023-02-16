import json
import nltk
import re
import string
import numpy as np
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences


# Preprocess the input text
def preprocess_text(text):
  # Join the tokens into a single string
  text = ' '.join(text)
  # Remove punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))
  # Convert to lowercase
  text = text.lower()
  # Tokenize
  tokens = nltk.word_tokenize(text)
  # Remove stop words
  stop_words = nltk.corpus.stopwords.words('english')
  tokens = [token for token in tokens if token not in stop_words]
  # Lemmatize
  lemmatizer = nltk.stem.WordNetLemmatizer()
  tokens = [lemmatizer.lemmatize(token) for token in tokens]
  return tokens

# Load the model from a file
model = tf.keras.models.load_model('chatbot_model.h5')

# Load the word index
with open('word_index.json') as f:
    word_index = json.load(f)

# Load the responses
with open('responses.json') as f:
    responses = json.load(f)

# Get the maximum length of the sequences
max_length = model.input_shape[1]

# Get the input text from the user
input_text = input('Enter your message: ')
# Preprocess the input text
tokens = preprocess_text(input_text)
# Convert the tokens to a sequence of word indices
sequence = [word_index[token] for token in tokens if len(token) > 1]
# Pad the sequence to the maximum length
sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
# Generate a response by predicting the class probabilities
probabilities = model.predict(sequence)[0]
# Select the class with the highest probability
class_index = np.argmax(probabilities)
# Retrieve the corresponding response
response = responses[class_index]
# Display the response
print(response)

























# import tensorflow as tf
# import re
#
# def preprocess_text(text):
#   # lowercase the text
#   text = text.lower()
#   # remove punctuation
#   text = re.sub(r'[^\w\s]', '', text)
#   # tokenize the text into words
#   tokens = text.split()
#   return tokens
#
# vocab = set()
# for intent in intents['intents']:
#   for pattern in intent['patterns']:
#     vocab.update(preprocess_text(pattern))
# # create a word index mapping
# word_index = {token: index for index, token in enumerate(vocab)}
#
#
# # define a function to generate a response to the input text
# def generate_response(model, text):
#   # preprocess the input text
#   tokens = preprocess_text(text)
#   # convert the tokens to a sequence of word indices
#   sequence = [word_index[token] for token in tokens]
#   # pad the sequence to the maximum length
#   sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
#   # generate a response by predicting the class probabilities
#   probabilities = model.predict(sequence)[0]
#   # select the class with the highest probability
#   class_index = np.argmax(probabilities)
#   # retrieve the corresponding response
#   response = responses[class_index]
#   return response
#
# # load the model from the chatbot_model.h5 file
# model = tf.keras.models.load_model('chatbot_model.h5')
#
# # get the input text from the user
# input_text = input('Enter your message: ')
#
# # generate a response to the input text
# response = generate_response(model, input_text)
#
# print(response)









import nltk
import json
from nltk import word_tokenize, pos_tag
import nltk
nltk.download('averaged_perceptron_tagger')



# Load the intents from the intents.json file
with open('intents.json') as f:
    intents = json.load(f)

# Define a function that takes a list of words as input and returns a list of named entities
def extract_entities(text):
    entities = []
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        if tag == 'NNP':
            entities.append(word)
    return entities

# Loop through the intents and extract named entities from the patterns
for intent in intents['intents']:
    if isinstance(intent.get('patterns', ''), str):
        intent['patterns'] = [intent['patterns']]
    for pattern in intent['patterns']:
        entities = extract_entities(pattern)
        if entities:
            intent['tag'] = ' '.join(entities)
    else:
        intent['tag'] = 'Other'


# Save the modified intents to a new file
with open('intents_with_tags.json', 'w') as f:
    json.dump(intents, f)
