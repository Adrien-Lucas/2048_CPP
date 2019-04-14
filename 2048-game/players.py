# -*- coding: utf-8 -*-

import rules
import random
import config

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


def basic_coop_score(board):  # TODO : Favoriser le serpentin
    quality = 0
    # m = 0
    # m_tile = []
    # for x in range(len(board)):
    #     for y in range(len(board[x])):
    #         if board[x][y] > m:
    #             m = board[x][y]
    #            m_tile = [x, y]
    # sorts = sorted(sorted(board[0])+sorted(board[1])+sorted(board[2])+ sorted(board[3]))
    # snaked = [sorts[0:4] , list(reversed(sorts[4:8])) , sorts[8:12] , list(reversed(sorts[12:16]))]
    # if board == snaked:
    #     quality = 50
    #     # print("WOW")
    
    return quality, rules.level(board)


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
    if rules.is_full(board):
        return None
    m = ()
    a = 0
    for i in range(3): 
        if rules.move_dir(i, board) != board:
            s = coop_score_dir(rules.move_dir(i, board), config.DEPTH)
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
            if rules.move_dir(i, board) != board:
                s = coop_score_tile(rules.move_dir(i, board), depth-1)
                if s > m:
                    m = s
                    a = i
        if m == ():
            a = 3
        res = basic_coop_score(rules.move_dir(a, board))
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
    assert len(zeros) > 0
    for i in range(len(zeros)):
        b = [board[i].copy() for i in range(SIZE)]
        b[zeros[i][0]][zeros[i][1]] = 2
        s = coop_score_tile(b, config.DEPTH)
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
        return basic_coop_score(ret)
    else:
        MemoTile[idx] = basic_coop_score(board)
        return basic_coop_score(board)


# ---------- Recursive comp players ----------

def comp_dir(board):
    #  Inutile ici : le game over est géré par play2048
    # if (board != EMPTYBOARD) and (rules.game_over(board)):
    #     return None
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

    zeros = []
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                zeros.append([x, y])
    m = 1e16
    a = 0

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
    if depth > 0:
        m = 0
        for i in rules.DIRECTIONS: 
            if rules.move_dir(i, board) != board:
                s = comp_score_dir(rules.move_dir(i, board), depth - 1)
                if s > m:
                    m = s      
        return m
    else:
        return rules.level(board)
    
    
def comp_score_tile(board, depth):
    """Returns the minimum score available for a specified depth & board"""
    if depth > 0:
        zeros = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    zeros.append([x, y])
        m = 1e16
        Outb = []
        for i in range(len(zeros)):
            b1, b2 = ([board[i].copy() for i in range(SIZE)] for k in '##')
            (rules.move_tile(zeros[i] + [n], b) for (n, b) in ((1, b1), (2, b2)))
            tst = [comp_score_tile(b,  depth - 1) for b in (b1, b2)]
            if min(tst) < m:
                m = min(tst)
                Outb = (b1, b2)[tst.index(min(tst))]
        return rules.level(Outb)
    else:
        return rules.level(board)
