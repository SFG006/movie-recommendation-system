import pickle
import random
import requests
import urllib.parse
from sklearn.metrics.pairwise import cosine_similarity
from flask import url_for

API_KEY = '1785d39c9dc62729cb9c119ae7957953'

moviess = pickle.load(open('models/movies.pkl', 'rb'))
vectors = pickle.load(open('models/vectors.pkl', 'rb'))

def fetch_poster(title):
    try:
        encoded_title = urllib.parse.quote(title)
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={encoded_title}"
        search_response = requests.get(search_url, timeout=5)
        search_data = search_response.json()

        if search_data.get('results'):
            movie_id = search_data['results'][0]['id']
            poster_path = search_data['results'][0].get('poster_path')

            details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
            details_response = requests.get(details_url, timeout=5)
            details_data = details_response.json()
            imdb_id = details_data.get('imdb_id')

            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else url_for('static', filename='default.jpg')
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

            return poster_url, imdb_url
        else:
            return url_for('static', filename='default.jpg'), None

    except Exception as e:
        print("Error fetching poster or IMDb link:", e)
        return url_for('static', filename='default.jpg'), None


def recommend(movie_title):
    idx = moviess[moviess['title'].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        print("Movie not found.")
        return []

    idx = idx[0]
    distances = cosine_similarity(vectors[idx], vectors)
    movie_list = sorted(list(enumerate(distances[0])), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in movie_list:
        title = moviess.iloc[i[0]].title
        poster, imdb = fetch_poster(title)
        recommendations.append({
            'title': title,
            'poster': poster,
            'imdb': imdb
        })

    return recommendations


def search_by_genre(genre):
    return moviess[moviess['genre'].str.contains(genre, case=False)]['title'].tolist()
