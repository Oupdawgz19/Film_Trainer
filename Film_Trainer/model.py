
import requests,render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

TMDB_API_KEY = "89b58596928c97c7afa8f23569b4d33b"

def get_movies(query):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)
    results = response.json().get("results", [])
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("results", [])
    return results[:5]  # Limit to 5 base results

def get_similar_movies(base_movies):
    genres = []
    titles = []

    for movie in base_movies:
        title = movie['title']
        movie_id = movie['id']
        detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        response = requests.get(detail_url).json()
        genre_names = [g['name'] for g in response.get("genre", [])]
        genres.append(" ".join(genre_names))
        titles.append(title)

    # Vectorize genres and calculate similarity
    tfidf = TfidfVectorizer()
    genre_matrix = tfidf.fit_transform(genres)
    sim_matrix = cosine_similarity(genre_matrix)

    # Recommend based on first movie
    similar_scores = list(enumerate(sim_matrix[0]))
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)[1:]

    recommendations = [titles[i] for i, _ in similar_scores]
    return recommendations
