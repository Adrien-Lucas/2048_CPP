#! /usr/bin/env python3

import rules
import validation_tools as vt
import players
import mean_score
import random

# INSERT YOUR TESTS HERE


def Key_tst(scale):
    """Test if there is 2 different boards with the same key on a specified random sample"""
    dico = {}
    for k in range(scale):
        tstboard = [[random.randint(0, 15) for i in range(rules.SIZE)] for i in range(rules.SIZE)]
        idx = players.key(tstboard)
        print
        if idx in dico:
            try:
                assert dico[idx] == tstboard
            except AssertionError:
                print('ERREUR :\n{0}\nET\n{1}\nONT LA MÊME CLÉE !!!!'.format(dico[idx], tstboard))
                return
        dico[idx] = tstboard
        
def Comp_tst(n, dir_pl):
    """Test wether or not the average score of the comp players is above the standard ones"""
    stdscore, score = 0, 0
    for i in range(n):
        score += mean_score.game_tile_first(dir_pl, players.comp_tile, rules.EMPTYBOARD)
        stdscore += mean_score.game_tile_first(dir_pl, players.random_tile, rules.EMPTYBOARD)
    stdscore /= n
    score /= n
    if stdscore < score:
        raise Exception('Player compétitif plus efficace que random Tile ({0} vs. {1})'.format(score,stdscore))
        
def Coop_tst(n):
    """Test wether or not the average score of the coop players is above the standard ones"""
    stdscore, score = 0, 0
    for i in range(n):
        score += mean_score.game_tile_first(players.coop_direction, players.coop_tile, rules.EMPTYBOARD)
        stdscore += mean_score.game_tile_first(players.random_direction, players.random_tile, rules.EMPTYBOARD)
    stdscore /= n
    score /= n
    if stdscore > score:
        raise Exception('Player coop moins efficace que random  ({0} vs. {1})'.format(score,stdscore))
        
def Coop_dir_tst(n, Tile):
    stdscore, score = 0, 0
    for i in range(n):
        score += mean_score.game_tile_first(players.coop_direction, Tile, rules.EMPTYBOARD)
        stdscore += mean_score.game_tile_first(players.random_direction, Tile, rules.EMPTYBOARD)
    stdscore /= n
    score /= n
    if stdscore < score:
        raise Exception('Player compétitif plus efficace que random Tile ({0} vs. {1})'.format(score,stdscore))

## Coop tests

def Coop_Validation():
    print('======== Stage : Coop validation ========')
    config.DEPTH = 1
    res = []
    res.append(mean_score.game_tile_first(players.coop_direction, players.coop_tile, rules.EMPTYBOARD))
    config.DEPTH = 2
    res.append(mean_score.game_tile_first(players.coop_direction, players.coop_tile, rules.EMPTYBOARD))
    
    if(res[1] > res[0]):
        print('Coop is ok, better depth is getting a better score')
    else:
        print('ERROR : Coop game with depth 2 has a lowest score than with depth 1')
        
Coop_Validation()

# --------- TESTS ---------
vt.start_test('Key on random board')
Key_tst(10)
Key_tst(500)
# Key_tst(int(1e5))

vt.valid_current_stage("Clées de Mémoïsation")

vt.start_test('Coop Players')

Coop_tst(1)
Coop_dir_tst(1, players.random_tile)

vt.valid_current_stage("Coop Players")


vt.start_test('Competitive Players')

Comp_tst(10, vt.play_DOWN)
Comp_tst(10, vt.play_FIRST)
Comp_tst(10, players.random_direction)

vt.valid_current_stage("Competitive Players")

