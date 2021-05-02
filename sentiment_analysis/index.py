from flask import Flask, render_template, request
import pandas as pd
import requests
import json
import numpy as np
from flask_sqlalchemy import SQLAlchemy
import json
import model
from __init__ import app

f = open(
    "../movies.json",
)

data = json.load(f)

url = "http://localhost:8501/v1/models/my_model:predict"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/movie_page/<movie_id>")
def movie_page(movie_id):
    movie_data = {}
    for d in data["movies"]:
        if int(d["id"]) == int(movie_id):
            movie_data = d
    return render_template("movie_page.htm", movie_data=movie_data)


@app.route("/sentiment_analysis/<movie_id>", methods=["POST", "GET"])
def sentiment_analysis(movie_id):
    if request.method == "POST":
        input = request.form.get("review")
        print(input)
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
        if probability < 0:
            review_result1 = 0
        elif probability >= 0:
            review_result1 = 1
        new_review = {"reviewData": input, "result": review_result1}
        movie = model.Movie.query.filter_by(id=movie_id).first()
        print(movie)
        new_review = model.Comments(
            comment=input, review_status=review_result1, movie_id=movie_id
        )
        movie.average_score = movie.average_score + probability
        model.db.session.add(new_review)
        model.db.session.commit()
        movie_data = {}
        print(data)
        for d in data["movies"]:
            if int(d["id"]) == int(movie_id):
                movie_data = d
        reviews = model.Comments.query.filter_by(movie_id=movie_id).all()
        return render_template(
            "movie_page.htm",
            movie_data=movie_data,
            reviews=reviews,
        )


if __name__ == "__main__":
    app.run(debug=True)
