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
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x,y])
    if(len(zeros) > 0):
        i = random.randint(0, len(zeros)-1)
        a = random.random()
        if(a <= 1/9):
            return(zeros[i][0], zeros[i][1], 2)
        else:
            return(zeros[i][0], zeros[i][1], 1)
    else:
        return None

SIZE = 4
EMPTYBOARD = [[0] * SIZE for i in range(SIZE)]
print(random_tile(EMPTYBOARD))


def first_direction(board):
    for d in rules.DIRECTIONS:
        if rules.move_dir_possible(d, board):
            return d


def first_tile(board):
    for i in range(rules.LAST, -1, -1):
        for j in range(rules.LAST, -1, -1):
            if board[i][j] == 0:
                return (i, j, 2)
                
def basic_coop_direction(board):
    if(rules.is_full(board)):
        return None
    m = 0
    a = 0
    for i in range(3): 
        if rules.move_dir(i,board) != board:
            s = basic_coop_score(rules.move_dir(i,board))
            if s > m:
                m = s
                a = i
    if m == 0:
        a = 3
    return a
    
def basic_coop_score(board):
   return rules.level(board)


def basic_coop_tile(board):
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x,y])
    m = 0
    a = 0
    if(len(zeros) > 0):
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            b[zeros[i][0]][zeros[i][1]] = 2
            s = basic_coop_score(b)
            if s > m:
                m = s
                a = i
        return (zeros[a][0], zeros[a][1], 2)
    else:
        return None

#Recursive coop players

def coop_direction(board):
    if(rules.is_full(board)):
        return None
    m = 0
    a = 0
    for i in range(3): 
        if rules.move_dir(i,board) != board:
            s = coop_score_dir(rules.move_dir(i,board), 4)
            if s > m:
                m = s
                a = i
    if m == 0:
        a = 3
    return a

def coop_score_dir(board, depth):
    if depth > 0:
        m = 0
        a = 0
        for i in range(3): 
            if rules.move_dir(i,board) != board:
                s = basic_coop_score(rules.move_dir(i,board))
                if s > m:
                    m = s
                    a = i
        if m == 0:
            a = 3
        ret = rules.move_dir(a, board)
        return(coop_score_tile(ret, depth-1))
    else :
        return basic_coop_score(board)   
    
def coop_tile(board):
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x,y])
    m = 0
    a = 0
    if(len(zeros) > 0):
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            b[zeros[i][0]][zeros[i][1]] = 2
            s = coop_score_tile(b, 4)
            if s > m:
                m = s
                a = i
        return (zeros[a][0], zeros[a][1], 2)
    else:
        return None
    
def coop_score_tile(board, depth):
    if depth > 0:
        zeros = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    zeros.append([x,y])
        m = 0
        ret = []
        if(len(zeros) > 0):
            for i in range(len(zeros)):
                b = [board[i].copy() for i in range(SIZE)]
                b[zeros[i][0]][zeros[i][1]] = 2
                s = basic_coop_score(b)
                if s > m:
                    m = s
                    ret = b
        return(coop_score_dir(ret, depth-1))
    else :
        return basic_coop_score(board)

    

