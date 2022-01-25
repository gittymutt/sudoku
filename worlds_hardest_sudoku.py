# try to solve a real sudoku (38 filled) Most difficult puzzle in the 
# world https://www.kristanix.com/sudokuepic/worlds-hardest-sudoku.php

from board import Board

board = Board()

board.set_number(0, 0, 1)
board.set_number(5, 0, 6)
board.set_number(6, 0, 3)

board.set_number(1, 1, 3)
board.set_number(4, 1, 1)
board.set_number(7, 1, 4)

board.set_number(2, 2, 9)
board.set_number(3, 2, 5)
board.set_number(8, 2, 7)


board.set_number(2, 3, 6)
board.set_number(3, 3, 3)

board.set_number(1, 4, 2)
board.set_number(4, 4, 8)

board.set_number(0, 5, 7)
board.set_number(5, 5, 4)

board.set_number(2, 6, 5)
board.set_number(3, 6, 9)
board.set_number(8, 6, 3)

board.set_number(0, 7, 9)
board.set_number(6, 7, 1)


board.set_number(1, 8, 8)
board.set_number(4, 8, 2)
board.set_number(7, 8, 7)

print("Original Board")
board.print()
for tries in range(100):
    # eliminate non-sole candidates
    for board_row in board.board:
        for square in board_row:
            if square.filled:
                #print(square.x, square.y)
                board.eliminate_columns(square.x, square.y)
                board.eliminate_rows(square.x, square.y)
                board.eliminate_big_square(square.x, square.y)
                
    # Fill in unique candidates
    board.fill_unique()
    
    if board.solved():
        break
board.print()
if board.solved():
    print("Solved it!")
else:
    print("I'm stumped!!")


