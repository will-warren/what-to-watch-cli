from load_movielens import load_data
# from analyze_movielens import all_ratings, avg_rating, all_users_ratings
from movielens import Calculate


def main():
    movies, user_ratings, movie_ratings, tags, links = load_data()
    data = {
        'movies': movies,
        'user_ratings': user_ratings,
        'movie_ratings': movie_ratings,
        'tags': tags,
        'links': links
    }
    c = Calculate(**data)
    print(c.rank_movies(25))


main()
