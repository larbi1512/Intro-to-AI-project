import numpy as np
from board import Board
from ai_player import AI_player

symbol = {
        "cross": 1,
        "circle": -1,
        "blank": 0
    }

agent = {
        "human": 0,
        "AI": 1
    }


class Game:
    def __init__(self, cross_player, circle_player, size):
        self.cross_player = cross_player
        self.circle_player = circle_player
        self.board = Board(size)
        self.ai = AI_player(symbol["circle"])


    @property
    def cross_player(self):
        return self.__cross_player
    
    @cross_player.setter
    def cross_player(self, value):
        if(value != agent["human"] or value != agent["AI"]):
            print("wrong definition of player 1!!")
            self.__circle_player = agent["AI"]
        else:
            self.__cross_player = value

    @property
    def circle_player(self):
        return self.__circle_player
    
    @circle_player.setter
    def circle_player(self, value):
        if(value != agent["human"] or value != agent["AI"]):
            print("wrong definition of player 1!!")
            self.__circle_player = agent["AI"]
        else:
            self.__circle_player = value


    @property
    def board(self):
        return self.board
    
    def draw_game(self):
        self.board.display_board()

    def make_move(self):
        pass

    