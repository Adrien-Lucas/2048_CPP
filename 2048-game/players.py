# -*- coding: utf-8 -*-

import rules
import random
import config
from math import inf

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
                return i, j, 2


def basic_coop_direction(board):
    if rules.is_full(board):
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
    quality = 0
    
    for x in range(len(board)):
        for y in range(len(board[x])):

            if x % 2 == 0:
                Y = y
            else:
                Y = len(board) - 1 - y
            quality += board[x][Y] * (18 ** (x * len(board) + Y))
    # Pour serpentiner, on donne de la qualité si les grosses tuiles se disposent de façon serpentinné
    # c'est à dire si les grosses tuiles sont proches de la fin du tableau avec l'ordre de répartition qui
    # s'inverse à chaque ligne. 
    
    
    #return(rules.level(board))
    return (quality, 0)


def basic_coop_tile(board):
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x,y])
    m = 0
    a = 0
    if len(zeros) > 0:
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            b[zeros[i][0]][zeros[i][1]] = 2
            s = basic_coop_score(b)
            if s > m:
                m = s
                a = i
        return zeros[a][0], zeros[a][1], 2
    else:
        return None

# ---------- Recursive coop players ----------


def key(board):
    """returns the value for the key of the board in the memo dict"""
    res = ''.join(format(e, '02X') for i in range(rules.SIZE)for e in board[i])  # On utilise hex pour éviter ls doubles
    res = hex(int(res, 16))  # on passe en hexadécimal pour réduire l'usage mémoire
    return res


def coop_direction(board):
    global MemoDir
    MemoDir = {}
    if rules.game_over(board):
        return None
    m = ()
    a = 0
    for i in range(3): 
        md = rules.move_dir(i, board)
        if md != board:
            s = coop_score_dir(md, config.DEPTH)
            if s > m:
                m = s
                a = i
    if m == ():
        a = 3
    return a


def coop_score_dir(board, depth):
    idx = key(board)
    if idx in MemoDir:
        return MemoDir[idx]
    if depth > 0:
        m = ()
        a = 0
        for i in rules.DIRECTIONS: 
            md = rules.move_dir(i, board)
            if md != board:
                s = coop_score_tile(md, depth-1)
                if s > m:
                    m = s
                    a = i
        if m == ():
            a = 3
        res = m
        MemoDir[idx] = res
        return res
    else:
        MemoDir[idx] = basic_coop_score(board)
        return basic_coop_score(board)   


def coop_tile(board):
    global MemoTile
    MemoTile = {}
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x, y])
    m = ()
    a = 0
    if len(zeros) == 0:
        return None
    # profondeur progressive : on limite depth quand il y a un gd nb de tuiles vides afin de gagner en performances
    if len(zeros) > 5:
        depth = 2
    else:
        depth = config.DEPTH
    for i in range(len(zeros)):
        b = [board[i].copy() for i in range(SIZE)]
        b[zeros[i][0]][zeros[i][1]] = 2
        s = coop_score_tile(b, depth)
        if s > m:
            m = s
            a = i
    return zeros[a][0], zeros[a][1], 2


def coop_score_tile(board, depth):
    idx = key(board)
    if idx in MemoTile:
        return MemoTile[idx]
    if depth > 0:
        zeros = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    zeros.append([x, y])
        m = ()
        ret = []
        for i in range(len(zeros)):
            b = [board[i].copy() for i in range(SIZE)]
            b[zeros[i][0]][zeros[i][1]] = 2
            s = coop_score_dir(b, depth-1)
            if s > m:
                m = s
                ret = b
        MemoTile[idx] = basic_coop_score(ret)
        return m
    else:
        MemoTile[idx] = basic_coop_score(board)
        return basic_coop_score(board)

# ---------- Recursive comp players ----------


def comp_score(board):
    """return a score for a specified board so as to optimise the comp players"""
    maxb = rules.max_tile(board)
    if maxb == 0:
        maxb = None
    coef = 0
    # On favorise les board ou la tuile max est sur un bord / un coin
    if maxb in (board[0] or board[rules.LAST]):
        coef += 2
    if maxb in ((board[i][0] for i in range(SIZE)) or (board[i][rules.LAST] for i in range(SIZE))):
        coef += 2
    # Favorise les board où les tuiles de grande valeur sont sur la même ligne

    for i in range(SIZE):
            coef += max(sum(board[i]) - 4 * min(board[i]), 0)
    return coef*rules.level(board)


def comp_dir(board):
    #  Inutile ici : le game over est géré par play2048
    # if (board != EMPTYBOARD) and (rules.game_over(board)):
    #     return None
    global MemoDir
    MemoDir = {}
    m = 0
    a = 0
    for i in rules.DIRECTIONS: 
        if rules.move_dir(i, board) != board:
            s = comp_score_dir(rules.move_dir(i, board), config.DEPTH)
            if s > m:
                m = s
                a = i        
    return a
    

def comp_tile(board):
    """Tile player trying to return the position of the tile to add leading to the minimum score
    ACHTUNG : for some reason, only works with depth below 2"""
    global MemoTile
    MemoTile = {}
    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x, y])
    m = inf
    a = 0
    val = 1
    if len(zeros) == 0:  # Nécessaire pour le game-over des mean_score
        return None
    for i in range(len(zeros)):
        b1, b2 = ([board[i].copy() for i in range(SIZE)] for k in'##')
        b1[zeros[i][0]][zeros[i][1]], b2[zeros[i][0]][zeros[i][1]] = 1, 2
        tst = [comp_score_tile(b,  config.DEPTH) for b in (b1, b2)]
        if min(tst) < m:
                m = min(tst)
                a = i
                val = tst.index(min(tst)) + 1
    return zeros[a][0], zeros[a][1], val


def comp_score_dir(board, depth):
    idx = (key(board), depth)
    if idx in MemoDir:
        return MemoDir[idx]
    if depth > 0:
        m = 0
        for i in rules.DIRECTIONS: 
            if rules.move_dir(i, board) != board:
                s = comp_score_dir(rules.move_dir(i, board), depth - 1)
                if s > m:
                    m = s
        MemoDir[idx] = m
        return m
    else:
        MemoDir[idx] = comp_score(board)
        return comp_score(board)
    
    
def comp_score_tile(board, depth):
    """Returns the minimum score available for a specified depth & board"""
    idx = (key(board), depth)
    if idx in MemoTile:
        return MemoTile[idx]
    if depth > 0:
        zeros = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    zeros.append([x, y])
        m = inf
        Outb = []
        for i in range(len(zeros)):
            b1, b2 = ([board[i].copy() for i in range(SIZE)] for k in '##')
            (rules.move_tile(zeros[i] + [n], b) for (n, b) in ((1, b1), (2, b2)))
            tst = [comp_score_tile(b,  depth - 1) for b in (b1, b2)]
            if min(tst) < m:
                m = min(tst)
                Outb = (b1, b2)[tst.index(min(tst))]
        MemoTile[idx] = m
        return m
    else:
        MemoTile[idx] = comp_score(board)
        return comp_score(board)
