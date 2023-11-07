
## Name:                EECS 210 Assignment 6
## Description:         A program that can solve Sudoku problems and tell you if they are unsolvable.
## Author:              Riley Meyerkorth
## Collaborators:       N/A
## Sources:             N/A
## Inputs:              N/A
## Outputs:             Prints out whether it was able to solve the Sudoku puzzle or not. If not, it prints it's proof.
## Creation date:       2023 November 6
## Modification Date:   2023 November 6

class Solver:
    # TODO: Implement proof of unsolvable problems
    
    def solve(self, puzzle:list[list]):
        """Solves a given Sudoku problem"""
        # If the recursive function does not return anything, it means that no solution was found.
        if not self._solve_rec(puzzle):
            print("No solution found.")
    
    def _solve_rec(self, puzzle:list[list]):
        """Recursively solves a Sudoku problem by brute-force"""
        # Find an empty cell in the puzzle
        empty = self._findEmptyCell(puzzle)
        
        # If no empty cell is found, then the puzzle is solved.
        if not empty:
            # Print the puzzle
            printPuzzle(puzzle)
            return True
        
        # Get the row and column indices
        row, col = empty

        # Iterate through the range of numbers in any given cell
        for num in range(1, 10):
            # Check if the value is valid with the empty column. If it is...
            if self._isValid(puzzle, row, col, num):
                # Set the cell to that number
                puzzle[row][col] = num

                # If the puzzle is solved from this...
                if self._solve_rec(puzzle):
                    return True

                # If our choice didn't lead to a solution, set the value to zero and backtrack
                puzzle[row][col] = 0

        # Backtrack fallback
        return False
    
    def _isValid(self, board:list[list], row:int, col:int, num:int):
        """Checks whether a Sudoku board is valid by checking the rows and columns against the value of a given cell"""
        # Check if 'num' is not in the given 'row' by iterating through possible values
        for x in range(9):
            if board[row][x] == num:
                return False

        # Check if 'num' is not in the given 'col' by iterating through possible values
        for x in range(9):
            if board[x][col] == num:
                return False

        # Check if 'num' is not in the given 3x3 box by modulus math
        startRow = row - row % 3
        startCol = col - col % 3
        # Iterate through the 3x3 and check for the value of 'num'
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                # If 'num' is in the 3x3 already, it is not valid
                if board[i][j] == num:
                    return False

        # If these tests fail, it is valid
        return True

    def _findEmptyCell(self, board:list[list]):
        """Finds an empty cell within a given Sudoku board as a tuple"""
        # Iterate through the indices of the board's 2D array
        for i in range(9):
            for j in range(9):
                # If the spot is equal to an empty cell's value, return the cell's coordinates
                if board[i][j] == 0:
                    return (i, j)
        # Otherwise, return None, indicating that an empty cell does not exist
        return None
        
def createPuzzle(txt_file:str):
    """Creates a 2D array of a Sudoku puzzle from a text file"""
    puzzle = []
    # Open the text file to read the Sudoku puzzle from
    file = open(txt_file, 'r')
    # Iterate through the lines of the file within an iterator (list)
    for line in file.readlines():
        """
            Append the line to the puzzle matrix after doing the following:
            1. Replacing the "_" characters to zeros
            2. Removing the newlines
            3. Splitting the string into a list with a space separator
            4. Cast every value to an integer using list comprehension
        """
        puzzle.append([int(i) for i in line.replace("\n", "").replace("_", "0").split()])
    return puzzle
    
def printPuzzle(puzzle:list[list]):
    """Prints the given Sudoku puzzle"""
    # Iterate through every cell of the puzzle
    for row in puzzle:
        for cell in row:
            # Transform zeros back to "_" input char
            if (cell == 0): cell = "_"
            # Print the cell value
            print(cell, end=" ")
        # Print a line break at the end of each row
        print()
    
def main():
    # Initialie solver
    solver = Solver()
    
    # All puzzles/test cases to solve
    puzzles = ["puzzle1.txt", 
               "puzzle2.txt", 
               "puzzle3.txt", 
               "puzzle4.txt", 
               "puzzle5.txt"]
    
    # Iterate through all puzzle files
    for i, name in enumerate(puzzles, start=1):
        # Create the puzzle
        puzzle = createPuzzle(name)
        
        # Print the unsolved puzzle
        print(f"--- Puzzle #{i}: {name} ---")
        printPuzzle(puzzle)
        
        # Print the solved puzzle
        print(f"\n--- Solution #{i} {name} ---")
        solver.solve(puzzle)
        
        # Print a newline for clarity/formatting
        print()

# Default main name check
if __name__ == '__main__':
    main()