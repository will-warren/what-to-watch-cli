# module to load movie data
import csv
from movielens import Movie, Rating, Tag, Link


def load_data():

    """loads all the data, returns as a tuple of
    (movies, ratings, tags, links), movie id is primary key"""
    movie_path = 'movies.csv'
    movies = {}
    with open(movie_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['movieId', 'title', 'genres'])
        for row in reader:
            movies[row['movieId']] = Movie(**row)

    """load ratings, setdefault() prevents overwrites
        (e.g. many ratings for one movie)"""

    rating_path = 'ratings.csv'
    user_ratings = {}
    movie_ratings = {}
    with open(rating_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['userId', 'movieId', 'rating',
                                            'timestamp'])
        for row in reader:
            movie_ratings.setdefault(row['movieId'], []).append(Rating(**row))
            user_ratings.setdefault(row['userId'], []).append(Rating(**row))

    """load tags, tag_count acts as a primary key"""

    tag_path = 'tags.csv'
    tags = {}
    tag_count = 0
    with open(tag_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['userId', 'movieId',
                                            'tag', 'timestamp'])
        for row in reader:
            tags[tag_count] = Tag(**row)
            tag_count += 1

    """load links, link_count acts as primary key"""

    link_path = 'links.csv'
    links = {}
    link_count = 0
    with open(link_path, encoding='latin-1') as f:
        reader = csv.DictReader(f, delimiter=',',
                                fieldnames=['movieId', 'imdbId', 'tmdbId'])
        for row in reader:
            links[link_count] = Link(**row)
            link_count += 1

    """return data as a tup of dicts"""
    return movies, user_ratings, movie_ratings, tags, links
