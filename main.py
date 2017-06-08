from load_movielens import load_data
# from analyze_movielens import all_ratings, avg_rating, all_users_ratings
from movielens import Calculate
import os

def main():
    os.system('clear')
    print("Welcome to Movie Lens!")
    movies, user_ratings, movie_ratings, tags, links = load_data()
    data = {
        'movies': movies,
        'user_ratings': user_ratings,
        'movie_ratings': movie_ratings,
        'tags': tags,
        'links': links
    }
    c = Calculate(**load_data())
    print("The 5 most popular movies are: ")
    print(c.rank_movies(5))
    print("")
    user_id = input('Enter your User Id: ')
    while(True):
        print('Choose an Option')
        print('(1)List of Unseen Movies\n(2)List of Personalized Recommedations\n(Q)uit')
        choice = input('Enter your choice: ')
        if(choice.upper() == 'Q'):
            print("Goodbye!")
            exit()
        elif choice == '1':
            print('Try one of these!')
            print(c.find_unseen_movies(user_id))
        elif choice == '2':
            print('Based on users similar to you, we recommend:')
            print(c.recommend_unseen_movies(user_id))
        else:
            print('That wasn\'t a correct choice, try again.')

if __name__ == '__main__':
    main()
