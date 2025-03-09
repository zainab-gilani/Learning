import random


# Constants
GRID_SIZE = 5
NUM_SHIPS = 3

# - : Represents empty waters
# S : Represents a ship in that square

WATER_SHAPE = "-"
SHIP_SHAPE = "S"
HIT_SHAPE = "X"
MISS_SHAPE = "O"

# Global Variables
# List of rows / 2D grid
gameBoard = None
humanBoard = None
# Functions

def createBoard(size):
    """ Creates the board by making a list of rows that are of 'size' """
    grid = []
    # Create rows for the grid
    for i in range(size):
        row = []

        # Create columns for the grid
        for j in range(size):
            row.append(WATER_SHAPE)
        #endfor
        grid.append(row)
    #endfor
    return grid
#enddef

def placeShips(board, numShips, gridSize):
    # Randomly places numShips at different coordinates
    # Note: randint can return the same number more than once
    # So I am using a while loop to keep generating coordinates until they are unique

    coordinates = []
    while len(coordinates) != numShips:
        # Random number between 0 and GRID_SIZE
        row = random.randint(0, gridSize - 1)
        col = random.randint(0, gridSize - 1)
        coordinate = [row, col]

        if coordinate in coordinates:
            continue
        # endif

        board[row][col] = SHIP_SHAPE

        coordinates.append(coordinate)
    # endwhile
#enddef

def printBoard(board, gridSize):
    numbers = []
    for i in range(1, gridSize+1):
        numbers.append(str(i))
    print(" ", numbers)

    # Print rows and their row letters
    asciiA = ord("A")
    for row in board:
        print(chr(asciiA), row)
        asciiA = asciiA + 1
    #endfor
#enddef

def countShips(board):
    # go over each row and find if the square has a ship
    # increase count
    count = 0
    for row in board:
        for item in row:
            if item == SHIP_SHAPE:
                count = count + 1
            #endif
        #endfor
    #endfor
    return count
#enddef

# Returns a list of two numbers: [row, column], or None if it's invalid
def askPlayerForCoordinates(forHumanGuessing, gridSize):
    lastRow = chr(ord("A") + (gridSize-1))
    # A10

    word = "place ships"

    if forHumanGuessing:
        word = "fire"
    #endif

    ans = input("Enter coordinates to %s (between A1 - %s%d), e.g A1: " % (word, lastRow, gridSize)).upper().strip()

    if ans == "":
        return None
    #endif

    # take first letter convert letter to row
    row = ord(ans[0]) - ord("A")
    if row > gridSize or row < 0:
        return None
    #endif

    # take rest and convert to column
    colStr = ans[1:]

    if colStr == "":
        return None
    #endif

    if not colStr.isnumeric():
        return None
    #endif

    column = int(colStr) - 1

    if column >= gridSize or column < 0:
        return None
    #endif

    return [row, column]
#enddef


# Coordinates: [Int], first is always row, second is always column
# Board: [[""]]
# Returns True if ship is fired
def fireAtShip(coordinates, board):
    didFireShip = False

    # go to coordinates see if ship there
    # if ship there put "H"
    # else put "M"
    row = coordinates[0]
    col = coordinates[1]

    shape = board[row][col]
    #print(shape, row, col)
    if shape == SHIP_SHAPE:
        board[row][col] = HIT_SHAPE
        print("It's a hit!")

        shipsLeft = countShips(board)
        if shipsLeft == 1:
            print("There is %d ship remaining" % (shipsLeft))
        else:
            print("There are %d ships remaining" % (shipsLeft))
        #endif

        didFireShip = True
    else:
        board[row][col] = MISS_SHAPE
        print("Oops! That's a miss!")
    #endif

    return didFireShip
#enddef

def humanPlaysGame():
    gameBoard = createBoard(GRID_SIZE)

    # 2. Random Placement of Ships

    placeShips(gameBoard, NUM_SHIPS, GRID_SIZE)

    # printBoard(gameBoard, GRID_SIZE)

    # Count tries
    print("I have placed %d battleships in the sea of grid size %dx%d. Let's see how quickly you can sink them.\n" % (
    NUM_SHIPS, GRID_SIZE, GRID_SIZE))

    hits = 0
    misses = 0

    while countShips(gameBoard) > 0:
        # 3. Ask Human to Fire at Ships
        coordinates = askPlayerForCoordinates(True, GRID_SIZE)

        if coordinates == None:
            print("That's an invalid coordinate, try again!")
            continue
        # endif

        # Fire at coordinate
        didFire = fireAtShip(coordinates, gameBoard)

        # Increment the number of tries
        if didFire:
            hits = hits + 1
        else:
            misses = misses + 1
        # endif

    # endwhile

    print("You sunk all the ships in %d misses" % (misses))

    # Debug

    printBoard(gameBoard, GRID_SIZE)
#enddef

def compPlaysGame():
    # DONE  1. Create a new board
    # DONE 2. Ask user for coordinates to place ships until all ships added
    # DONE 3. Place ships on the board
    # DONE 4. Print the board on each placement

    # TODO 5. Computer Guesses coordinates and we show score for computer

    # 6. Human plays (current game)

    print("I've created a battleship board for you to place some ships on")

    humanBoard = createBoard(GRID_SIZE)

    printBoard(humanBoard, GRID_SIZE)

    while countShips(humanBoard) < NUM_SHIPS:
        coordinates = askPlayerForCoordinates(False, GRID_SIZE)

        if coordinates == None:
            print("That's an invalid coordinate, try again!")
            continue
        # endif

        row = coordinates[0]
        col = coordinates[1]
        humanBoard[row][col] = SHIP_SHAPE

        printBoard(humanBoard, GRID_SIZE)
    #endwhile


# 1. Game setup

compPlaysGame()

#humanPlaysGame()





