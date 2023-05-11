import numpy as np


# The functions of the class Board:
# player_turn_symbol(): to return the symbol that his turn has come
# turn_number(): to return the turn number in the board
# player_score(self, player_symbol): a function that get the 
# 
# 
# 
# 
# 
# 
# 



symbol = {
        "cross": 1,
        "circle": -1,
        "blank": 0
    }

agent = {
        "human": 0,
        "AI": 1
    }
class Board:
    def __init__(self, size = 6):
        if(size < 4 or size > 12):
            self.size = 6
        self.__matrix = np.zeros((self.size, self.size))
        self.__player_turn_symbol = symbol["cross"]
        self.__turn_number = 1

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if(value < 4 or value > 12):
            print("invalid board size")
        else:
            self.__size = value
            self.__matrix = np.zeros((self.size, self.size))

    

    @property
    def matrix(self):
        return self.__matrix
    
    def set_cell(self, row, col):
        if self.__matrix[row][col] == symbol["blank"]:
            self.__matrix[row][col] = self.__player_turn_symbol
            self.player_turn_symbol(1)
            self.__turn_number += 1
            return True
        
        return False
    
    @property
    def player_turn_symbol(self):
         return self.__player_turn_symbol
    
    @player_turn_symbol.setter
    def player_turn_symbol(self, n):
         if self.__player_turn_symbol == symbol["cross"]:
              self.__player_turn_symbol = symbol["circle"]

         if self.__player_turn_symbol == symbol["circle"]:
              self.__player_turn_symbol = symbol["cross"]

    @property
    def turn_number(self):
         return self.__turn_number

    def player_score(self, player_symbol):
        if not(player_symbol in symbol):
            print("invalid symbol number")
            return -1
        
        counter = 0
        # check right
        i = 0
        while i < self.size:
            j = 0
            while j < self.size - 3:
                if(self.__matrix[i][j] == player_symbol and self.__matrix[i][j+1] == player_symbol and self.__matrix[i][j+2]
                   == player_symbol and self.__matrix[i][j+3] == player_symbol):
                    counter += 1
                    j += 4
                    while j < self.size and self.__matrix[i][j] == player_symbol:
                        counter += 1
                        j += 1
                else:
                    j += 1

            i += 1

        # check down
        j = 0
        while j < self.size:
            i = 0
            while i < self.size - 3:
                if(self.__matrix[i][j] == player_symbol and self.__matrix[i+1][j] == player_symbol and self.__matrix[i+2][j]
                    == player_symbol and self.__matrix[i+3][j] == player_symbol):
                    counter += 1
                    i += 4
                    while i < self.size and self.__matrix[i][j] == player_symbol:
                        counter += 1
                        i += 1
                else:
                    i += 1

            j += 1

        def next_diago_line(i, j):
            if(i > 0):
                i -= 1
                return [i, j]
            
            if(i == 0):
                j += 1
                return [i, j]
            
        # check right-down
        i = self.size - 4
        j = 0
        while(j < self.size - 3):
            while (i < self.size - 3 and i >= j) or (j < self.size - 3 and j >= i):
                if(self.__matrix[i][j] == player_symbol and self.__matrix[i+1][j+1] == player_symbol and self.__matrix[i+2][j+2]
                        == player_symbol and self.__matrix[i+3][j+3] == player_symbol):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < self.size and j < self.size) and self.__matrix[i][j] == player_symbol:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - 3 or i >= self.size - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]

        # check left-up
        mirror_arr = np.zeros((self.size, self.size))
        for i in range(0, self.size):
             for j in range(0, self.size):
                  if i + j == self.size - 1:
                       mirror_arr[i][j] = 1

        self.__matrix = np.dot(self.__matrix, mirror_arr)

        i = self.size - 4
        j = 0
        while(j < self.size - 3):
            while (i < self.size - 3 and i >= j) or (j < self.size - 3 and j >= i):
                if(self.__matrix[i][j] == player_symbol and self.__matrix[i+1][j+1] == player_symbol and self.__matrix[i+2][j+2]
                        == player_symbol and self.__matrix[i+3][j+3] == player_symbol):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < self.size and j < self.size) and self.__matrix[i][j] == player_symbol:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - 3 or i >= self.size - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]

        self.__matrix = np.dot(self.__matrix, mirror_arr)
        return counter
    
    def player_situation(self, player_symbol):
        if not(player_symbol in symbol):
            print("invalid symbol number")
            return -1
        
        counter = 0
        good_symbols = [player_symbol, symbol["blank"]]
        # check right
        i = 0
        while i < self.size:
            j = 0
            while j < self.size - 3:
                if(self.__matrix[i][j] in good_symbols and self.__matrix[i][j+1] in good_symbols and self.__matrix[i][j+2]
                   in good_symbols and self.__matrix[i][j+3] in good_symbols):
                    counter += 1
                    j += 4
                    while j < self.size and self.__matrix[i][j] in good_symbols:
                        counter += 1
                        j += 1
                else:
                    j += 1

            i += 1

        # check down
        j = 0
        while j < self.size:
            i = 0
            while i < self.size - 3:
                if(self.__matrix[i][j] in good_symbols and self.__matrix[i+1][j] in good_symbols and self.__matrix[i+2][j]
                    in good_symbols and self.__matrix[i+3][j] in good_symbols):
                    counter += 1
                    i += 4
                    while i < self.size and self.__matrix[i][j] in good_symbols:
                        counter += 1
                        i += 1
                else:
                    i += 1

            j += 1

        def next_diago_line(i, j):
            if(i > 0):
                i -= 1
                return [i, j]
            
            if(i == 0):
                j += 1
                return [i, j]
            
        # check right-down
        i = self.size - 4
        j = 0
        while(j < self.size - 3):
            while (i < self.size - 3 and i >= j) or (j < self.size - 3 and j >= i):
                if(self.__matrix[i][j] in good_symbols and self.__matrix[i+1][j+1] in good_symbols and self.__matrix[i+2][j+2]
                        in good_symbols and self.__matrix[i+3][j+3] in good_symbols):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < self.size and j < self.size) and self.__matrix[i][j] in good_symbols:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - 3 or i >= self.size - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]

        # check left-up
        mirror_arr = np.zeros((self.size, self.size))
        for i in range(0, self.size):
             for j in range(0, self.size):
                  if i + j == self.size - 1:
                       mirror_arr[i][j] = 1

        self.__matrix = np.dot(self.__matrix, mirror_arr)

        i = self.size - 4
        j = 0
        while(j < self.size - 3):
            while (i < self.size - 3 and i >= j) or (j < self.size - 3 and j >= i):
                if(self.__matrix[i][j] in good_symbols and self.__matrix[i+1][j+1] in good_symbols and self.__matrix[i+2][j+2]
                        in good_symbols and self.__matrix[i+3][j+3] in good_symbols):
                        counter += 1
                        i += 4
                        j += 4
                        while (i < self.size and j < self.size) and self.__matrix[i][j] in good_symbols:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - 3 or i >= self.size - 3):
                             if i == j:
                                  j = 0; i = 0
                             elif i > j:
                                  i -= j
                                  j = 0
                             elif j > i:
                                  j -= i
                                  i = 0
                             l = next_diago_line(i, j)
                             i = l[0]; j = l[1]

            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            l = next_diago_line(i, j)
            i = l[0]; j = l[1]

        self.__matrix = np.dot(self.__matrix, mirror_arr)
        return counter
    
    def is_board_full(self):
         for row in self.__matrix:
              for cell in row:
                   if cell != symbol["blank"]:
                        return False
                   
         return True
    
    def reset_board(self, size = 0):
         if(size):
              size = self.size
         self.size = size
         self.__player_turn_symbol = symbol["cross"]
         self.__turn_number = 1

    def display_board(self):
         pass
    

    