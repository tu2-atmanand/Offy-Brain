import json
import nltk
import re
import string

import numpy as np
import tensorflow as tf
import token as token
from keras_preprocessing.sequence import pad_sequences

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

# preprocess the input text
# preprocess the input text
def preprocess_text(text):
  # join the tokens into a single string
  text = ' '.join(text)
  # remove punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))
  # convert to lowercase
  text = text.lower()
  # tokenize
  tokens = nltk.word_tokenize(text)
  # remove stop words
  stop_words = nltk.corpus.stopwords.words('english')
  tokens = [token for token in tokens if token not in stop_words]
  # lemmatize
  lemmatizer = nltk.stem.WordNetLemmatizer()
  tokens = [lemmatizer.lemmatize(token) for token in tokens]
  return tokens


# define a model using a deep learning neural network
def create_model():
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(output_size, activation='softmax')
  ])
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model


def generate_response(model, text):
  # get the input text from the user
  input_text = input('Enter your message: ')
  # preprocess the input text
  tokens = preprocess_text(input_text)
  # convert the tokens to a sequence of word indices
  sequence = [word_index[token] for token in tokens if len(token) > 1]
  # pad the sequence to the maximum length
  inputs = tf.keras.preprocessing.sequence.pad_sequences([sequence], maxlen=max_length, padding='post')
  # pad the sequence to the maximum length
  sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
  # generate a response by predicting the class probabilities
  probabilities = model.predict(sequence)[0]
  # select the class with the highest probability
  class_index = np.argmax(probabilities)
  # retrieve the corresponding response
  response = responses[class_index]
  return response





# generate a response to the input text
# def generate_response(model, text):
#   # preprocess the input text
#   tokens = preprocess_text(text)
#   # convert the tokens to a sequence of word indices
#   sequence = [word_index[token] for token in tokens if len(token) > 1]
#   # pad the sequence to the maximum length
#   sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
#   # generate a response by predicting the class probabilities
#   probabilities = model.predict(sequence)[0]
#   # select the class with the highest probability
#   class_index = np.argmax(probabilities)
#   # retrieve the corresponding response
#   response = responses[class_index]
#   return response

# load the training data from the dialogs.txt file
inputs, outputs = [], []
with open('dialogs.txt', 'r') as infile:
  for line in infile:
    input_text, output_text = line.strip().split('\t')
    input_tokens = preprocess_text(input_text)
    output_tokens = preprocess_text(output_text)
    inputs.append(input_tokens)
    outputs.append(output_tokens)

# create a vocabulary of unique tokens
all_tokens = [token for tokens in inputs + outputs for token in tokens]
vocab_size = len(set(all_tokens))


# read the dataset from a file
with open('dialogs.txt', 'r') as f:
  lines = f.readlines()

# create a list of intents
intents = []
for line in lines:
  # split the line into input and output
  input_text, output_text = line.strip().split('\t')
  # create an intent with a unique tag
  intent = {
    "tag": f"intent_{len(intents)}",
    "patterns": [input_text],
    "responses": [output_text]
  }
  intents.append(intent)

# create the intents data structure
intents = {
  "intents": intents
}

# create a vocabulary of unique words from the training data
vocab = set()
for intent in intents['intents']:
  for pattern in intent['patterns']:
    vocab.update(preprocess_text(pattern))

# create a word index mapping
word_index = {token: index for index, token in enumerate(vocab)}




# create a word index mapping
# word_index = {token: index for index, token in enumerate(set(all_tokens))}

# create a reverse word index mapping
reverse_word_index = {index: token for token, index in word_index.items()}

# create a list of responses
responses = [output for output in outputs]

# determine the maximum length of the input sequences
max_length = max([len(inputs) for inputs in inputs])

# create a list of input sequences padded to the maximum length
inputs = tf.keras.preprocessing.sequence.pad_sequences(inputs, maxlen=max_length, padding='post')

# create a one-hot encoded list of output sequences
outputs = tf.keras.utils.to_categorical(outputs)

# determine the number of unique output classes
output_size = len(set(outputs))

import json

# Save the responses to a file
with open("responses.json", "w") as f:
    json.dump(responses, f)

# Save the word index to a file
with open("word_index.json", "w") as f:
    json.dump(word_index, f)


# create the model
model = create_model()

# fit the model to the training data
model.fit(inputs, outputs, epochs=10)

# save the model
model.save('chatbot_model.h5')

