# class file for data models
# Movie, Rater, Rating classes
import re


class Movie:
    def __init__(self, **kwargs):
        self.id = kwargs.get('movieId')
        self.title = kwargs.get('title')
        self.genres = kwargs.get('genres').split('|')

    def __repr__(self):
        return 'Movie({}, {}, {})'.format(self.id, self.title, self.genres)

    def __str__(self):
        return self.__repr__()

    def get_title_by_id(self, movie_id):
        try:
            if movie_id == self.id:
                return self.title
        except:
            return "sorry that movie doesn't exist"
class Rating:
    def __init__(self, **kwargs):
        self.user = kwargs.get('userId')
        self.movie = kwargs.get('movieId')
        self.rating = kwargs.get('rating')
        self.created = kwargs.get('timestamp')

    def __repr__(self, **kwargs):
        return 'Rating({}, {}, {}, {})'.format(self.user, self.movie,
                                               self.rating, self.created)

    def __str__(self):
                return self.__repr__()


class Tag:
    def __init__(self, **kwargs):
        self.user = kwargs.get('userId')
        self.movie = kwargs.get('movieId')
        self.tag = kwargs.get('tag').split(',')
        self.timestamp = kwargs.get('timestamp')

    def __repr__(self):
        return 'Tag({}, {}, {}, {})'.format(self.user, self.movie,
                                            self.tag, self.timestamp)

    def __str__(self):
        return self.__repr__()


class Link:
    def __init__(self, **kwargs):
        self.movie = kwargs.get('movieId')
        self.imdb = kwargs.get('imdbId')
        self.tmdb = kwargs.get('tmdbId')

    def __repr__(self):
        return 'Link({}, {}, {})'.format(self.movie, self.imdb, self.tmdb)

    def __str__(self):
        return self.__repr__()


class Calculate:
    def __init__(self, **kwargs):
        self.movies = kwargs.get('movies')
        self.user_ratings = kwargs.get('user_ratings')
        self.movie_ratings = kwargs.get('movie_ratings')
        self.tags = kwargs.get('tags')
        self.links = kwargs.get('links')

    def all_ratings_user(self, user_id):
        '''returns all ratings by a single user, given its ID'''
        return [rating for rating in self.ratings if rating.user == user_id]

    def all_ratings_movie(self, movie_id):
        '''returns all ratings for a movie, given its ID'''
        return self.movie_ratings[movie_id]

    def get_avg_rating(self, movie_id):
        '''returns the average rating for a movie, given its ID'''
        total_ratings = self.movie_ratings[movie_id]
        return round(sum(float(r.rating) for r in total_ratings)
                    / len(total_ratings), 3)

    def filter_movies(self, n):
        '''creates a list of tuples (movie title, avg rating)
            for movies with more than n ratings'''
        movie_avgs = []
        for movie, rating in self.movie_ratings.items():
            if len(rating) > n:
                movie_avgs.append((self.movies[movie].title,
                                    self.get_avg_rating(movie)))
        return movie_avgs

    def rank_movies(self, n):
        '''returns ranked  list of movies with at least 10 ratings n movies long'''
        movie_rank = []
        qualified_movies = self.filter_movies(10)
        for movie in qualified_movies:
            m = max(float(movie[1]))
            movie_rank.append(m)
            qualified_movies.remove(m)
        return movie_rank.slice[:n]
        #
