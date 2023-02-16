import tensorflow as tf
import numpy as np
import os
import re
import random

# Preprocessing the data
def preprocess_sentence(sentence):
    sentence = sentence.lower().strip()
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ."
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
    sentence = re.sub(r'[" "]+', " ", sentence)
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    sentence = re.sub(r"[^a-zA-Z?.!,]+", " ", sentence)
    sentence = sentence.strip()
    # adding a start and an end token to the sentence
    return sentence

# Creating the dataset
def create_dataset(path):
    lines = open(path, 'r', encoding='UTF-8').read().strip().split('\n')
    sentence_pairs = [line.split('\t') for line in lines]
    preprocessed_sentence_pairs = [
        (preprocess_sentence(pair[0]), preprocess_sentence(pair[1])) for pair in sentence_pairs
    ]
    return preprocessed_sentence_pairs

# Building the tokenizer and encoding the sentences
def tokenize(lang):
    lang_tokenizer = tf.keras.preprocessing.text.Tokenizer(
        filters='', oov_token='<OOV>'
    )
    lang_tokenizer.fit_on_texts(lang)
    tensor = lang_tokenizer.texts_to_sequences(lang)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')
    return tensor, lang_tokenizer

def load_dataset(path):
    # creating cleaned input, output pairs
    pairs = create_dataset(path)

    # index language using the class defined above
    inp_tensor, inp_lang_tokenizer = tokenize([pair[0] for pair in pairs])
    targ_tensor, targ_lang_tokenizer = tokenize([pair[1] for pair in pairs])

    return inp_tensor, inp_lang_tokenizer, targ_tensor, targ_lang_tokenizer

# Creating the model
class ChatBotModel(tf.keras.Model):
    def __init__(self, inp_vocab, targ_vocab, emb_dim, enc_units, batch_size):
        super(ChatBotModel, self).__init__()
        self.enc_units = enc_units
        self.batch_size = batch_size
        self.embedding = tf.keras.layers.Embedding(inp_vocab, emb_dim)
        self.gru = tf.keras.layers.GRU(self.enc_units,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')
        self.fc = tf.keras.layers.Dense(targ_vocab)

    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state=hidden)
        output = tf.reshape(output, (-1, output.shape[2]))
        x = self.fc(output)
        return x, state

    def initialize_hidden_state(self):
        return tf.zeros((self.batch_size, self.enc_units))

    def train_step(inp, targ, enc_hidden):
        loss = 0

        with tf.GradientTape() as tape:
            enc_output, enc_hidden = model(inp, enc_hidden)

            dec_hidden = enc_hidden

            dec_input = tf.expand_dims([targ_lang.word_index['<start>']] * batch_size, 1)

            # Teacher forcing - feeding the target as the next input
            for t in range(1, targ.shape[1]):
                # passing enc_output to the decoder
                predictions, dec_hidden = model(dec_input, dec_hidden)

                loss += loss_function(targ[:, t], predictions)

                # using teacher forcing
                dec_input = tf.expand_dims(targ[:, t], 1)

        batch_loss = (loss / int(targ.shape[1]))
        variables = model.trainable_variables
        gradients = tape.gradient(loss, variables)
        optimizer.apply_gradients(zip(gradients, variables))

        return batch_loss


import tensorflow as tf
import numpy as np

# Building the model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length))
model.add(tf.keras.layers.GRU(128, return_sequences=True))
model.add(tf.keras.layers.GRU(128))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training the model
history = model.fit(padded, one_hot_labels, epochs=100, batch_size=512)

# Saving the model
model.save('model.h5')
