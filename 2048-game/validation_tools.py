# -*- coding: utf-8 -*-
"""
Auxiliary functions for validation. DO NOT MODIFY THIS FILE.
Instead, please copy-paste the needed parts of this file
in "validation_debug.py".
"""
import rules
import players
import mean_score
#import os


# Global variables
current_stage = 0

def version():
    print("### VALIDATION 2048 ---- CPP 2018-2019 ---- version: initial ###")

# ----------------------
# Handling of stages -> old stuff (no more used !)

# STAGE_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)),
#                           ".current_stage.txt")

# def read_stage():
#     global saved_stage
#     try:
#         f = open(STAGE_FILE)
#         res = f.readline()
#         f.close()
#         saved_stage = int(res)
#     except FileNotFoundError:
#         saved_stage = 0
#     except BaseException as e:
#         print("WARNING: reading {0} failed with error {1}".format(
#             repr(STAGE_FILE), e))
#         saved_stage = 0
#     print("# found saved_stage =", saved_stage)


# read_stage()  # init saved_stage

# def save_stage():
#     if current_stage <= saved_stage:
#         return
#     try:
#         f = open(STAGE_FILE, 'w')
#         f.write(repr(current_stage))
#         f.close()
#     except BaseException as e:
#         print("WARNING: writing {0} failed with error {1}".format(
#             STAGE_FILE, e))


def valid_current_stage(name):
    global current_stage
    current_stage += 1
    # if current_stage <= saved_stage:
    #     qmark = ""
    # else:
    #     qmark = "???"
    print("### STAGE {0} ({1}) PASSED ###".
          format(current_stage, name))
    # save_stage()


def conclude():
    # if saved_stage < current_stage:
    #     print("### This is not yet the end... ###")
    #     print("Your 'saved_stage' was {0} !".format(saved_stage))
    #     print("Re-run the script once in order to be sure that everything is ok !")
    # else:
    print("### That's all Folks ! ###")
    print("Fully validates {0} stages !".format(current_stage))
    version()

# ----------------------
# TESTS FUNCTIONS


INDENT = "  "


def start_test(name, indent=""):
    print(indent + "test: " + name)


def assert_equal(actual, expected):
    if actual != expected:
        print("Error ! Expected:", expected)
        print("But Found:", actual)
        assert actual == expected


STAGE_SLIDE_IS_OVER = False

def test_slide_is_possible(line, expected):
    if not STAGE_SLIDE_IS_OVER:
        assert_equal(rules.slide_is_possible([ line ], 0), expected)
        return
    start_test("mimicking with rules.slide", INDENT)
    xline = line.copy()
    res = rules.slide([ line ], [ xline ], 0)
    assert_equal(res, expected)
    if res != (xline != line):
        print("Error of rules.slide on input", line)
        print("Output line=", xline)
        if res:
            print("They are expected to be different")
        else:
            print("They are expected to be equal")
        assert res == (xline != line)


def perm_dir(d, board):
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    for i in range(rules.SIZE):
        for j in range(rules.SIZE):
            ip, jp = rules.PERM[d][i][j]
            xboard[ip][jp] = board[i][j]
    return xboard


def test_move_dir_possible(direction, board, expected):
    if not STAGE_SLIDE_IS_OVER:
        assert_equal(rules.move_dir_possible(direction, board), expected)
        if expected:
            start_test("game not over", INDENT)
            assert not rules.game_over(board)
        return
    start_test("mimicking with rules.move_dir", INDENT)
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    res = rules.move_dir(direction, xboard)
    if expected:
        if res == xboard:
            print("Error of rules.slide on input", xboard)
            print("Output is the same while it should be different")
            assert res != xboard
    elif res is not xboard:
        print("Error of rules.slide on input", xboard)
        print("Output is ", xboard)
        assert xboard is board
    start_test("purity", INDENT)
    assert_equal(board, xboard)


def test_slide(line, expected):
    xline = line.copy()
    res = rules.slide([line], [ xline ], 0)
    assert_equal(xline, expected)
    assert_equal(res, xline != line)


def test_move_dir(direction, board, expected):
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    res = rules.move_dir(direction, xboard)
    assert(res is not xboard)
    assert_equal(res, expected)
    start_test("purity", INDENT)
    assert_equal(board, xboard)


def play_DOWN(board):
    return rules.DOWN


def play_None(board):
    return None


def play_FIRST(board):
    return (0, 0, 1)


def test_game_direction_first(board, expected):
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    r = mean_score.game_direction_first(
        players.first_direction,
        players.first_tile,
        xboard)
    assert_equal(r, expected)
    start_test("purity", INDENT)
    assert_equal(board, xboard)


def torture_game_direction_first(player_d, player_t, board):
    try:
        xboard = [board[i].copy() for i in range(rules.SIZE)]
        r = mean_score.game_direction_first(
            player_d,
            player_t,
            xboard)
    except AssertionError:
        start_test("purity", INDENT)
        assert_equal(board, xboard)
        return
    print("game_direction_first has returned result:", r)
    print("WHEREAS it was expected to fail on an AssertionError !!")
    assert False


def test_game_tile_first(board, expected):
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    r = mean_score.game_tile_first(
        players.first_direction,
        players.first_tile,
        xboard)
    assert_equal(r, expected)
    start_test("purity", INDENT)
    assert_equal(board, xboard)


def torture_game_tile_first(player_d, player_t, board):
    try:
        xboard = [board[i].copy() for i in range(rules.SIZE)]
        r = mean_score.game_tile_first(
            player_d,
            player_t,
            xboard)
    except AssertionError:
        start_test("purity", INDENT)
        assert_equal(board, xboard)
        return
    print("game_tile_first has returned result:", r)
    print("WHEREAS it was expected to fail on an AssertionError !!")
    assert False


def test_invperm(f, board, expected):
    for d in rules.DIRECTIONS:
        start_test("with perm {0}".format(rules.DIR_NAME[d]), INDENT)
        assert_equal(f(perm_dir(d, board)), expected)


def test_xperm(perm, board, expected):
    xboard = [board[i].copy() for i in range(rules.SIZE)]
    fresh = perm(xboard)
    assert_equal(fresh, expected)
    start_test("purity", INDENT)
    assert_equal(board, xboard)


def test_reorder(board, expected):
    pos = rules.max_pos(board)
    assert pos is not None
    print("init board", board)
    xboard = rules.reorder(board, pos)(board)
    assert_equal(xboard, expected)


def torture_reorder(board):
    test_reorder(board, board)
