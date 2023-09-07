from array import Array
import random

class Grid():
    def __init__(self, rows, columns,fill_value=None ):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value=fill_value)
        
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

                result += "\n"

        return str(result)
    
    def random_fill(self, min, max):
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self[i][j] = random.randint(min, max)

if __name__ == "__main__":
    from array import array
    grid = Grid(5, 5)
    grid.random_fill(0, 1)
    print(grid)
    print(grid.get_height())
    print(grid.get_width())
    print(grid[0][0])
    print(grid[0][1])
    print(grid[0][2])
    print(grid[0][3])
    print(grid[0][4])
    print(grid[1][0])
    print(grid[1][1])
    print(grid[1][2])
    print(grid[1][3])
    print(grid[1][4])
    print(grid[2][0])
    print(grid[2][1])
    print(grid[2][2])
    print(grid[2][3])
    print(grid[2][4])
    print(grid[3][0])
    print(grid[3][1])
    print(grid[3][2])
    print(grid[3][3])
    print(grid[3][4])
    print(grid[4][0])
    print(grid[4][1])
    print(grid[4][2])
    print(grid[4][3])
    print(grid[4][4])
    print(grid[5][0])
    print(grid[5][1])
    print(grid[5][2])
    print(grid[5][3])
    print(grid[5][4])
    print(grid[6][0])
    print(grid[6][1])
    print(grid[6][2])
    print(grid[6][3])
    print(grid[6][4])
    print(grid[7][0])
    print(grid[7][1])
    print(grid[7][2])
    print(grid[7][3])
    print(grid[7][4])
    print(grid[8][0])
    print(grid[8][1])
    print(grid[8][2])
    print(grid[8][3])
    print(grid[8][4])
    print(grid[9][0])
    print(grid[9][1])
    print(grid[9][2])
    print(grid[9][3])
    print(grid[9][4])
    print(grid[10][0])
    print(grid[10][1])
    print(grid[10][2])
    print(grid[10][3])
    print(grid[10][4])
    print(grid[11][0])
    print(grid[11][1])
    print(grid[11][2])