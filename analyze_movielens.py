# module to analyze and say something useful about the movie lens data

def all_ratings(ratings, movie_id):
    '''gets all ratings for one movie, given a rating dict and the movie id'''
    all_ratings = [rating for rating in ratings if rating.movie == movie_id]
    return all_ratings


def avg_rating():
    pass


def all_users_ratings():
    pass


def top_n_tags():
    pass

def bottom_n_tags():
    pass
