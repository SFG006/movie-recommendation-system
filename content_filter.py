import pickle
import random
import requests
import urllib.parse
from sklearn.metrics.pairwise import cosine_similarity
from flask import url_for

API_KEY = '1785d39c9dc62729cb9c119ae7957953'

# Load the movie data and precomputed vectors from pickle files
moviess = pickle.load(open('models/movies.pkl', 'rb'))
vectors = pickle.load(open('models/vectors.pkl', 'rb'))

def fetch_poster(title):
    """
    Fetches the movie poster URL and IMDb URL for a given movie title using TMDB API.
    If no poster is found, returns a default poster image.
    """
    try:
        # Encode the movie title to make it URL-safe
        encoded_title = urllib.parse.quote(title)
        # Search for the movie using TMDB API
        search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={encoded_title}"
        search_response = requests.get(search_url, timeout=5)
        search_data = search_response.json()

        if search_data.get('results'):
            # Get the first search result's movie ID and poster path
            movie_id = search_data['results'][0]['id']
            poster_path = search_data['results'][0].get('poster_path')

            # Get additional details to fetch the IMDb ID
            details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
            details_response = requests.get(details_url, timeout=5)
            details_data = details_response.json()
            imdb_id = details_data.get('imdb_id')

            # Construct poster and IMDb URLs
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else url_for('static', filename='default.jpg')
            imdb_url = f"https://www.imdb.com/title/{imdb_id}/" if imdb_id else None

            return poster_url, imdb_url
        else:
            # No results, return default poster
            return url_for('static', filename='default.jpg'), None

    except Exception as e:
        # Handle errors gracefully and return default poster
        print("Error fetching poster or IMDb link:", e)
        return url_for('static', filename='default.jpg'), None


def recommend(movie_title):
    """
    Recommends top 5 movies similar to the given movie title based on cosine similarity of vector embeddings.
    Returns a list of dictionaries containing title, poster URL, and IMDb URL for each recommended movie.
    """
    # Find the index of the movie with the given title (case-insensitive)
    idx = moviess[moviess['title'].str.lower() == movie_title.lower()].index
    if len(idx) == 0:
        # Movie not found in the dataset
        print("Movie not found.")
        return []

    idx = idx[0]
    # Compute cosine similarity between the given movie vector and all others
    distances = cosine_similarity(vectors[idx], vectors)
    # Get indices for top 5 most similar movies excluding the queried movie itself
    movie_list = sorted(list(enumerate(distances[0])), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    for i in movie_list:
        title = moviess.iloc[i[0]].title
        # Fetch poster and IMDb URL for each recommended movie
        poster, imdb = fetch_poster(title)
        recommendations.append({
            'title': title,
            'poster': poster,
            'imdb': imdb
        })

    return recommendations