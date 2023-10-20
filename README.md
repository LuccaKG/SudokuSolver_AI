# Sudoku AI Solver

Sudoku Solver made in Python for 9x9 boards with 3x3 sub-grids.
The script receives a board image as input, pre-processes the image and subsequently recognizes the digits using PyTesseract.
Once the board was recognized, the 'py-sudoku' library was used to format and solve the game - the resolution could also be implemented manually, through linear programming.

## How to run

- [x] Have a well-adjusted photo of the Sudoku board you want to solve, as shown in the example below

![WhatsApp Image 2023-10-20 at 18 01 45](https://github.com/LuccaKG/SudokuSolver_AI/assets/122898459/d38f3190-8949-49bd-bde3-04dc8dd0879f)

- [x] Run **main.py** file and a file selection menu will appear. Click "Open file" and open the board picture

![image](https://github.com/LuccaKG/SudokuSolver_AI/assets/122898459/bdd6420d-6fc7-4d1f-b2ee-f556744f56fc)

- [x] Click the "Solve Sudoku" button. A terminal session will be opened with the message "Solver is running! Please wait."

During the execution, a folder called *Sudoku Cells - \<YY-MM-DD\>* will be created in the same directory as the execution, which will contain 81 photos, each one being a cutout of each cell on the board, in addition to a photo of the complete pre-processed board. All images will already be pre-processed by *imgPreProcessing.py* and their names will indicate the cell index on the board - starting at position 0, which is in the upper left corner and ending at position 80, in the lower right corner.

This folder will be traversed by the *puzzleRecognition.py* file, which will identify each digit present in each cell and return a matrix representing the board. In turn, the generated matrix will be accessed by the *solver.py* script invoked in the main function, which will print in the terminal the original board, the difficulty (number of empty cells) and, finally, the board filled with the solution.
In case the input board has no solution, the message "INVALID PUZZLE (GIVEN PUZZLE HAS NO SOLUTION)" will appear. 

Using the board mentioned above as an example, we obtained the following output:

![image](https://github.com/LuccaKG/SudokuSolver_AI/assets/122898459/b038df37-7a3f-4642-94ed-d4ea02894502)

By filling in the board in the mobile application where the game was generated, we confirm the solution from the script output

![WhatsApp Image 2023-10-20 at 18 30 03](https://github.com/LuccaKG/SudokuSolver_AI/assets/122898459/3e8d4dd4-cc74-44a2-b6a3-d8ea285d7cdd)

### Important note 

To be able to use PyTesseract, first download the .exe file from the https://github.com/UB-Mannheim/tesseract/wiki repository.

After completing the installation, define the path to the .exe in the script, as shown in the puzzleRecognition.py file

![image](https://github.com/LuccaKG/SudokuSolver_AI/assets/122898459/291ebe7f-321b-4522-bf00-1ddef798163e)

## About PyTesseract 🤖

PyTesseract is a Python binding for Google's Tesseract-OCR Engine. Tesseract itself is an Optical Character Recognition (OCR) tool, originally developed by Hewlett-Packard in the 1980s and 1990s. In 2005, it was open-sourced by HP and later, in 2006, it was adopted by Google. Since then, it has been continuously developed and has become one of the most accurate open-source OCR engines available.

The PyTesseract library allows Python developers to use Tesseract's capabilities directly in their applications, providing an easy way to extract text from images. By integrating Tesseract with Python, PyTesseract has made it simpler for developers to implement OCR solutions in Python-based projects.

## About py-sudoku 🔢

A simple Python program that generates and solves m x n Sudoku puzzles. More info on: https://pypi.org/project/py-sudoku/ 

## Possible improvements 🔍

This project solves traditional 9x9 boards with 3x3 sub-grids. However, we can change the code to enable the recognition of boards with different shapes, after all the *py-sudoku* library allows larger boards to be solved!



