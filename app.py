from flask import Flask, render_template, request
from content_filter import recommend, fetch_poster
import pickle

app = Flask(__name__)

# Load the movies dataframe from the pickle file
movies = pickle.load(open('models/movies.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route for the web application.
    Handles displaying the movie selection form and showing recommendations.
    """
    recommended = []
    if request.method == 'POST':
        # Get the movie title submitted by the user
        movie = request.form['movie']
        # Optionally fetch the poster (though not used directly here)
        poster_url = fetch_poster(movie)
        # Get a list of recommended movies based on the selected movie
        recommended = recommend(movie)
    # Render the main page with the first 100 movie titles and recommendations
    return render_template('index.html', movies=movies['title'].head(100).values, recommended=recommended)


if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)