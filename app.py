from flask import Flask, render_template, request
from content_filter import recommend, fetch_poster
import pickle

app = Flask(__name__)

movies = pickle.load(open('models/movies.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended = []
    if request.method == 'POST':
        movie = request.form['movie']
        poster_url = fetch_poster(movie)
        recommended = recommend(movie)
    return render_template('index.html', movies=movies['title'].head(100).values, recommended=recommended)


if __name__ == '__main__':
    app.run(debug=True)