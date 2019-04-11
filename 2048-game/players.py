# -*- coding: utf-8 -*-

import rules
import random

MemoDir = {}
MemoTile = {}

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
# print(random_tile(EMPTYBOARD))


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

def key(board):
    """returns the value for the key of the board in the memo dict"""
    res = ''.join(str(e) for i in range(rules.SIZE)for e in board[i])
    res = hex(int(res)) # on passe en hexadécimal c'est moins foireux
    return res

def coop_direction(board):
    global MemoDir
    MemoDir = {}
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
    idx = key(board)
    if idx in MemoDir:
        return MemoDir[idx]
    if depth > 0:
        m = 0
        a = 0
        for i in rules.DIRECTIONS: 
            if rules.move_dir(i,board) != board:
                s = coop_score_tile(rules.move_dir(i,board), depth-1)
                if s > m:
                    m = s
                    a = i
        if m == 0:
            a = 3
        res = basic_coop_score(rules.move_dir(a, board))
        MemoDir[idx] = res
        return(res)
    else :
        MemoDir[idx] = basic_coop_score(board)
        return basic_coop_score(board)   
    
def coop_tile(board):
    global MemoTile
    MemoTile = {}
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
    idx = key(board)
    if idx in MemoTile:
        return MemoTile[idx]
    if depth > 0:
        zeros = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    zeros.append([x,y])
        m = 0
        ret = []
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            b[zeros[i][0]][zeros[i][1]] = 2
            s = coop_score_dir(b, depth-1)
            if s > m:
                m = s
                ret = b
        MemoTile[idx] = basic_coop_score(ret)
        return(basic_coop_score(ret))
    else :
        MemoTile[idx] = basic_coop_score(board)
        return basic_coop_score(board)


####### Recursive comp players

def comp_dir(board):
    if (board != EMPTYBOARD) and (rules.game_over(board)):
        ValueError()
        return None
    m = 0
    a = 0
    for i in rules.DIRECTIONS: 
        if rules.move_dir(i,board) != board:
            s = comp_score_dir(rules.move_dir(i,board), 4)
            if s > m:
                m = s
                a = i        
    return a
    

def comp_tile(board):
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x, y])
    res = 0
    a = 0
    if(len(zeros) > 0):
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            tst = [comp_score_tile(rules.move_tile(zeros[i] + [n], b), 4) for n in (1, 2)]
            if min(tst) < res:
                res = min(tst)
                val = tst.index(min(tst)) + 1  # on joue 2 si les 2 tiles renvoient le même résultat
                a = i
        return (zeros[a][0], zeros[a][1], val)
    else:
        return None
    

def comp_score_dir(board, depth):
    if depth > 0:
        m = 0
        for i in rules.DIRECTIONS: 
            if rules.move_dir(i,board) != board:
                s = comp_score_dir(rules.move_dir(i,board), depth - 1)
                if s > m:
                    m = s      
        return m
    else :
        return basic_coop_score(board)   
    
    
def comp_score_tile(board, depth):
    if depth > 0 :
        zeros = []
        for x in range(SIZE):
            for y in range(SIZE):
                if board[x][y] == 0:
                    zeros.append([x, y])
        res = 0
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            tst = [comp_score_tile(rules.move_tile(zeros[i] + [n], b), 4) for n in (1, 2)]
            if min(tst) < res:
                res = min(tst)
        return res
    else :
        return basic_coop_score(board)
