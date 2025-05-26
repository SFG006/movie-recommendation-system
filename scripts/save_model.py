# save_model.py

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from recommend_utils import collapse

# Load your dataset
moviess = pd.read_csv("../data/TMDB_movie_dataset_v11.csv")

# Preprocess text columns
moviess.fillna('', inplace=True)

moviess['tags'] = (moviess['title'] + ' ' +
                   moviess['overview'] + ' ' +
                   moviess['tagline'] + ' ' +
                   moviess['genres'].apply(collapse) + ' ' +
                   moviess['keywords'].apply(collapse) + ' ' +
                   moviess['production_companies'].apply(collapse) + ' ' +
                   moviess['spoken_languages'].apply(collapse) + ' ' +
                   moviess['original_language'])

# Vectorize
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(moviess['tags'])

# Save models
pickle.dump(moviess, open('../models/movies.pkl', 'wb'))
pickle.dump(cv, open('../models/vectorizer.pkl', 'wb'))
pickle.dump(vectors, open('../models/vectors.pkl', 'wb'))
