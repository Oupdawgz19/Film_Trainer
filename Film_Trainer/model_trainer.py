from flask import Flask, render_template, request, jsonify
from model import get_movies, get_similar_movies
import pandas as pd

data=pd.read_csv('action.csv')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def recommend():
    results = []
    if request.method == "POST":
        query = request.form["query"].strip().lower()
        matches = data[data["title"].str.lower().str.contains(query, na=False)]
        results = matches.head(5).to_dict(orient="records")
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def get_matching_movies_from_csv(action.csv, user_input):

    df = pd.read_csv("action.csv")

    # Assuming you have a 'title' column and want to find case-insensitive matches
    # Filter rows where the title contains the user input
    matches = df[df['genre'].str.contains(user_input, case=False, na=False)]

    # Return the first 5 matches as a list of dictionaries (or as desired)
    return matches.head(5).to_dict(orient='records')
def home():
    return f"Loaded {len(data)} movies from CSV."

if __name__ == "__main__":
    app.run(debug=True)
