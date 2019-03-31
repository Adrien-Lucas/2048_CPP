#! /usr/bin/env python3

import rules
import validation_tools as vt
import players
import mean_score

# INSERT YOUR TESTS HERE

# r = mean_score.game_direction_first(vt.play_None, players.first_tile, rules.STEP0)
# print(r)

r = players.first_tile(rules.EMPTYBOARD)
q = mean_score.game_tile_first(players.first_direction, players.first_tile, rules.EMPTYBOARD)
print(q)
print(r)
# print(rules.move_dir(0, [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [3, 2, 2, 2]]))



