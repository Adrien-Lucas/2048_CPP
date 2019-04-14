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
        if idx in dico:
            try:
                assert dico[idx] == tstboard
            except AssertionError:
                print('ERREUR :\n{0}\nET\n{1}\nONT LA MÊME CLÉE !!!!'.format(dico[idx], tstboard))
                return
        dico[idx] = tstboard

# --------- TESTS ---------
vt.start_test('Key on random board')
Key_tst(10)
Key_tst(500)
Key_tst(int(1e5))


vt.valid_current_stage("Clées de Mémoïsation")

