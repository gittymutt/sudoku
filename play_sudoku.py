from board import Board

# try to solve a real sudoku (38 filled) Easy level from sudoku.com

board = Board()

board.set_number(0, 0, 6)
board.set_number(1, 0, 8)
board.set_number(6, 0, 3)
board.set_number(8, 0, 2)
board.set_number(2, 1, 4)
board.set_number(4, 1, 8)
board.set_number(7, 1, 9)
board.set_number(0, 2, 9)
board.set_number(1, 2, 1)
board.set_number(3, 2, 7)

board.set_number(4, 2, 2)
board.set_number(7, 2, 6)
board.set_number(1, 3, 7)
board.set_number(2, 3, 9)
board.set_number(5, 3, 1)
board.set_number(6, 3, 6)
board.set_number(7, 3, 8)
board.set_number(1, 4, 6)
board.set_number(6, 4, 7)
board.set_number(7, 4, 3)

board.set_number(8, 4, 4)
board.set_number(1, 5, 3)
board.set_number(2, 5, 8)
board.set_number(4, 5, 6)
board.set_number(6, 5, 2)
board.set_number(2, 6, 6)
board.set_number(3, 6, 9)
board.set_number(5, 6, 3)
board.set_number(6, 6, 8)
board.set_number(7, 6, 5)

board.set_number(2, 7, 5)
board.set_number(3, 7, 1)
board.set_number(5, 7, 8)
board.set_number(7, 7, 2)
board.set_number(1, 8, 9)
board.set_number(2, 8, 1)
board.set_number(4, 8, 5)
board.set_number(8, 8, 3)

turns = 0
while not board.solved():
    turns = turns+1
    print("Turn ", turns)
    for board_row in board.board:
        for square in board_row:
            if square.filled:
                #print(square.x, square.y)
                board.eliminate_columns(square.x, square.y)
                board.eliminate_rows(square.x, square.y)
                board.eliminate_big_square(square.x, square.y)
        print()
    board.print()

board.print()