from pickletools import optimize
import random
import json
import pickle
from tabnanny import verbose
from tokenize import Ignore
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import sequential
from tensorflow.keras.layeers import dense, activation, dropout
from tensorflow.keras.optimizers import SGD 

lemmatizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
Ignore_letters = ['?','!', '.', ',']

for intent in intents['intentts']:
    for patern in intent['patterns']:
        word_list = nltk.tokenize(patterns)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in Ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))
pickle.dump(words, open('words.pk1', 'wb'))
pickle.dump(classes, open('classes.pk1', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower())for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
        
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random. shuffle(training)
training = np.array(training)
    
train_x = list(training[:, 0])
train_y = list(training[:, 0])

model = sequential()
model.add(dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(dropout(0.5))
model.add(dense(64, activation='relu'))
model.add(dropout(0.5))
model.add(dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentrophy', optimize=sgd,metrics=['accuracy'])

model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot model.model')
print("done")