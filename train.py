
import json, pickle, numpy as np
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open("../data/intents.json") as f:
    data = json.load(f)

sentences, labels = [], []
for intent in data["intents"]:
    for p in intent["patterns"]:
        sentences.append(p)
        labels.append(intent["tag"])

encoder = LabelEncoder()
y = encoder.fit_transform(labels)

tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
X = pad_sequences(tokenizer.texts_to_sequences(sentences), maxlen=20)

model = Sequential([
    Embedding(1000, 16, input_length=20),
    GlobalAveragePooling1D(),
    Dense(16, activation="relu"),
    Dense(len(set(labels)), activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, np.array(y), epochs=300)

model.save("../model/chat_model")
pickle.dump(tokenizer, open("../model/tokenizer.pickle", "wb"))
pickle.dump(encoder, open("../model/label_encoder.pickle", "wb"))

print("Model trained and saved.")
