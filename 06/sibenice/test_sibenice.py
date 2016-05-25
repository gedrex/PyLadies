#!/usr/bin/python3.4

import pytest
from futils import *

#is_right(char, word)
def test_is_right():
    assert is_right('a', 'sedm') == False
    assert is_right('a', 'samice') == 2
    
#change_board(position, char, board)
def test_change_board():
    assert change_board(5, 'a', '----xx-----') == '----ax-----'

