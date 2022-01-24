from square import Square
from math import floor


class Board:
    def __init__(self, x=9, y=9):
        self.board = [[ Square(i, j) for j in range (y)] for i in range (x)]
    
    def eliminate_columns(self, x, y):
        if self.board[x][y].filled == 0:
            print("Can't eliminate. ", x, ", ", y, " is not filled. Continuing...")
            return False
        filled = self.board[x][y].filled
        #print("number to eliminate is ", filled)
        for col_num in range(9):
            self.board[col_num][y].eliminate(filled)
            
    def eliminate_rows(self, x, y):
        if self.board[x][y].filled == 0:
            print("Can't eliminate. ", x, ", ", y, " is not filled. Continuing...")
            return False
        filled = self.board[x][y].filled # filled is the filled in number that we want to eliminate from other rows
        # print("number to eliminate is ", filled)
        for row_num in range(9):
            self.board[x][row_num].eliminate(filled)
    
    def eliminate_big_square(self, x, y):
        if self.board[x][y].filled == 0:
            print("Can't eliminate. ", x, ", ", y, " is not filled. Continuing...")
            return False
        filled = self.board[x][y].filled
    
        top_x_corner = floor(x/3)*3
        top_y_corner = floor(y/3)*3
        for x in range(3):
            for y in range(3):
                #print(top_x_corner + x, top_y_corner + y )
                self.board[top_x_corner + x][top_y_corner + y].eliminate(filled)

            
    
    
    
    def set_number(self, x, y, num):
        self.board[x][y].fill(num)
    
    
    
    def solved(self):
        solved = True
        for board_row in self.board:
            for square in board_row:
                if not square.filled:
                    solved = False
        return solved
    
    def has_single_possibilities(self):
        possibilities = False
        for board_row in self.board:
            for square in board_row:
                if not square.has_one():
                    possibilities = False
        return possibilities
    
    # only works with 3x3 now. change 
    def print(self):
        print()
        big_sq_horiz_border = 1
        for board_row in self.board:
            for square_row in range(3):
                big_sq_vert_border=1
                for s in board_row:
                    
                    for count, j in enumerate(s.get_row((square_row))):
                        if isinstance(j, str):
                            if s.filled:
                                print(end=" . ")
                            else:
                                print(end="   ")
                        else:
                            print ("{:2d}".format(j), end=" ")
                    if big_sq_vert_border % 3 == 0:
                        print(" @ ", end="")
                    else:
                        print(" | ", end="")
                    big_sq_vert_border = big_sq_vert_border + 1 # make every 3rd vertical line thick
                    
                    
                print()
            if big_sq_horiz_border % 3 == 0:    
                print("@ "*54)
            else:
                print("-"*108)
            big_sq_horiz_border = big_sq_horiz_border + 1
