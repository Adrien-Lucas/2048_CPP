"""rules of 2048 game + auxiliary functions"""

DIRECTIONS = tuple(range(4))
DOWN, LEFT, RIGHT, UP = DIRECTIONS
DIR_NAME = ('DOWN', 'LEFT', 'RIGHT', 'UP')
SIZE = 4  # board size
LAST = SIZE - 1


# PERMUTATIONS
   
IDENTITY = tuple(tuple((i, j) for j in range(SIZE)) for i in range(SIZE))
MIRROR = tuple(tuple((i, j) for j in reversed(range(SIZE))) for i in range(SIZE))
TRANSPOSE = tuple(tuple((j, i) for j in range(SIZE)) for i in range(SIZE))
ANTITRANS = tuple(tuple((j, i) for j in reversed(range(SIZE))) for i in reversed(range(SIZE)))

PERM = (
    ANTITRANS, # DOWN
    IDENTITY,  # LEFT
    MIRROR,    # RIGHT
    TRANSPOSE  # UP
)


# A few predefined boards

EMPTYBOARD = [[0] * SIZE for i in range(SIZE)]

STEP0 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [3, 2, 0, 0]
]

FULLBOARD = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

XFULLBOARD = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 3, 2],
    [4, 1, 5, 5]
]

FINAL1 = [
    [2, 4, 5, 2],
    [9, 8, 7, 4],
    [10, 11, 12, 13],
    [17, 16, 15, 14]
]


def move_tile(new_tile_move, board):
    """set on a new tile on the board
       'new_tile_move' is given as a triple (i,j,log2_value)
       where (i,j) is the position of the tile
       and 2**log2_value is the value of the tile"""
    i, j, log2_value = new_tile_move
    if not ((log2_value == 1 or log2_value == 2) and board[i][j] == 0):
        raise AssertionError
    board[i][j] = log2_value


def is_full(board):
    """test whether the board has no empty cell"""
    for l in board:
        for v in l:
            if v == 0:
                return False
    return True


def slide_is_possible(board, i, perm=IDENTITY):
    """test whether a LEFT move_dir applied to line 'i' is possible 
       on the 'board' permutated by 'perm'

       contents follows the log convention:
       0 means "empty cell" and N>0 means "cell containing 2 ** N".
    """
    for n in range(len(board[i])-1):
        if board[perm[i][n][0]][perm[i][n][1]] == 0:
            if board[perm[i][n+1][0]][perm[i][n+1][1]] != 0 :
                return True
            else:
                continue
        elif board[perm[i][n][0]][perm[i][n][1]] == board[perm[i][n+1][0]][perm[i][n+1][1]]:
            return True
        else :
            continue
    return False


def move_dir_possible(direction, board):
    """test whether a move_dir applied on board is possible."""

    for i in range(SIZE):
        if slide_is_possible(board, i, PERM[direction]):
            return True
        else:
            continue
    return False


def game_over(board):
    """check if a direction can be played !
       PRECONDITION: the board is not empty !
    """
    
    for i in range(0,4):
        if(move_dir_possible(PERM[i], board) == False):
            return True
    return False


def slide(in_board, out_board, i, perm=IDENTITY):
    """performs the slide inside board (for the same slide than in 
       slide_is_possible(board, i, perm)
       
    For example, if the line was initially [2, 2, 0, 0]
    then it becomes [3, 0, 0, 0].

    Returns True iff 'board' has changed
    """
    raise NotImplementedError()
    return slide_is_possible(board, i, perm)  # A CHANGER POUR GAGNER EN EFFICACITE


def move_dir(direction, board):
    """Returns a board resulting from the slide of 'board'
       according to 'direction'.
       'board' remains unchanged.
       The resulting board 'res' satisfies 'res == board' iff 'res is board'
    """
    raise NotImplementedError()



def level(board):
    """evaluation of the board (should only increase on well-played games)"""
    raise NotImplementedError()


def max_tile(board):
    """return the max tile on the board."""
    res = 0
    for l in board:
        for v in l:
            if v > res:
                res = v
    return res


def score(board):
    res = max_tile(board)
    if res == 0:
        return res
    return 1 << res  # equiv to 2 ** res


# -- Example of observer for play2048 below
# This function is blocking for play2048
# For example:
#  'input' function below waits a response of the user;
#  in the meanwhile, the GUI is stopped and no more responsive to events !


log = 0
PLAYER_NAME = ('TILE', 'DIRECTION')


def observer_example(board, player):
    """player is the next player in play2048.py"""
    global log
    v = max_tile(board)
    if v > log:
        print('reach', 1 << v, ' on board: ', board)
        print('next player is:', PLAYER_NAME[player])
        log = v
        input('press return to continue --')

