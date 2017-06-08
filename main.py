from load_movielens import load_data
from movielens import Calculate
import os


def beautify(calc_obj, movies):
    for movie in movies:
        if type(movie) == tuple:
            try:
                print('Movie: {:>40} Rating: {:>10}'.format(movie[1], movie[0]))
            except TypeError:
                print('Movie: {:>40} Rating: {:>10}'.format(movie[1].title, movie[0]))
        else:
            avg = calc_obj.get_avg_rating(movie.id)
            print('Movie: {:>40} Rating: {:>10}'.format(movie.title, avg))


def main():
    os.system('clear')
    print("Welcome to Movie Lens!")

    c = Calculate(**load_data())

    print("The 5 most popular movies are: ")
    print(beautify(c, c.rank_all_movies(5)))
    print('\n')
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
            print(beautify(c, c.rank_unseen_movies(user_id)))
        elif choice == '2':
            print('Based on users similar to you, we recommend:')
            print(beautify(c, c.recommend_unseen_movies(user_id)))
        else:
            print('That wasn\'t a correct choice, try again.')

if __name__ == '__main__':
    main()
