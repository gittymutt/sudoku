# try to solve a real sudoku (38 filled) Evil difficulty level from sudoku.com
from board import Board

board = Board()

board.set_number(1, 0, 5)
board.set_number(2, 0, 4)
board.set_number(8, 0, 6)
board.set_number(0, 1, 6)
board.set_number(4, 1, 3)
board.set_number(6, 1, 9)
board.set_number(0, 2, 3)
board.set_number(3, 2, 4)
board.set_number(4, 2, 8)
board.set_number(6, 2, 1)

board.set_number(5, 3, 1)
board.set_number(1, 4, 6)
board.set_number(4, 4, 9)
board.set_number(6, 4, 8)
board.set_number(0, 5, 8)
board.set_number(7, 5, 7)
board.set_number(7, 6, 2)
board.set_number(2, 7, 3)
board.set_number(4, 7, 1)
board.set_number(6, 7, 5)

board.set_number(0, 8, 7)
board.set_number(5, 8, 5)


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
    # board.print()


board.print()
if board.solved():
    print("Solved it!")
else:
    print("I'm stumped!!")


