from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sentiment", methods=["POST", "GET"])
def sentiment_analysis():
    model = load_model("model_py", compile=False)

    if request.method == "POST":
        input = request.form.get("nm")
        probability = model.predict(np.array([input]))[0][0]
        print(probability)
        if probability < 0:
            sentiment = "Negative"
        elif probability >= 0:
            sentiment = "Positive"
        return render_template(
            "index.html", nm=input, probability=probability, sentiment=sentiment
        )


if __name__ == "__main__":
    app.run(debug=True)
