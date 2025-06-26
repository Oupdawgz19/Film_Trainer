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
    
    def get_matching_movies_from_csv(matches, query ):

  
    matches = data[data['genre'].str.contains(query, case=False, na=False)]

    # Return the first 5 matches as a list
    return matches.head(5).to_dict(orient='records')

def home():
    return f"Loaded {len(data)} movies from CSV."

if __name__ == "__main__":
    app.run(debug=True)


