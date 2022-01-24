from math import sqrt, ceil, floor

class Square:
    # x, y = which box the square occupies on the board
    # size = range of numbers used in the game. Ex 1-9
    # for a 9x9 board
    def __init__(self, x, y, number_range=9):
        self.numbers_left = [i+1 for i in range(number_range)]
        self.filled = 0
        self.x = x
        self.y = y
        self.number_range = number_range
        
    def has_one(self):
        return len(self.numbers_left) == 1

    def eliminate(self, num):
        if num in self.numbers_left and not self.has_one():
            self.numbers_left.remove(num)
            #print("removed ", num, " from ", self.x, ", ", self.y, " ", self.numbers_left)
            if self.has_one():
                self.filled = self.numbers_left[0]
                #print("Filled in ", self.x, ", ", self.y, " with ", self.numbers_left[0])
                
    def print_numbers(self):
        #print(self.x, self.y)
        #print("filled: ", self.filled)
        for n in self.numbers_left:
            print(n)

    # Return yth row of numbers for printing.
    # Turns into a square 2-d array. Index 0-x
    
    def get_row(self, y):
        
        
        side_length = ceil(sqrt(self.number_range))
        display_grid = [' '] * self.number_range 
        # print("dispaly_grid: ", display_grid, "number range: ", self.number_range)
        for i in self.numbers_left:
            display_grid[i-1] = i
        return display_grid[y*side_length:y*side_length+side_length]
        
              
            
    
    def fill(self, num):
        if num >= 1 and num <= 9:
            self.filled = num
            self.numbers_left = [num]