
import json, pickle, numpy as np, random
from tensorflow import keras

model = keras.models.load_model("../model/chat_model")
tokenizer = pickle.load(open("../model/tokenizer.pickle", "rb"))
encoder = pickle.load(open("../model/label_encoder.pickle", "rb"))

with open("../data/intents.json") as f:
    intents = json.load(f)

while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        break

    seq = tokenizer.texts_to_sequences([msg])
    padded = keras.preprocessing.sequence.pad_sequences(seq, maxlen=20)
    tag = encoder.inverse_transform([np.argmax(model.predict(padded))])[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            print("Bot:", random.choice(intent["responses"]))
