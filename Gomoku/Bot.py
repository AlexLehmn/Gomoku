#!/usr/bin/env python3

import Exceptions
import re

threats = [
    [0,2,0,2,2,0],
    [1,0,2,2,2,0,0]
]

class Bot:
    def __init__(self, size, info):
        try:
            self.info = info
            self.size = int(size)
            if (self.size < 0):
                raise Exceptions.WrongBoardSize
            self.generateBoard()
            print('OK')
        except ValueError:
            print('ERROR "The size of the board is not correctly formated."')
        except Exceptions.WrongBoardSize:
            print('ERROR "The size of the board must be at least equal or above 5."')
    def getSize(self):
        return self.size
    def setInfo(self, info):
        self.info = info
    def generateBoard(self):
        self.board = [[0] * self.size for i in range(self.size)]
    def generateBoardFrom(self):
        self.generateBoard()
        running = True
        while running == True:
            managerInput = input()
            if managerInput == "DONE":
                running = False
            else:
                splitInput = managerInput.split(",")
                try:
                    x = int(splitInput[0])
                    y = int(splitInput[1])
                    if (x >= self.size or y >= self.size):
                        raise Exceptions.StoneOutOfBoard
                    player = int(splitInput[2])
                    if self.board[x][y] != 0:
                        raise Exceptions.StoneOnAnotherStone
                    self.board[x][y] = player
                except ValueError:
                    print('ERROR "BOARD line is not formatted correctly."')
                except Exceptions.StoneOutOfBoard:
                    print('ERROR "This stone is out of the board."')
                except Exceptions.StoneOnAnotherStone:
                    print('ERROR "There is already a stone at ',x,',',y,' coordinates."')
        self.doTurn()
    def searchThreatThree(self):
        threatThree = [0,2,2,2,0]
        defenses = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x, y + 4))
                #search from top to bottom
                if len(self.board) - x >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x + i][y] != threatThree[i] :
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 4, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatThree) and len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x + i][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 4, y + 4))
                #search diagonal down left
                if x >= len(threatThree) - 1 and len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x - i][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x - 4, y + 4))
                y += 1
            x += 1
        return defenses
    def searchWinThree(self):
        threatThree = [0,1,1,1,0]
        attacks = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x, y + 4))
                #search from top to bottom
                if len(self.board) - x >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x + i][y] != threatThree[i] :
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x + 4, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatThree) and len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x + i][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x + 4, y + 4))
                #search diagonal down left
                if x >= len(threatThree) - 1 and len(self.board) - y >= len(threatThree):
                    i = 0
                    threat = True
                    while i < len(threatThree):
                        if self.board[x - i][y + i] != threatThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x - 4, y + 4))
                y += 1
            x += 1
        return attacks
    def searchThreatFour(self):
        threatFour = [1,2,2,2,2,0]
        defenses = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                #search from top to bottom
                if len(self.board) - x >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x + i][y] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x + 5, y))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatFour) and len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x + i][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x + 5, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                #search diagonal down left
                if x >= len(threatFour) - 1 and len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x - i][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x - 5, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x - u][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                y += 1
            x += 1
        return defenses
    def searchWinFour(self):
        threatFour = [2,1,1,1,1,0]
        attacks = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x, y))
                #search from top to bottom
                if len(self.board) - x >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x + i][y] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x + 5, y))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatFour) and len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x + i][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x + 5, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x, y))
                #search diagonal down left
                if x >= len(threatFour) - 1 and len(self.board) - y >= len(threatFour):
                    i = 0
                    threat = True
                    while i < len(threatFour):
                        if self.board[x - i][y + i] != threatFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x - 5, y + 5))
                    i = len(threatFour) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x - u][y + u] != threatFour[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x, y))
                y += 1
            x += 1
        return attacks
    def searchThreatFourWall(self):
        threatFourWall = [2,2,2,2,0]
        defenses = []
        x = 0
        while x < self.size:
            y = 0
            threat = True
            while y < len(threatFourWall):
                if self.board[x][y] != threatFourWall[y]:
                    threat = False
                y += 1
            if threat == True:
                defenses.append((x, 4))
            x += 1
        x = 0
        while x < self.size:
            y = self.size - 1
            threat = True
            i = 0
            while i < len(threatFourWall):
                if self.board[x][y] != threatFourWall[i]:
                    threat = False
                i += 1
                y -= 1
            if threat == True:
                defenses.append((x, self.size - 5))
            x += 1
        y = 0
        while y < self.size:
            x = 0
            threat = True
            while x < len(threatFourWall):
                if self.board[x][y] != threatFourWall[x]:
                    threat = False
                x += 1
            if threat == True:
                defenses.append((4, y))
            y += 1
        y = 0
        while y < self.size:
            x = self.size - 1
            threat = True
            i = 0
            while i < len(threatFourWall):
                if self.board[x][y] != threatFourWall[i]:
                    threat = False
                i += 1
                x -= 1
            if threat == True:
                defenses.append((self.size - 5, y))
            y += 1
        return defenses
    def searchWinFourWall(self):
        threatFourWall = [1,1,1,1,0]
        attacks = []
        x = 0
        while x < self.size:
            y = 0
            threat = True
            while y < len(threatFourWall):
                if self.board[x][y] != threatFourWall[y]:
                    threat = False
                y += 1
            if threat == True:
                attacks.append((x, 4))
            x += 1
        x = 0
        while x < self.size:
            y = self.size - 1
            threat = True
            i = 0
            while i < len(threatFourWall):
                if self.board[x][y] != threatFourWall[i]:
                    threat = False
                i += 1
                y -= 1
            if threat == True:
                attacks.append((x, self.size - 5))
            x += 1
        y = 0
        while y < self.size:
            x = 0
            threat = True
            while x < len(threatFourWall):
                if self.board[x][y] != threatFourWall[x]:
                    threat = False
                x += 1
            if threat == True:
                attacks.append((4, y))
            y += 1
        y = 0
        while y < self.size:
            x = self.size - 1
            threat = True
            i = 0
            while i < len(threatFourWall):
                if self.board[x][y] != threatFourWall[i]:
                    threat = False
                i += 1
                x -= 1
            if threat == True:
                attacks.append((self.size - 5, y))
            y += 1
        return attacks
    def searchThreatStraightFour(self):
        threatStraightFour = [0,2,2,2,2,0]
        defenses = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x, y + 4))
                #search from top to bottom
                if len(self.board) - x >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x + i][y] != threatStraightFour[i] :
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 4, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatStraightFour) and len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x + i][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 4, y + 4))
                #search diagonal down left
                if x >= len(threatStraightFour) - 1 and len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x - i][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x - 4, y + 4))
                y += 1
            x += 1
        return defenses
    def searchWinStraightFour(self):
        threatStraightFour = [0,1,1,1,1,0]
        attacks = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x, y + 4))
                #search from top to bottom
                if len(self.board) - x >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x + i][y] != threatStraightFour[i] :
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x + 4, y))
                #search diagonal down right
                if len(self.board) - x >= len(threatStraightFour) and len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x + i][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x + 4, y + 4))
                #search diagonal down left
                if x >= len(threatStraightFour) - 1 and len(self.board) - y >= len(threatStraightFour):
                    i = 0
                    threat = True
                    while i < len(threatStraightFour):
                        if self.board[x - i][y + i] != threatStraightFour[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y))
                        attacks.append((x - 4, y + 4))
                y += 1
            x += 1
        return attacks
    def searchThreatBrokenThree(self):
        brokenThree = [0,2,0,2,2,0]
        defenses = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x, y + 2))
                        defenses.append((x, y + 5))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x, y + 3))
                        defenses.append((x, y + 5))
                #search from top to bottom
                if len(self.board) - x >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x + i][y] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 2, y))
                        defenses.append((x + 5, y))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 3, y))
                        defenses.append((x + 5, y))
                #search diagonal down right
                if len(self.board) - x >= len(brokenThree) and len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x + i][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 2, y + 2))
                        defenses.append((x + 5, y + 5))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x, y))
                        defenses.append((x + 3, y + 3))
                        defenses.append((x + 5, y + 5))
                #search diagonal down left
                if x >= len(brokenThree) - 1 and len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x - i][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        defenses.append((x - 5, y + 5))
                        defenses.append((x - 2, y + 2))
                        defenses.append((x, y))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x - u][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        defenses.append((x - 5, y + 5))
                        defenses.append((x - 3, y + 3))
                        defenses.append((x, y))
                y += 1
            x += 1
        return defenses
    def searchWinBrokenThree(self):
        brokenThree = [0,1,0,1,1,0]
        attacks = []
        x = 0
        while x < len(self.board):
            y = 0
            while y < len(self.board[x]):
                #search from left to right
                if len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x, y + 2))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x, y + 3))
                #search from top to bottom
                if len(self.board) - x >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x + i][y] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x + 2, y))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x + 3, y))
                #search diagonal down right
                if len(self.board) - x >= len(brokenThree) and len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x + i][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x + 2, y + 2))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x + u][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x + 3, y + 3))
                #search diagonal down left
                if x >= len(brokenThree) - 1 and len(self.board) - y >= len(brokenThree):
                    i = 0
                    threat = True
                    while i < len(brokenThree):
                        if self.board[x - i][y + i] != brokenThree[i]:
                            threat = False
                        i += 1
                    if threat == True:
                        attacks.append((x - 2, y + 2))
                    i = len(brokenThree) - 1
                    u = 0
                    threat = True
                    while i > -1:
                        if self.board[x - u][y + u] != brokenThree[i]:
                            threat = False
                        u += 1
                        i -= 1
                    if threat == True:
                        attacks.append((x - 3, y + 3))
                y += 1
            x += 1
        return attacks
    def attackSelection(self):
        attacks = []
        for attack in self.searchWinThree():
            attacks.append((attack, 1))
        for attack in self.searchWinFour():
            exist = False
            i = 0
            while i < len(attacks) and exist == False:
                if attacks[i][0][0] == attack[0] and attacks[i][0][1] == attack[1]:
                    attacks[i] = (attacks[i][0], attacks[i][1] + 3)
                    exist = True
                i += 1
            if exist == False:
                attacks.append((attack, 3))
        for attack in self.searchWinFourWall():
            exist = False
            i = 0
            while i < len(attacks) and exist == False:
                if attacks[i][0][0] == attack[0] and attacks[i][0][1] == attack[1]:
                    attacks[i] = (attacks[i][0], attacks[i][1] + 3)
                    exist = True
                i += 1
            if exist == False:
                attacks.append((attack, 3))
        for attack in self.searchWinStraightFour():
            exist = False
            i = 0
            while i < len(attacks) and exist == False:
                if attacks[i][0][0] == attack[0] and attacks[i][0][1] == attack[1]:
                    attacks[i] = (attacks[i][0], attacks[i][1] + 3)
                    exist = True
                i += 1
            if exist == False:
                attacks.append((attack, 3))
        for attack in self.searchWinBrokenThree():
            exist = False
            i = 0
            while i < len(attacks) and exist == False:
                if attacks[i][0][0] == attack[0] and attacks[i][0][1] == attack[1]:
                    attacks[i] = (attacks[i][0], attacks[i][1] + 2)
                    exist = True
                i += 1
            if exist == False:
                attacks.append((attack, 2))
        if len(attacks) > 1:
            highest = 0
            for d in attacks:
                if d[1] > highest:
                    highest = d[1]
            attacks2 = []
            for d in attacks:
                if d[1] == highest:
                    attacks2.append(d)
            if len(attacks2) > 1:
                i = 0
                while i < len(attacks2):
                    if self.board[attacks[i][0][0] + 1][attacks[i][0][1]] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0]][attacks[i][0][1] + 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0] - 1][attacks[i][0][1]] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0]][attacks[i][0][1] - 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0] + 1][attacks[i][0][1] + 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0] + 1][attacks[i][0][1] - 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0] - 1][attacks[i][0][1] + 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    if self.board[attacks[i][0][0] - 1][attacks[i][0][1] - 1] != 0:
                        attacks[i] = (attacks[i][0], attacks[i][1] + 1)
                    highest = 0
                    for d in attacks2:
                        if d[1] > highest:
                            highest = d[1]
                    attacks3 = []
                    for d in attacks2:
                        if d[1] == highest:
                            attacks3.append(d)
                    return attacks3
            else:
                return attacks2
        else:
            return attacks
    def defenseSelection(self):
        defenses = []
        for defense in self.searchThreatThree():
            defenses.append((defense, 2))
        for defense in self.searchThreatFour():
            exist = False
            i = 0
            while i < len(defenses) and exist == False:
                if defenses[i][0][0] == defense[0] and defenses[i][0][1] == defense[1]:
                    defenses[i] = (defenses[i][0], defenses[i][1] + 2)
                    exist = True
                i += 1
            if exist == False:
                defenses.append((defense, 2))
        for defense in self.searchThreatFourWall():
            exist = False
            i = 0
            while i < len(defenses) and exist == False:
                if defenses[i][0][0] == defense[0] and defenses[i][0][1] == defense[1]:
                    defenses[i] = (defenses[i][0], defenses[i][1] + 2)
                    exist = True
                i += 1
            if exist == False:
                defenses.append((defense, 2))
        for defense in self.searchThreatStraightFour():
            exist = False
            i = 0
            while i < len(defenses) and exist == False:
                if defenses[i][0][0] == defense[0] and defenses[i][0][1] == defense[1]:
                    defenses[i] = (defenses[i][0], defenses[i][1] + 100)
                    exist = True
                i += 1
            if exist == False:
                defenses.append((defense, 2))
        for defense in self.searchThreatBrokenThree():
            exist = False
            i = 0
            while i < len(defenses) and exist == False:
                if defenses[i][0][0] == defense[0] and defenses[i][0][1] == defense[1]:
                    defenses[i] = (defenses[i][0], defenses[i][1] + 2)
                    exist = True
                i += 1
            if exist == False:
                defenses.append((defense, 2))
        if len(defenses) > 1:
            highest = 0
            for d in defenses:
                if d[1] > highest:
                    highest = d[1]
            defenses2 = []
            for d in defenses:
                if d[1] == highest:
                    defenses2.append(d)
            if len(defenses2) > 1:
                i = 0
                while i < len(defenses2):
                    if self.board[defenses[i][0][0] + 1][defenses[i][0][1]] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0]][defenses[i][0][1] + 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0] - 1][defenses[i][0][1]] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0]][defenses[i][0][1] - 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0] + 1][defenses[i][0][1] + 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0] + 1][defenses[i][0][1] - 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0] - 1][defenses[i][0][1] + 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    if self.board[defenses[i][0][0] - 1][defenses[i][0][1] - 1] != 0:
                        defenses[i] = (defenses[i][0], defenses[i][1] + 1)
                    highest = 0
                    for d in defenses2:
                        if d[1] > highest:
                            highest = d[1]
                    defenses3 = []
                    for d in defenses2:
                        if d[1] == highest:
                            defenses3.append(d)
                    return defenses3
            else:
                return defenses2
        else:
            return defenses
    def doTurn(self):
        attacks = self.attackSelection()
        #print(attacks)
        if len(attacks) == 0:
            defenses = self.defenseSelection()
            #print(defenses)
            running = True
            if len(defenses) == 0:
                x = 0
                while x < len(self.board) and running == True:
                    y = 0
                    while y < len(self.board[x]) and running == True:
                        if self.board[x][y] == 0:
                            print(x,",",y, sep="")
                            self.board[x][y] = 1
                            running = False
                        y += 1
                    x += 1
            else:
                print(defenses[0][0][0],",",defenses[0][0][1], sep="")
                self.board[defenses[0][0][0]][defenses[0][0][1]] = 1
        else:
            print(attacks[0][0][0],",",attacks[0][0][1],sep="")
            self.board[attacks[0][0][0]][attacks[0][0][1]] = 1
    def TURN(self, previousTurn):
        try:
            regex = re.compile(r'^([0-9]+),([0-9]+)$')
            splitPreviousTurn = regex.search(previousTurn)
            if not splitPreviousTurn:
                raise Exceptions.WrongTurnCommandFormat
            X_pos_str, Y_pos_str = splitPreviousTurn.groups()
            X_pos = int(X_pos_str)
            Y_pos = int(Y_pos_str)
            if X_pos < 0 or X_pos >= self.size:
                raise Exceptions.WrongTurnCommandXPos
            if Y_pos < 0 or Y_pos >= self.size:
                raise Exceptions.WrongTurnCommandYPos
            self.board[X_pos][Y_pos] = 2
        except Exceptions.WrongTurnCommandFormat:
            print('ERROR "TURN command arguments are not formatted correctly."')
        except Exceptions.WrongTurnCommandXPos:
            print('ERROR "The stone X position must be between 1 and the maximum size of the board."')
        except Exceptions.WrongTurnCommandYPos:
            print('ERROR "The stone Y position must be between 1 and the maximum size of the board."')
        self.doTurn()
