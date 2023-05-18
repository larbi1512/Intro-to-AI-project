import numpy as np
from board import Board
from ai_player import AI_player
import time

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
    def __init__(self, cross_player, circle_player, size=6):
        self.cross_player = cross_player
        self.circle_player = circle_player
        self.board = Board(size)
        self.ai = AI_player(symbol["circle"])


    @property
    def cross_player(self):
        return self.__cross_player
    
    @cross_player.setter
    def cross_player(self, value):
        if(value != agent["human"] and value != agent["AI"]):
            print("wrong definition of cross player!!")
            self.__circle_player = agent["AI"]
        else:
            self.__cross_player = value

    @property
    def circle_player(self):
        return self.__circle_player
    
    @circle_player.setter
    def circle_player(self, value):
        if(value != agent["human"] and value != agent["AI"]):
            print("wrong definition of circle player!!")
            self.__circle_player = agent["AI"]
        else:
            self.__circle_player = value


    @property
    def board(self):
        return self.__board
    
    @board.setter
    def board(self, board) -> Board:
        self.__board = board
    
    def draw_game(self):
        self.board.display_board()

    def make_move_human(self):
        if  self.player_turn() == symbol["cross"]:
            if self.cross_player == agent["human"]:
                self.board.set_cell(self.board.hovered_square[0], self.board.hovered_square[1])

        if  self.player_turn() == symbol["circle"]:
            if self.circle_player == agent["human"]:
                self.board.set_cell(self.board.hovered_square[0], self.board.hovered_square[1])

    def make_move_AI(self):
        if  self.player_turn() == symbol["cross"]:
            if self.cross_player == agent["AI"]:
                self.ai.symbol = symbol["cross"]
                next_move = self.ai.next_move(self.board)
                time.sleep(0.2)
                self.board.set_cell(next_move[0], next_move[1])

        if  self.player_turn() == symbol["circle"]:
            if self.circle_player == agent["AI"]:
                self.ai.symbol = symbol["circle"]
                next_move = self.ai.next_move(self.board)
                time.sleep(0.2)
                self.board.set_cell(next_move[0], next_move[1])

    def restart(self):
        self.__board.reset_board()

    def player_turn(self):
        return self.__board.player_turn_symbol
    
    def turn_number(self):
        return self.__board.turn_number

    