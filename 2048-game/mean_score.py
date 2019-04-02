#! /usr/bin/env python3
"""
Compute the average score to '2048' between automatic players.
"""

import rules
import config
import time


def game_direction_first(dir_player, tile_player, board):
    """Plays a game on board when dir_player is the first player"""
    if not dir_player(board):
        assert rules.is_full(board) is True
    i = 0
    while dir_player(board) is not None:
        board = rules.move_dir(dir_player(board), board)
        tile = tile_player(board)
        if tile is not None:
            rules.move_tile(tile_player(board), board)
            i += 1
        else:
            assert rules.move_tile is None

    return 2**rules.max_tile(board), i


def game_tile_first(dir_player, tile_player, board):
    """Plays a game on board when tile_player is the first player"""
    board2 = [board[i].copy() for i in range(rules.SIZE)]
    if not dir_player(board):
        assert rules.game_over(board) is True
    i = 0
    while tile_player(board2) is not None:
        rules.move_tile(tile_player(board2), board2)
        dir = dir_player(board2)
        i += 1
        if dir is not None:
            board2 = rules.move_dir(dir, board2)
        else:
            assert rules.game_over(board2) is True
    return 2 ** rules.max_tile(board2), i

def mean_score():
    if config.FIRST_PLAYER == 0:
        game = game_tile_first
    else:
        game = game_direction_first
        # NB: direction can not start the game on a empty board !
        assert (config.INIT_BOARD != rules.EMPTYBOARD)
    # NB: no interactive players here !
    assert config.TILE_PLAYER is not None
    assert config.DIRECTION_PLAYER is not None
    n = 0
    s = 0
    best = 0
    nbest = 0
    worst = None
    nworst = 0
    INIT_TIME = time.clock()
    for i in range(config.GAMES_NUMBER):
        print("running game:", i + 1)
        ss, nn = game(config.DIRECTION_PLAYER,
                      config.TILE_PLAYER,
                      config.INIT_BOARD)
        n += nn
        s += ss
        if ss > best:
            best = ss
            nbest = 1
        elif ss == best:
            nbest += 1
        if worst is None or ss < worst:
            worst = ss
            nworst = 1
        elif ss == worst:
            nworst += 1
    print("TOTAL TIME:", time.clock() - INIT_TIME)
    print("MEAN MAX TILE:{0} -- MEAN TILE NUMBER: {1}".format(
        s / config.GAMES_NUMBER,
        n / config.GAMES_NUMBER))
    print("MAX of MAX TILE:{0} -- PROBA: {1}".format(
        best,
        nbest / config.GAMES_NUMBER))
    print("MIN of MAX TILE:{0} -- PROBA: {1}".format(
        worst,
        nworst / config.GAMES_NUMBER))


# CODE TO RUN when the file is used as a single executable
if __name__ == "__main__":
    mean_score()

# SIMULATIONS :
# First Tile VS First Dir : tuile max = 512
# Rand Tile VS Rand Dir : tuile max moyenne = 104.76 (max = 256)
# Rand Tile VS First Dir : tuile max moyenne = 198.95 (max = 1024)
