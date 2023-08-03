import numpy as np
import random


def build_board(size):
    options = ['Empty', 'Red', 'Black']
    board = np.random.choice(options, size=(size, size))
    return board

def get_count(board, item):
    return np.count_nonzero(board == item)


if __name__ == "__name__":
    print("This file is not intended to be run as the main file.")