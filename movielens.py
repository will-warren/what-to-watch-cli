# class file for data models
# Movie, Rater, Rating classes
from math import sqrt


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

    def filter_movies(self, n=10):
        '''creates a list of tuples (movie title, avg rating)
            for movies with more than n ratings default is 10 ratings'''
        movie_avgs = []
        for movie, rating in self.movie_ratings.items():
            if len(rating) > n:
                movie_avgs.append((self.get_avg_rating(movie),
                                  self.movies[movie].title))
        return movie_avgs

    def rank_all_movies(self, n):
        '''returns ranked list of all movies with at least 10 ratings n movies long'''
        qualified_movies = self.filter_movies()
        movie_rank = sorted(qualified_movies, reverse=True)
        return movie_rank[:n]

    def find_unseen_movies(self, user_id):
        '''finds all movies a user hasn't seen, given their id'''
        return [movie for movie in self.movies.keys()
                if movie not in self.user_ratings[user_id]]

    def rank_unseen_movies(self, user_id, n=5):
        '''ranks unseen movies, returns top n, default set to five'''
        unseen_movies = self.find_unseen_movies(user_id)
        rank_unseen_movies = sorted(self.filter_movies(), reverse=True)
        return rank_unseen_movies[:n]

    def get_euclidean_distance(self, user1, user2):
        """taking two lists of movies a user has seen, we find the distance between them, the distance being how similar they are on a scale from 0 to 1. 1 means 100 percent identical"""

        if len(self.user_ratings[user1]) is 0:
            return 0

        user1_ratings = [rating.rating for rating in self.user_ratings[user1]]
        user2_ratings = [rating.rating for rating in self.user_ratings[user2]]
        user1_ratings_num = sorted(user1_ratings)
        user2_ratings_num = sorted(user2_ratings)

        difference = [float(user1_ratings_num[i]) - float(user2_ratings_num[i])
                      for i in range(min([len(user1_ratings_num), len(user2_ratings_num)]))]

        squares = [diff ** 2 for diff in difference]
        sum_of_squares = sum(squares)

        return 1 / (1 + sqrt(sum_of_squares))

    def find_most_similar_user(self, user_id):
        '''finds the most similar user, and who may have a good movie
        to reccommend to us'''

        most_similar_user = ''
        score = 0
        for user in self.user_ratings.keys():
            if user != user_id:
                euc_dist = self.get_euclidean_distance(user_id, user)
                if score < euc_dist:
                    score = euc_dist
                    most_similar_user = user
        return most_similar_user

    def recommend_unseen_movies(self, userId):
        '''recommends movies from the matched user that current user hasn't seen'''
        matched_user = self.find_most_similar_user(userId)
        rec_movies_by_title = []
        user1_movies = set([rating.movie for rating in self.user_ratings[userId]])
        matched_user_movies = set([rating.movie for rating
                                  in self.user_ratings[matched_user]])
        rec_list = matched_user_movies - user1_movies
        for movie in rec_list:
            rec_movies_by_title.append((self.get_avg_rating(movie), self.movies[movie]))
        rec_movies = sorted(rec_movies_by_title, reverse=True)
        return rec_movies[:10]
