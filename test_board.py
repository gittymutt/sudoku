from board import Board

b = Board()

# b.print_coords()
r = b.get_row(0)

# for s in r:
#     #print(s.x, s.y)
#     print(s.numbers_left)

# c = b.get_col(3)
# print("object is: ", c)
# for s in c:
#     #print(s.x, s.y)

#print(c[3].x, c[3].y)

block = b.get_block(8, 8)
print(block)

for s in block:
    print(s.x, s.y)
