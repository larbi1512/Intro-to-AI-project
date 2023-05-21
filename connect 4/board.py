import pygame
import numpy as np
from constaints import *


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

def p(s):
    if(s == -1):
        return 1
    if(s == 1):
        return 0
class Board:
    def __init__(self, size = 6):
        self.size = size
        if(size < 4 or size > 12):
            self.size = 6
        self.__matrix = np.zeros((self.size, self.size))
        self.__player_turn_symbol = symbol["cross"]
        self.hovered_square = (-1, -1)
        self.__turn_number = 1

        self.SQUARE_SIZE = BOARD_SIZE / self.size - LINE_WIDTH
        self.CIRCLE_RADIUS = (self.SQUARE_SIZE / 2) - SQUARE_PADDING

        self.cross_player_score = self.circle_player_score = 0

        self.mirror_arr = np.zeros((self.size, self.size))
        for i in range(0, self.size):
             for j in range(0, self.size):
                  if i + j == self.size - 1:
                       self.mirror_arr[i][j] = 1

        self.lines_list = []
        lines_number = self.size * 2 + (self.size * 2 - 1) * 2
        for i in range(lines_number):
             self.lines_list.append([0, 0])
                  

    @property
    def cross_player_score(self):
        return self.__cross_player_score
    
    @cross_player_score.setter
    def cross_player_score(self, value):
        self.__cross_player_score = value
    
    @property
    def circle_player_score(self):
        return self.__circle_player_score
    
    @circle_player_score.setter
    def circle_player_score(self, value):
        self.__circle_player_score = value
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
            self.mirror_arr = np.zeros((self.size, self.size))
            for i in range(0, self.size):
                 for j in range(0, self.size):
                     if i + j == self.size - 1:
                         self.mirror_arr[i][j] = 1

    

    @property
    def matrix(self):
        return self.__matrix
    
    def set_cell(self, row, col):
        if row >= self.size or col >= self.size or row < 0 or col < 0:
             return False
        
        if self.__matrix[row][col] == symbol["blank"]:
            self.__matrix[row][col] = self.__player_turn_symbol

            self.lines_list[row][p(self.player_turn_symbol)] += 1
            self.lines_list[self.size + col][p(self.player_turn_symbol)] += 1

            i = row; j = col
            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            self.lines_list[self.size * 2 + self.size - i - 1 + j][p(self.player_turn_symbol)] += 1

            i = row; j = self.size - col - 1
            if i == j:
                j = 0; i = 0
            elif i > j:
                i -= j
                j = 0
            elif j > i:
                j -= i
                i = 0

            self.lines_list[self.size * 2 + self.size * 2 - 1 + self.size - i - 1 + j][p(self.player_turn_symbol)] += 1


            self.player_turn_symbol = 1
            self.__turn_number += 1
            self.circle_player_score = self.player_score(symbol["circle"])
            self.cross_player_score = self.player_score(symbol["cross"])
            return True
        
        return False
    
    @property
    def player_turn_symbol(self):
         return self.__player_turn_symbol
    
    @player_turn_symbol.setter
    def player_turn_symbol(self, n):
         if self.__player_turn_symbol == symbol["cross"]:
              self.__player_turn_symbol = symbol["circle"]
              return

         if self.__player_turn_symbol == symbol["circle"]:
              self.__player_turn_symbol = symbol["cross"]

    @property
    def turn_number(self):
         return self.__turn_number
    
    @property
    def hovered_square(self):
         return self.__hovered_square
    
    @hovered_square.setter
    def hovered_square(self, position):
         self.__hovered_square = position

    def player_score(self, player_symbol, line_width=4):
        if player_symbol not in list(symbol.values()):
            print("invalid symbol number")
            return -1
        
        counter = 0
        # check right
        i = 0
        while i < self.size:
            if self.lines_list[i][p(player_symbol)] < line_width:
                 i += 1
                 continue
            j = 0
            while j < self.size - (line_width - 1):
                if all(self.__matrix[i][j+k] == player_symbol for k in range(line_width)):
                    counter += 1
                    j += line_width
                    while j < self.size and self.__matrix[i][j] == player_symbol:
                        counter += 1
                        j += 1
                else:
                    j += 1

            i += 1

        # check down
        j = 0
        while j < self.size:
            if self.lines_list[j + self.size][p(player_symbol)] < line_width:
                 j += 1
                 continue
            i = 0
            while i < self.size - (line_width - 1):
                if all(self.__matrix[i+k][j] == player_symbol for k in range(line_width)):
                    counter += 1
                    i += line_width
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
        lines_counter = self.size * 2 + line_width - 1
        i = self.size - line_width
        j = 0
        while(j < self.size - (line_width - 1)):
            if self.lines_list[lines_counter][p(player_symbol)] < line_width:
                 lines_counter += 1
                 l = next_diago_line(i, j)
                 i = l[0]; j = l[1]
                 continue
            lines_counter += 1
            while (i < self.size - (line_width - 1) and i >= j) or (j < self.size - (line_width - 1) and j >= i):
                if all(self.__matrix[i+k][j+k] == player_symbol for k in range(line_width)):
                        counter += 1
                        i += line_width
                        j += line_width
                        while (i < self.size and j < self.size) and self.__matrix[i][j] == player_symbol:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - (line_width - 1) or i >= self.size - (line_width - 1)):
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
        

        self.__matrix = np.dot(self.__matrix, self.mirror_arr)

        lines_counter = self.size * 2 + self.size * 2 - 1 + line_width - 1
        i = self.size - line_width
        j = 0
        while(j < self.size - (line_width - 1)):
            if self.lines_list[lines_counter][p(player_symbol)] < line_width:
                 lines_counter += 1
                 l = next_diago_line(i, j)
                 i = l[0]; j = l[1]
                 continue
            
            lines_counter += 1
            while (i < self.size - (line_width - 1) and i >= j) or (j < self.size - (line_width - 1) and j >= i):
                if  all(self.__matrix[i+k][j+k] == player_symbol for k in range(line_width)):
                        counter += 1
                        i += line_width
                        j += line_width
                        while (i < self.size and j < self.size) and self.__matrix[i][j] == player_symbol:
                            counter += 1
                            i += 1
                            j += 1
                else:
                        i += 1
                        j += 1
                        if(j >= self.size - (line_width - 1) or i >= self.size - (line_width - 1)):
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

        self.__matrix = np.dot(self.__matrix, self.mirror_arr)

        return counter
    
    def player_situation(self, player_symbol):
        if player_symbol not in list(symbol.values()):
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
        self.__matrix = np.dot(self.__matrix, self.mirror_arr)

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

        self.__matrix = np.dot(self.__matrix, self.mirror_arr)
        return counter
    
    def is_board_full(self):
         for row in self.__matrix:
              for cell in row:
                   if cell == symbol["blank"]:
                        return False
                   
         return True
    
    def reset_board(self, size = 0):
         self.__init__(self.size)

    def draw_board(self, win):
         (mouse_x, mouse_y) = pygame.mouse.get_pos()
         self.hovered_square = (-1, -1)
         for row in range(self.size):
              for col in range(self.size):
                   if(mouse_x <= WINDOW_PADDING + LINE_WIDTH * row + row * self.SQUARE_SIZE + self.SQUARE_SIZE and 
                      mouse_x >= WINDOW_PADDING + LINE_WIDTH * row + row * self.SQUARE_SIZE and 
                      mouse_y <= WINDOW_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE + self.SQUARE_SIZE and 
                      mouse_y >= WINDOW_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE and 
                      self.matrix[row][col] == symbol["blank"]):
                        pygame.draw.rect(win, YELLOW, (WINDOW_PADDING + LINE_WIDTH * row + row * self.SQUARE_SIZE, WINDOW_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                        self.hovered_square =  (row, col)
                   else:
                        pygame.draw.rect(win, GRAY, (WINDOW_PADDING + LINE_WIDTH * row + row * self.SQUARE_SIZE, WINDOW_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

         self.draw_figures(win)

         self.display_score(win)
    
    def draw_cross(self, win, row, col):

         pygame.draw.line(win, RED, (WINDOW_PADDING + SQUARE_PADDING + CROSS_WIDTH/10 + LINE_WIDTH * row + row * self.SQUARE_SIZE, WINDOW_PADDING + SQUARE_PADDING
                                      + LINE_WIDTH * col + col * self.SQUARE_SIZE),
                          (WINDOW_PADDING - (SQUARE_PADDING + CROSS_WIDTH/10)+ LINE_WIDTH * row + row * self.SQUARE_SIZE + self.SQUARE_SIZE,
                             WINDOW_PADDING - SQUARE_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE + self.SQUARE_SIZE), CROSS_WIDTH)
         
         pygame.draw.line(win, RED, (int(WINDOW_PADDING - (SQUARE_PADDING + CROSS_WIDTH/10) + LINE_WIDTH * row + row * self.SQUARE_SIZE + self.SQUARE_SIZE),
                                      int(WINDOW_PADDING + SQUARE_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE)),
                           (int(WINDOW_PADDING + SQUARE_PADDING + CROSS_WIDTH/10 + LINE_WIDTH * row + row * self.SQUARE_SIZE), int(WINDOW_PADDING - SQUARE_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE 
                            + self.SQUARE_SIZE)), CROSS_WIDTH)
    
    def draw_figures(self, win):
         for row in range(self.size):
              for col in range(self.size):
                if self.matrix[row][col] == symbol["cross"]:
                    self.draw_cross(win, row, col)
                elif self.matrix[row][col] == symbol["circle"]:
                    self.draw_circle(win, row, col)

    def display_score(self, win):
         fontname = 'times'
         fontsize = 38
         font = pygame.font.SysFont(fontname, fontsize)

         label = font.render("Connect 4 game", 1, (255, 255, 255))
         win.blit(label, (WINDOW_PADDING + self.SQUARE_SIZE * self.size + 100 + 50, WINDOW_PADDING))

         fontsize = 24
         font = pygame.font.SysFont(fontname, fontsize)
         # apply it to text on a label
         label = font.render(f"Turn Number: {self.turn_number}", 1, (255, 255, 255))
         # put the label object on the screen at point x=100, y=100
         win.blit(label, (WINDOW_PADDING + self.SQUARE_SIZE * self.size + 100 + 100, WINDOW_PADDING + 500))

         pygame.draw.circle( win, BLUE, (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2,
                                          WINDOW_PADDING + 200), 
                                          25, 7 )
         
         pygame.draw.line(win, RED, (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 - 20, WINDOW_PADDING + 200 + 120),
                          (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 - 20 + 40,
                             WINDOW_PADDING + 200 + 120 + 40), CROSS_WIDTH)
         
         pygame.draw.line(win, RED, (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 - 20 + 40, WINDOW_PADDING + 200 + 120),
                           (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 - 20, WINDOW_PADDING + 200 + 120 + 40), CROSS_WIDTH)
         if self.circle_player_score >= 1:
              if self.cross_player_score >= 1:
                   pass
         label = font.render(f"Score: {self.circle_player_score}", 1, (255, 255, 255))
         win.blit(label, (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 + 50, WINDOW_PADDING + 200 - 12.5))

         label = font.render(f"Score: {self.cross_player_score}", 1, (255, 255, 255))
         win.blit(label, (WINDOW_PADDING + LINE_WIDTH * self.size + self.size * self.SQUARE_SIZE + 100 + self.SQUARE_SIZE/2 + 50, WINDOW_PADDING + 200 + 8 + 120))
                        

    
    def draw_circle(self, win, row, col):
         pygame.draw.circle( win, BLUE, (WINDOW_PADDING + LINE_WIDTH * row + row * self.SQUARE_SIZE + self.SQUARE_SIZE / 2,
                                          WINDOW_PADDING + LINE_WIDTH * col + col * self.SQUARE_SIZE + self.SQUARE_SIZE / 2), 
                                          self.CIRCLE_RADIUS, CIRCLE_WIDTH )
    
    def display_turn(self, win):
         pass
    
    def display_winner(self, win):
         if(self.turn_number >= self.size * 2 + 1):
             fontname = 'times'
             fontsize = 24
             font = pygame.font.SysFont(fontname, fontsize)

             winner = "Tie"

             if(self.circle_player_score > self.cross_player_score):
                 winner = "Cross player wins"
                 label = font.render(winner, 1, (255, 255, 255))
                 win.blit(label, (WINDOW_PADDING + self.SQUARE_SIZE * self.size + 100 + 50, WINDOW_PADDING))
             elif(self.circle_player_score < self.cross_player_score):
                 winner = "Circle player wins"
                 label = font.render(winner, 1, (255, 255, 255))
                 win.blit(label, (WINDOW_PADDING + self.SQUARE_SIZE * self.size + 100 + 50, WINDOW_PADDING))
        
             label = font.render("Tie", 1, (255, 255, 255))
             win.blit(label, (WINDOW_PADDING + self.SQUARE_SIZE * self.size + 100 + 50, WINDOW_PADDING))
    

    