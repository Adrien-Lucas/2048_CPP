# -*- coding: utf-8 -*-

import rules
import random


def random_direction(board):
    l = [d for d in rules.DIRECTIONS if rules.move_dir_possible(d, board)]
    if l:
        return random.choice(l)


def random_tile(board):
    """returns a random 'tile move' on the board
        where tile 4 has only probably 1/9"""
    raise NotImplementedError()


def first_direction(board):
    for d in rules.DIRECTIONS:
        if rules.move_dir_possible(d, board):
            return d


def first_tile(board):
    for i in range(rules.LAST, -1, -1):
        for j in range(rules.LAST, -1, -1):
            if board[i][j] == 0:
                return (i, j, 2)
