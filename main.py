from load_movielens import load_data
from analyze_movielens import all_ratings


def main():
    movies, ratings, tags, links = load_data()
    print(all_ratings(ratings, '1'))


main()
