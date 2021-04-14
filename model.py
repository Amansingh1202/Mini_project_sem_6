from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model
import numpy as np
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sentiment",methods = ['POST', 'GET'])
def sentiment_analysis():

    model = load_model('model_py/model.h5',compile = False)

    if request.method == 'POST':
        input = request.form.get("nm")
        sentiment = ''
        max_review_length = 100
        word_to_ind = imdb.get_word_index()
        strip_special_characters = re.compile("[^A-Za-z0-9]+")
        input  = input.lower().replace("<br>","")
        input = re.sub(strip_special_characters,"",input.lower())

        words = input.split()
        x_test = [[word_to_ind[word] if (word in word_to_ind and word_to_ind[word]<=20000) else 0 for word in words]]
        x_test = pad_sequences(x_test,maxlen = max_review_length)
        vector = np.array([x_test.flatten()])

        probability = model.predict(np.array([vector][0]))[0][0]
        class1 = model.predict_classes(np.array([vector][0]))[0][0]

        if (class1 == 0):
            sentiment = 'Negative'
        elif (class1 == 1):
            sentiment = 'Positive'
        else:
            sentiment = 'None'
        return render_template("index.html",nm = input,probability = probability, sentiment = sentiment)

if __name__ == "__main__":
    app.run(debug = True)
