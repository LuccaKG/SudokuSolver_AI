# -*- coding: ISO-8859-1
import imgPreProcessing as ipp
import fileSelector as fs
import puzzleRecognition as pr

# open window to select original sudoku puzzle
file_sel = fs.WindowCreator(fs.win)
file_sel.buttons_creator()
fs.win.mainloop()
 
ipp.Mkdir() # create folder where splitted images will be stored
ipp.ImgPreProc(file_sel.sdk_path) # run image processing applying threshold and split

print("Solver is running! Please wait.")
puzzle = pr.PuzzleRec() # store cell values (already recognized)

pr.PrintPuzzle(puzzle) # print the recognized puzzle




