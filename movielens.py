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

    # def get_name(self):
    #     title = re.search(r'^\(?\d{4}\)', self.title)
    #     print(title)
    #     return "{}".format(title)


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
