#!/usr/bin/python3.4
import pytest
from piskvorky import evaluate, player_turn
from ai import tah_pocitace

game_table = '-x--o----x'
free_positions = [0,2,3,5,6,7,8] 
game_table_char = '-'
user_char = 'x'
pc_char = 'o'

def test_evaluate():
    assert evaluate('------x----', 'x', 'o', [3,5,9])== False
    assert evaluate('----xxx----', 'x', 'o', [3,5,9])=='x'
    assert evaluate('----ooo---', 'x', 'o', [3,5,9])=='o'
    assert evaluate('xoxoxoxox', 'x', 'o', [])=='!'

#player_turn(game_table, played_number, player_char, free_positions)
def test_player_turn():
    assert player_turn('-----', 2, 'x', [0,1,2,3,4])== '--x--'
    assert player_turn('-----', 1, 'o', [0,1,2,3,4]) == '-o---'

