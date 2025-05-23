import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity

API_KEY = '1785d39c9dc62729cb9c119ae7957953'  # 🔁 Replace this with your actual API key


def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        for movie in data['results']:
            poster_path = movie.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
    return "/static/no_poster_available.png"




moviess = pickle.load(open('models/movies.pkl', 'rb'))
vectors = pickle.load(open('models/vectors.pkl', 'rb'))

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
        poster = fetch_poster(title)
        recommendations.append({'title': title, 'poster': poster})

    return recommendations
