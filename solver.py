from sudoku import Sudoku

def PrintPuzzle(Puzzle:list):
    global puzzle
    puzzle = Sudoku(3, 3, board=Puzzle)
    print("-"*100)
    print("Here's your puzzle! The difficulty indicates the % of empty cells (e.g. 0.4 = 40% of empty cells)")
    print("-"*100)
    print(puzzle)

def PrintSolution():
    print("-"*40)
    print("Your solution is ready! Check below 👇")
    print("-"*40)
    puzzle.solve(raising=True).show_full()
