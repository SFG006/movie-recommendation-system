# 🎬 Movie Recommendation System

This is a **Flask-based Movie Recommendation Web App** that suggests similar movies based on a selected title using **content-based filtering**. It fetches movie posters and IMDb links using the **TMDb API**.

---

### 🚀 Live Demo

Try the app online on Hugging Face Spaces:
[Illustrious Films on Hugging Face](https://huggingface.co/spaces/SFG006/Illustrious-Films)

---

## 🚀 Features

* 🎥 Recommend similar movies using vector-based cosine similarity
* 🖼️ Fetch high-quality posters using the TMDb API
* 🔗 Direct IMDb links for recommended movies
* 💡 Sleek and responsive user interface
* 🧠 Built using Scikit-learn, Flask, and precomputed embeddings

---

## 📂 Project Structure

```plaintext
movie-recommendation-system/
├── app.py
├── content_filter.py
├── Dockerfile
├── requirements.txt
├── models/
│   ├── movies.pkl
│   └── vectors.pkl
├── data/
│   └── movies.csv
├── notebooks/
│   └── development_notebook.ipynb
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## 🛠️ How It Works

### 1. Content-Based Filtering

* Uses **TF-IDF vectorization** of movie descriptions.
* Computes **cosine similarity** between movies.
* Returns top 5 similar movies.

### 2. Poster Fetching

* Integrates with **TMDb API** to fetch:

  * Movie Poster
  * IMDb URL

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/SFG006/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install Dependencies

Make sure you have Python 3.7+ and `pip` installed.

```bash
pip install -r requirements.txt
```

```bash
pip install flask scikit-learn requests
```

### 3. Set Environment Variable

Get your **TMDb API Key** from [TMDb](https://www.themoviedb.org/) and set it:

**On Linux/macOS:**

```bash
export TMDB_API_KEY="your_api_key"
```

**On Windows (Command Prompt):**

```cmd
set TMDB_API_KEY=your_api_key
```

### 4. Run the App

```bash
python app.py
```

The app will run on `http://0.0.0.0:7860`.

---

---

## 🐳 Docker Deployment

To run the application using Docker:

1. **Build the Docker Image**:

   ```bash
   docker build -t movie-recommendation .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -p 7860:7860 --env TMDB_API_KEY=your_api_key_here movie-recommendation
   ```

   * The application will be accessible at `http://localhost:7860/`.

---

## 📸 Screenshots

*(Add a screenshot of your app UI here if you want)*

---

## 📚 Technologies Used

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* TMDb API 🎞️
* HTML5 + CSS3 🎨

---

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## 💬 Acknowledgements

* [TMDb](https://www.themoviedb.org/) for their free API
* Scikit-learn for vector similarity functions

---

## 🧑‍💻 Author

Made with ❤️ by SFG006
