import os
import numpy as np
from pathlib2 import Path



def load_data():
    with open('data/train_dates_all.txt', 'r') as file:
        lines = file.readlines()

    return