# module to load movie data
import csv
from movielens import Movie, Rating, Tag, Link


def load_data():

    """loads all the data, returns as a tuple of
    (movies, ratings, tags, links)"""
    movie_path = 'movies.csv'
    movies = []
    with open(movie_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['movieId', 'title', 'genres'])
        for row in reader:
            movies.append(Movie(**row))

    """load ratings"""

    rating_path = 'ratings.csv'
    ratings = []
    with open(rating_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['userId', 'movieId', 'rating',
                                            'timestamp'])
        for row in reader:
            ratings.append(Rating(**row))

    """load tags"""

    tag_path = 'tags.csv'
    tags = []
    with open(tag_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['userId', 'movieId',
                                            'tag', 'timestamp'])
        for row in reader:
            tags.append(Tag(**row))

    """load links"""

    link_path = 'links.csv'
    links = []
    with open(link_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['movieId', 'imdbId', 'tmdbId'])
        for row in reader:
            links.append(Link(**row))

    """return data as a tuple: movie, rating, tag, link = load_data()"""
    return movies, ratings, tags, links
