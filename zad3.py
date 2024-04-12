import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

class Movie:
    def __init__(self, movie_id, title, genres):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres.split('|')

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'title': self.title,
            'genres': self.genres
        }

class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def to_dict(self):
        return {
            'movie_id': self.movie_id,
            'imdb_id': self.imdb_id,
            'tmdb_id': self.tmdb_id
        }

class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'user_id': str(self.user_id),
            'movie_id': str(self.movie_id),
            'rating': self.rating,
            'timestamp': str(self.timestamp)
        }

class Tag:
    def __init__(self, user_id, movie_id, tag, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'user_id': str(self.user_id),
            'movie_id': str(self.movie_id),
            'tag': self.tag,
            'timestamp': str(self.timestamp)
        }

def load_movies(filepath):
    movies_df = pd.read_csv(filepath)
    movies = [Movie(row['movieId'], row['title'], row['genres']) for _, row in movies_df.iterrows()]
    return movies

def load_links(filepath):
    links_df = pd.read_csv(filepath)
    links = [Link(row['movieId'], row['imdbId'], row['tmdbId']) for _, row in links_df.iterrows()]
    return links

def load_ratings(filepath):
    ratings_df = pd.read_csv(filepath)
    ratings = [Rating(row['userId'], row['movieId'], row['rating'], row['timestamp']) for _, row in ratings_df.iterrows()]
    return ratings

def load_tags(filepath):
    tags_df = pd.read_csv(filepath)
    tags = [Rating(row['userId'], row['movieId'], row['tag'], row['timestamp']) for _, row in tags_df.iterrows()]
    return tags

@app.route('/movies')
def movies_endpoint():
    filepath = 'database/movies.csv' 
    movies = load_movies(filepath)
    return jsonify([movie.to_dict() for movie in movies])

@app.route('/links')
def links_endpoint():
    filepath = 'database/links.csv'
    links = load_links(filepath)
    return jsonify([link.to_dict() for link in links])

@app.route('/ratings')
def ratings_endpoint():
    filepath = 'database/ratings.csv'
    ratings = load_ratings(filepath)
    return jsonify([rating.to_dict() for rating in ratings])

@app.route('/tags')
def tags_endpoint():
    filepath = 'database/tags.csv'
    tags = load_tags(filepath)
    return jsonify([tag.to_dict() for tag in tags])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

