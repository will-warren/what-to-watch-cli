# module to analyze and say something useful about the movie lens data


def filter_movies(ratings):
    '''filters movies with at least 10 ratings'''
    return len(ratings) >= 10

def rank_movies(movies):
    '''ranks all the movies, with at least 10 reviews'''
    pass


def get_top_n_movies(n):
    '''finds top n movies, given n'''
    pass


def all_users_ratings(user_id, ratings):
    '''gets all ratings a user has submitted'''
    all_users_ratings = [rating for rating in ratings if rating.user == user_id]
    return all_users_ratings


def top_n_tags():
    pass

def bottom_n_tags():
    pass
