import numpy as np
from board import Board
agent = {
        "human": 0,
        "AI": 1
    }

symbol = {
        "cross": 1,
        "circle": -1,
        "blank": 0,
        "max": 1,
        "min": -1
    }

DEPTH = 30


class AI_player:
    def __init__(self, agent_symbol):
        self.symbol = agent_symbol

    @property
    def symbol(self):
        return self.__symbol
    
    @symbol.setter
    def symbol(self, value):
        if value == symbol["circle"] or value == symbol["cross"]:
            self.__symbol == value

    #to know if the board is in a terminal state or not
    def terminal(self, board: Board):
        return board.is_board_full()
    
    def value(self,board: Board):
        return board.player_score(symbol["max"]) - board.player_score(symbol["min"])
    
    def playerTurn(self, board: Board):
        return board.player_turn_symbol
    
    def evaluation_function(self, board: Board):
        evaluation = board.player_situation(symbol["max"]) - board.player_situation(symbol["min"])
        if(board.turn_number > 6):
            evaluation += 2 * self.value(board)

        return evaluation
    
    def actions(self, board: Board):
        if board.is_board_full():
            return []
        
        board_possible_next_states = []
        board_copy = board

        for i in range(0, board_copy.size):
            for j in range(0, board_copy.size):
                if board_copy.set_cell(i, j):
                    board_possible_next_states.append(board_copy)
                    board_copy = board

        return board_possible_next_states
    
    def minimax(self, board: Board, depth, alpha, beta, player_symbol):
        if depth == 0 or board.is_board_full():
            return self.evaluation_function(board)
        
        if player_symbol == symbol["max"]:
            possible_next_states = self.actions(board)
            max_evaluation = -np.inf
            for child in possible_next_states:
                evaluation = self.minimax(child, depth - 1, alpha, beta, symbol["min"])
                max_evaluation = max(max_evaluation, evaluation)
                alpha = max(alpha, evaluation)

                if beta <= alpha:
                    break
                
            return max_evaluation
        
        elif player_symbol == symbol["min"]:
            if player_symbol == symbol["max"]:
                possible_next_states = self.actions(board)
                min_evaluation = np.inf
                for child in possible_next_states:
                    evaluation = self.minimax(child, depth - 1, alpha, beta, symbol["max"])
                    min_evaluation = min(min_evaluation, evaluation)
                    beta = min(beta, evaluation)

                    if beta <= alpha:
                        break

                return min_evaluation
            
    def next_move(self, board: Board):
        best_move = []
        all_possible_actions = self.actions(board)

        if  len(all_possible_actions) == 0:
            print("no more moves can be taking here")
            return best_move
        
        if self.playerTurn != board.player_turn_symbol:
            print(f"it is not {list(symbol.values()).index(self.playerTurn)} turn yet")
            print(f"it's {list(symbol.values()).index(board.player_turn_symbol)} turn")
            return best_move
        
        alpha = -np.inf
        beta = np.inf
        depth = DEPTH

        if self.symbol == symbol["max"]:
            max_evaluation = -np.inf
            for child in possible_next_states:
                evaluation = self.minimax(child, depth - 1, alpha, beta, symbol["min"])
                max_evaluation = max(max_evaluation, evaluation)
                alpha = max(alpha, evaluation)

                if beta <= alpha:
                    break
                
            return max_evaluation
        
        elif self.symbol == symbol["min"]:
            possible_next_states = self.actions(board)
            min_evaluation = np.inf
            for child in possible_next_states:
                evaluation = self.minimax(child, depth - 1, alpha, beta, symbol["max"])
                min_evaluation = min(min_evaluation, evaluation)
                beta = min(beta, evaluation)

                if beta <= alpha:
                    break

            return min_evaluation
        


        


