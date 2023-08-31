def make_a_grid():
    grid = []
    for i in range(0, 6):
        grid.append([])
        for j in range(0, 7):
            grid[i].append(".")
    return grid

def print_grid(grid):
    for row in grid:
        print("|", end = "")
        for cell in row:
            print(cell, end = "|")
        print("")

def get_integer_input(question):
    while True:
        try:
            integer = int(input(question))
            return integer
        except Exception:
            print("Your input is not an integer. Try again.")

def play_connect4(grid):
    four_in_a_row = False
    while four_in_a_row == False:
        print_grid(grid)
        circle = get_integer_input("Which column would you like to drop your circle into? ")
        grid = fill_in_grid_circle(circle, grid)
        won_game = check_win_condition(grid)
        if won_game == True:
            print("Team Circle has won!")
            print_grid(grid)
            exit()

        print_grid(grid)
        cross = get_integer_input("Which column would you like to drop your cross into? ")
        grid = fill_in_grid_cross(cross, grid)
        won_game = check_win_condition(grid)
        if won_game == True:
            print("Team Cross has won!")
            print_grid(grid)
            exit()

def fill_in_grid_circle(column, grid):
    invalid_input = True
    while invalid_input == True:
        try:
            if grid[0][column - 1] == "O" or grid[0][column - 1] == "X":
                column = get_integer_input("The column is full. Try another column: ")
            else:
                invalid_input = False
        except Exception:
            column = get_integer_input("There is a problem with your input. Which column would you like to drop your"
                                       " circle into? ")

    for row in reversed(grid):
        if row[column - 1] == ".":
            row[column - 1] = "O"
            break

    return grid

def fill_in_grid_cross(column, grid):
    invalid_input = True
    while invalid_input == True:
        try:
            if grid[0][column - 1] == "O" or grid[0][column - 1] == "X":
                column = get_integer_input("The column is full. Try another column: ")
            else:
                invalid_input = False
        except Exception:
            column = get_integer_input("There is a problem with your input. Which column would you like to drop your"
                                       " cross into? ")

    for row in reversed(grid):
        if row[column - 1] == ".":
            row[column - 1] = "X"
            break

    return grid

def check_win_condition(grid):
    for row in grid: # Iterate through each row
        for col in range(len(row) - 3): # Go through columns 1-4 because any later isn't possible to have 4-in-a-row
            # horizontally
            if row[col] == row[col + 1] == row[col + 2] == row[col + 3] != ".": # Check if there is a match not equal
                # to an empty cell horizontally
                return True # If there is, return a win

    for col in range(len(grid[0])): # Iterate through indexes/columns 1-7
        for row in range(len(grid) - 3): # Iterate through indexes/rows 1-4 because any later rows you can't have
            # 4-in-a-row vertically
            if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] != ".": # Check for
                # each column and rows 1-4 that there is a match not equal to an empty cell vertically
                return True # If there is, return a win


    for row in range(len(grid) - 3): # Iterate through indexes/rows 1-4 because any later rows you can't have
        # 4-in-a-row diagonally
        for col in range(len(grid[0]) - 3): # This is diagonally from left to right, so you can only go through columns
            # 1-4 to have 4-in-a-row
            if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] != ".":
                return True

    for row in range(len(grid) - 3): # Iterate through indexes/rows 1-4 because any later rows you can't have
        # 4-in-a-row diagonally
        for col in range(3, len(grid[0])): # This is diagonally from right to left, so you can only go through columns
            # 4-7 to have 4-in-a-row
            if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] != ".":
                return True

    if "." not in grid[0]: # If the top row has no empty cells, the game has ended as a tie
        print("There is no winner! It's a tie!")
        exit()

    return False # If no conditions filled, the game continues







def main():
    grid = make_a_grid()
    play_connect4(grid)

main()