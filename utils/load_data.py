import os
import numpy as np
from pathlib2 import Path


def load_data(set):

    # Load training data
    train_dates_all = np.loadtxt('../data/train_dates_all.txt')
    train_ratings_all = np.loadtxt('../data/train_ratings_all.txt')
    train_y_date = np.loadtxt('../data/train_y_date.txt')
    train_y_rating = np.loadtxt('../data/train_y_rating.txt')

    # Load test data
    test_ratings_all = np.loadtxt('../data/test_ratings_all.txt')
    test_dates_all = np.loadtxt('../data/test_dates_all.txt')
    test_y_date = np.loadtxt('../data/test_y_date.txt')

    # Load Movie Titles
    movie_data = data = np.loadtxt('../data/movie_titles.txt', delimiter=',', dtype=[('year', 'f4'), ('name', 'U50')])
    movie_years = movie_data['year']
    movie_names = movie_data['name']

    if set == 'train':
        return {'train_dates_all' : train_dates_all,
                'train_ratings_all' : train_ratings_all,
                'train_y_date' : train_y_date,
                'train_y_rating' : train_y_rating,
                'movie_years' : movie_years,
                'movie_names' : movie_names}

    elif set == 'test':
        return {'test_dates_all' : test_dates_all,
                'test_ratings_all' : test_ratings_all,
                'test_y_date' : test_y_date,
                'movie_years' : movie_years,
                'movie_names' : movie_names}
    else:
        raise ValueError('Set must be either train or test')
