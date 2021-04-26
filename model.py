from flask import Flask, render_template, request
import pandas as pd
import requests
import json
import numpy as np

url = "http://localhost:8501/v1/models/my_model:predict"


app = Flask(__name__)

reviews = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sentiment_analysis", methods=["POST", "GET"])
def sentiment_analysis():
    if request.method == "POST":
        input = request.form.get("review")
        inputValue = [input]
        inputValues = pd.DataFrame(inputValue)
        print(inputValues)
        data = json.dumps(
            {
                "signature_name": "serving_default",
                "instances": inputValues.values.tolist(),
            }
        )
        print(data)
        headers = {"content-type": "application/json"}
        json_response = requests.post(url, data=data, headers=headers)
        output = json.loads(json_response.text)
        probability = np.squeeze(output["predictions"][0])
        print(probability)
        if probability < 0:
            review_result1 = 0
        elif probability >= 0:
            review_result1 = 1
        new_review = {"reviewData": input, "result": review_result1}
        reviews.append(new_review)
        return render_template(
            "index.html",
            reviews=reviews,
        )


if __name__ == "__main__":
    app.run(debug=True)
