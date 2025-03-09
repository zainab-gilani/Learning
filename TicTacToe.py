# Tic Tac Toe

# Here are some goals
# 1. Requires a Grid 3x3
# 2. Two players - one is computer and other is user
# 3. Put X and O in empty spots only
# 4. The first user to have a straight line in any order (even diagonal) wins

# Requirements:
# 1. Use a Class to represent the Game
# 2. Write nice girly code
# 3. Document logic where needed

class TicTacToe:
    def __init__(self):
        # Create the grid
        self.__grid = []
        for i in range(3):
            row = []
            self.__grid.append(row)
            for j in range(3):
                row.append(" ")
            # endfor
        # endfor

        self.print_grid()
    # enddef

    def print_grid(self):
        for i in range(3):
            if i == 0:
                print(f"{self.__grid[i][0]}|{self.__grid[i][1]}|{self.__grid[i][2]}")
                print("-+-+-")
            elif i == 1:
                print(f"{self.__grid[i][0]}|{self.__grid[i][1]}|{self.__grid[i][2]}")
                print("-+-+-")
            else:
                print(f"{self.__grid[i][0]}|{self.__grid[i][1]}|{self.__grid[i][2]}")
            #endif
        #endfor
    # enddef

    def guess(self):
        pass
    #enddef

    def askUser(self):
        ans = input("Give row and column for placing X (e.g. 3,2): ")
        pos = ans.split(",")
        row = int(pos[0])-1
        column = int(pos[1])-1
        self.__grid[row][column] = "X"

        self.print_grid()
    #enddef
# endclass

game = TicTacToe()
game.askUser()