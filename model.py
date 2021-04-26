from flask import Flask, render_template, request
import pandas as pd
import requests
import json

url = "http://localhost:8501/v1/models/my_model:predict"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sentiment", methods=["POST", "GET"])
def sentiment_analysis():
    # model = load_model("model_py", compile=False)

    if request.method == "POST":
        input = request.form.get("nm")
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
        probability = json.loads(json_response.text)
        print(probability)
        # probability = model.predict(np.array([input]))[0][0]
        # print(probability)
        # if probability < 0:
        #     sentiment = "Negative"
        # elif probability >= 0:
        #     sentiment = "Positive"
        return render_template(
            "index.html", nm=input, probability=probability, sentiment=probability
        )


if __name__ == "__main__":
    app.run(debug=True)
