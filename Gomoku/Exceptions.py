#!/usr/bin/env python3

class StoneOutOfBoard(Exception):
    pass

class NoBotYet(Exception):
    pass

class StoneOnAnotherStone(Exception):
    pass

class WrongBoardSize(Exception):
    pass