#! /usr/bin/env python3
"""
Script for validation. DO NOT MODIFY THIS FILE.
Instead, please copy-paste the needed parts of this file
in "validation_debug.py".
"""

import rules
import validation_tools as vt
import players


vt.version()


# ---- STAGE slide_is_possible -----

def tests_slide_is_possible(test_slide):
    vt.STAGE_SLIDE_IS_OVER = test_slide
    #
    vt.start_test('slide impossible with empty line')
    vt.test_slide_is_possible([0, 0, 0, 0], False)
    #
    vt.start_test('slide impossible with full line')
    vt.test_slide_is_possible([1, 2, 1, 2], False)
    #
    vt.start_test('slide impossible with almost full line')
    vt.test_slide_is_possible([3, 2, 3, 0], False)
    #
    vt.start_test('slide impossible with two tiles')
    vt.test_slide_is_possible([1, 3, 0, 0], False)
    #
    vt.start_test('slide impossible with one tile')
    vt.test_slide_is_possible([2, 0, 0, 0], False)
    #
    vt.start_test('slide possible with one tile (pos 1)')
    vt.test_slide_is_possible([0, 1, 0, 0], True)
    #
    vt.start_test('slide with one tile (pos 2)')
    vt.test_slide_is_possible([0, 0, 2, 0], True)
    #
    vt.start_test('slide with one tile (pos 3)')
    vt.test_slide_is_possible([0, 0, 0, 3], True)
    #
    vt.start_test('slide with two different tiles v1')
    vt.test_slide_is_possible([0, 2, 0, 3], True)
    #
    vt.start_test('slide with two different tiles v2')
    vt.test_slide_is_possible([3, 0, 2, 0], True)
    #
    vt.start_test('slide with two different tiles v3')
    vt.test_slide_is_possible([1, 0, 0, 3], True)
    #
    vt.start_test('slide with three different tiles v1')
    vt.test_slide_is_possible([1, 2, 0, 1], True)
    #
    vt.start_test('slide with three different tiles v2')
    vt.test_slide_is_possible([2, 0, 1, 2], True)
    #
    vt.start_test('slide with two identical consecutive tiles v1')
    vt.test_slide_is_possible([1, 1, 0, 0], True)
    #
    vt.start_test('slide with two identical consecutive tiles v2')
    vt.test_slide_is_possible([2, 1, 1, 0], True)
    #
    vt.start_test('slide with two identical consecutive tiles v3')
    vt.test_slide_is_possible([1, 2, 3, 3], True)

tests_slide_is_possible(False)

vt.valid_current_stage("rules.slide_is_possible")
    
# ---- STAGE move_dir_possible + game_over -----

def test_move_dir_possible():
    for d in rules.DIRECTIONS:
        vt.start_test('impossible move dir on ' + rules.DIR_NAME[d] + ' (empty)')
        vt.test_move_dir_possible(d, rules.EMPTYBOARD, False)
        #
    empty1_board = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [0, 14, 15, 16],
    ]
    #
    for d in (rules.RIGHT, rules.UP):
        vt.start_test('impossible move dir on ' + rules.DIR_NAME[d] + ' (empty1)')
        vt.test_move_dir_possible(d, empty1_board, False)
    #
    for d in (rules.LEFT, rules.DOWN):
        vt.start_test('possible move dir on ' + rules.DIR_NAME[d] + ' (empty1)')
        vt.test_move_dir_possible(d, empty1_board, True)
    #
    empty1_board = vt.perm_dir(rules.UP, empty1_board)
    #
    for d in (rules.RIGHT, rules.UP):
        vt.start_test('possible move dir on ' + rules.DIR_NAME[d] + ' (empty1)')
        vt.test_move_dir_possible(d, empty1_board, True)
    #
    for d in (rules.LEFT, rules.DOWN):
        vt.start_test('impossible move dir on ' + rules.DIR_NAME[d] + ' (empty1)')
        vt.test_move_dir_possible(d, empty1_board, False)
    #
    for d in (rules.UP, rules.DOWN):
        vt.start_test('impossible move dir on ' +
                      rules.DIR_NAME[d] + ' (XFULLBOARD)')
        vt.test_move_dir_possible(d, rules.XFULLBOARD, False)
    #
    for d in (rules.LEFT, rules.RIGHT):
        vt.start_test('possible move dir on ' +
                      rules.DIR_NAME[d] + ' (XFULLBOARD)')
        vt.test_move_dir_possible(d, rules.XFULLBOARD, True)
    #
    myboard = vt.perm_dir(rules.DOWN, rules.XFULLBOARD)
    #
    for d in (rules.UP, rules.DOWN):
        vt.start_test('possible move dir on ' +
                      rules.DIR_NAME[d] + ' (XFULLBOARD)')
        vt.test_move_dir_possible(d, myboard, True)
    #
    for d in (rules.LEFT, rules.RIGHT):
        vt.start_test('impossible move dir on ' +
                      rules.DIR_NAME[d] + ' (XFULLBOARD)')
        vt.test_move_dir_possible(d, myboard, False)

test_move_dir_possible()
    
vt.start_test('game.over')
assert rules.game_over(rules.FULLBOARD)

vt.valid_current_stage("move_dir_possible + game_over")


# ---- STAGE slide -----


vt.start_test('slide with zero tile')
vt.test_slide(
    [0, 0, 0, 0],
    [0, 0, 0, 0])

vt.start_test('slide with one tile (pos 0)')
vt.test_slide(
    [4, 0, 0, 0],
    [4, 0, 0, 0])

vt.start_test('slide with one tile (pos 1)')
vt.test_slide(
    [0, 1, 0, 0],
    [1, 0, 0, 0])

vt.start_test('slide with one tile (pos 2)')
vt.test_slide(
    [0, 0, 2, 0],
    [2, 0, 0, 0])

vt.start_test('slide with one tile (pos 3)')
vt.test_slide(
    [0, 0, 0, 3],
    [3, 0, 0, 0])

vt.start_test('slide with two different tiles at bottom')
vt.test_slide(
    [1, 2, 0, 0],
    [1, 2, 0, 0])

vt.start_test('slide with two different tiles v1')
vt.test_slide(
    [0, 2, 0, 3],
    [2, 3, 0, 0])

vt.start_test('slide with two different tiles v2')
vt.test_slide(
    [3, 0, 0, 2],
    [3, 2, 0, 0])

vt.start_test('slide with two identical tiles')
vt.test_slide(
    [0, 1, 0, 1],
    [2, 0, 0, 0])

vt.start_test('slide with two identical consecutive tiles')
vt.test_slide(
    [0, 3, 3, 0],
    [4, 0, 0, 0])

vt.start_test('slide with two identical consecutive tiles at bottom')
vt.test_slide(
    [2, 2, 0, 0],
    [3, 0, 0, 0])

vt.start_test('slide with 3 mixed tiles')
vt.test_slide(
    [2, 1, 0, 2],
    [2, 1, 2, 0])

vt.start_test('slide with 3 identical consecutive tiles')
vt.test_slide(
    [4, 4, 4, 0],
    [5, 4, 0, 0])

vt.start_test('slide with 3 identical non-consecutive tiles')
vt.test_slide(
    [4, 4, 0, 4],
    [5, 4, 0, 0])

vt.start_test('slide with 3 identical tiles ')
vt.test_slide(
    [4, 0, 4, 4],
    [5, 4, 0, 0])

vt.start_test('slide with 2 identical tiles and 1 greater')
vt.test_slide(
    [4, 4, 5, 0],
    [5, 5, 0, 0])

vt.start_test('slide with 1 greater and 2 identical tiles')
vt.test_slide(
    [5, 4, 0, 4],
    [5, 5, 0, 0])

vt.start_test('slide with 4 identical tiles')
vt.test_slide(
    [6, 6, 6, 6],
    [7, 7, 0, 0])


tests_slide_is_possible(True)

vt.valid_current_stage("rules.slide")

# ---- STAGE MOVE_DIR -----

simple_board = [
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 3, 0],
    [0, 0, 0, 0],
]

vt.start_test('Simple rules.move_dir left')
vt.test_move_dir(rules.LEFT, simple_board, [
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [3, 0, 0, 0],
    [0, 0, 0, 0],
])

vt.start_test('Simple rules.move_dir right')
vt.test_move_dir(rules.RIGHT, simple_board, [
    [0, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
])

vt.start_test('Simple rules.move_dir up')
vt.test_move_dir(rules.UP, simple_board, [
    [0, 2, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
])


vt.start_test('Simple rules.move_dir down')
vt.test_move_dir(rules.DOWN, simple_board, [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 2, 3, 0],
])



complex_board= [
    [2, 4, 2, 3], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 2, 0]
]

vt.start_test('Complex rules.move_dir left')
vt.test_move_dir(rules.LEFT, complex_board, [
    [2, 4, 2, 3], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [2, 0, 0, 0]
])

vt.start_test('Complex rules.move_dir right')
vt.test_move_dir(rules.RIGHT, complex_board, [
    [2, 4, 2, 3], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 2]
])

vt.start_test('Complex rules.move_dir down')
vt.test_move_dir(rules.DOWN, complex_board, [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [2, 4, 3, 3]
])

vt.start_test('Complex rules.move_dir up')
vt.test_move_dir(rules.UP, complex_board, [
    [2, 4, 3, 3],
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]
])



complex_board = [
    [2, 2, 2, 1],
    [2, 2, 2, 0],
    [1, 2, 1, 1],
    [1, 0, 0, 0],
]

vt.start_test('Complex rules.move_dir left (2)')
vt.test_move_dir(rules.LEFT, complex_board, [
    [3, 2, 1, 0],
    [3, 2, 0, 0],
    [1, 2, 2, 0],
    [1, 0, 0, 0],
])

vt.start_test('Complex rules.move_dir right (2)')
vt.test_move_dir(rules.RIGHT, complex_board, [
    [0, 2, 3, 1],
    [0, 0, 2, 3],
    [0, 1, 2, 2],
    [0, 0, 0, 1],
])

vt.start_test('Complex rules.move_dir down (2)')
vt.test_move_dir(rules.DOWN, complex_board, [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [3, 2, 3, 0],
    [2, 3, 1, 2],
])

vt.start_test('Complex rules.move_dir up (2)')
vt.test_move_dir(rules.UP, complex_board, [
    [3, 3, 3, 2],
    [2, 2, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
])

test_move_dir_possible()
vt.valid_current_stage("rules.move_dir")

# ---- STAGE MEAN-SCORE -----

vt.start_test('mean_score.game_direction_first on FULLBOARD')
vt.test_game_direction_first(rules.FULLBOARD, (65536, 0))

vt.start_test('mean_score.game_direction_first on XFULLBOARD')
vt.test_game_direction_first(rules.XFULLBOARD, (64, 4))

vt.start_test('mean_score.game_direction_first on STEP0')
vt.test_game_direction_first(rules.STEP0, (512, 334))

vt.start_test('mean_score.game_direction_first torture DIR')
vt.torture_game_direction_first(vt.play_DOWN,
                                players.first_tile,
                                rules.XFULLBOARD)

vt.start_test('mean_score.game_direction_first torture TILE')
vt.torture_game_direction_first(players.first_direction,
                                vt.play_FIRST,
                                rules.XFULLBOARD)

vt.start_test('mean_score.game_direction_first torture None')
vt.torture_game_direction_first(vt.play_None,
                                players.first_tile,
                                rules.STEP0)

vt.start_test('mean_score.game_tile_first on FULLBOARD')
vt.test_game_tile_first(rules.FULLBOARD, (65536, 0))

vt.start_test('mean_score.game_tile_first on XFULLBOARD')
vt.test_game_tile_first(rules.XFULLBOARD, (32, 0))

vt.start_test('mean_score.game_tile_first on STEP0')
vt.test_game_tile_first(rules.STEP0, (512, 334))

vt.start_test('mean_score.game_tile_first on EMPTYBOARD')
vt.test_game_tile_first(rules.EMPTYBOARD, (512, 337))

myboard = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 3, 2],
    [4, 0, 5, 5],
]


vt.start_test('mean_score.game_tile_first torture DIR')
vt.torture_game_tile_first(vt.play_DOWN,
                           players.first_tile,
                           myboard)

vt.start_test('mean_score.game_tile_first torture TILE')
vt.torture_game_tile_first(players.first_direction,
                           vt.play_FIRST,
                           myboard)

vt.valid_current_stage("mean_score.games")

# ---- STAGE LEVEL -----

vt.start_test('rules.level EMPTYBOARD')
vt.test_invperm(rules.level, rules.EMPTYBOARD, 0)

vt.start_test('rules.level basic corner 0')
vt.test_invperm(rules.level, [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
], 3)

vt.start_test('rules.level basic corner 1')
vt.test_invperm(rules.level, [
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], 10)

vt.start_test('rules.level basic corner 2')
vt.test_invperm(rules.level, [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
], 10)


vt.start_test('rules.level basic corner 3')
vt.test_invperm(rules.level, [
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], 10)


vt.start_test('rules.level basic corner 4')
vt.test_invperm(rules.level, [
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
], 10)


vt.start_test('rules.level line 0')
vt.test_invperm(rules.level, [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
], 4)

vt.start_test('rules.level line 1')
vt.test_invperm(rules.level, [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], 10)

vt.start_test('rules.level line 2')
vt.test_invperm(rules.level, [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
], 11)

vt.start_test('rules.level line 3')
vt.test_invperm(rules.level, [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
], 11)

vt.start_test('rules.level line 4')
vt.test_invperm(rules.level, [
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
], 19)

vt.start_test('rules.level line 5')
vt.test_invperm(rules.level, [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
], 20)

vt.start_test('rules.level line 6')
vt.test_invperm(rules.level, [
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 2]
], 99)

vt.start_test('rules.level line 7')
vt.test_invperm(rules.level, [
    [2, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 0]
], 92)

vt.start_test('rules.level line 8')
vt.test_invperm(rules.level, [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 2, 1],
    [0, 0, 0, 0]
], 92)


vt.start_test('rules.level full 1')
vt.test_invperm(rules.level, [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
], 72)

vt.start_test('rules.level semi-full 1')
vt.test_invperm(rules.level, [
    [1, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
], 36)


vt.start_test('rules.level semi-full 2')
vt.test_invperm(rules.level, [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1]
], 8)

vt.start_test('rules.level semi-full 3')
vt.test_invperm(rules.level, [
    [2, 0, 1, 0],
    [2, 0, 1, 0],
    [0, 2, 2, 0],
    [0, 1, 1, 0]
], 902)


vt.start_test('rules.level STEP0')
vt.test_invperm(rules.level, rules.STEP0, 6642)

vt.start_test('rules.level XFULLBOARD')
vt.test_invperm(rules.level, rules.XFULLBOARD, 432619463)

vt.start_test('rules.level FINAL1')
vt.test_invperm(rules.level, rules.FINAL1, 3476604868046168890712585943456)

vt.valid_current_stage("rules.level")

# -------------------------

vt.conclude()
