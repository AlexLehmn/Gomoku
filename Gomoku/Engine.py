#!/usr/bin/env python3

from Bot import Bot
from Exceptions import NoBotYet

class Engine:
    def __init__(self):
        self.running = True
        self.setDefaultInfo()
        while (self.running):
            self.manageInput()
    def manageInput(self):
        managerInput = input()
        splitInput = managerInput.split()
        match splitInput[0]:
            case 'END':
                self.running = False
            case 'ABOUT':
                self.about()
            case 'INFO':
                if len(splitInput) == 3:
                    self.setInfo(splitInput)
                else:
                    print('ERROR "Incorrect number of arguments."')
            case 'START':
                if len(splitInput) == 2:
                    self.bot = Bot(splitInput[1], self.info)
                else:
                    print('ERROR "Incorrect number of arguments."')
            case 'RESTART':
                self.setDefaultInfo()
                self.bot = Bot(self.bot.getSize(), self.info)
            case 'BOARD':
                if len(splitInput) > 1:
                    print('ERROR "BOARD command should not have arguments."')
                else:
                    try:
                        if not hasattr(self, 'bot'):
                            raise NoBotYet
                        self.bot.generateBoardFrom()
                    except NoBotYet:
                        print('ERROR "Use START command to initialize the bot first."')
            case 'TURN':
                if len(splitInput) == 2:
                    try:
                        if not hasattr(self, 'bot'):
                            raise NoBotYet
                        self.bot.TURN(splitInput[1])
                    except NoBotYet:
                        print('ERROR "Use START command to initialize the bot first."')
                else:
                    print('ERROR "TURN command should have only one argument."')
            case 'BEGIN':
                if len(splitInput) == 1:
                    try:
                        if not hasattr(self, 'bot'):
                            raise NoBotYet
                        self.bot.doTurn()
                    except NoBotYet:
                        print('ERROR "Use START command to initialize the bot first."')
            case _:
                print('UNKNOWN "This command is not known by the bot."')
    def about(self):
        print('name="pbrain-gomoku-ai", version="1.0", author="L.V. Allis", country="The Netherlands"')
    def setDefaultInfo(self):
        self.info = {
            "timeout_turn": 0,
            "timeout_match": 0,
            "max_memory": 0,
            "time_left": 0,
            "game_type": 0,
            "rule": 0,
            "evaluate": [0, 0],
            "folder": ""
        }
    def setInfo(self, inputs):
        match inputs[1]:
            case 'timeout_turn':
                try:
                    self.info.update(timeout_turn = int(inputs[2]))
                except ValueError:
                    print('ERROR "Bad value"')
            case 'timeout_match':
                try:
                    self.info.update(timeout_match = int(inputs[2]))
                except ValueError:
                    print('ERROR "Bad value"')
            case 'max_memory':
                try:
                    value = int(inputs[2])
                except ValueError:
                    print('ERROR "Bad value"')
            case 'time_left':
                try:
                    self.info.update(time_left = int(inputs[2]))
                except ValueError:
                    print('ERROR "Bad value"')
            case 'game_type':
                try:
                    self.info.update(game_type = int(inputs[2]))
                except ValueError:
                    print('ERROR "Bad value"')
            case 'rule':
                try:
                    self.info.update(rule = int(inputs[2]))
                except ValueError:
                    print('ERROR "Bad value"')
            case 'evaluate':
                try:
                    splitValues = inputs[2].split(",")
                    self.info.update(evaluate = [int(splitValues[0]), int(splitValues[1])])
                except ValueError:
                    print('ERROR "Bad value"')
            case 'folder':
                self.info.update(folder = inputs[2])
            case _:
                print('ERROR "This info does not exist"')
        self.bot.setInfo(self.info)
