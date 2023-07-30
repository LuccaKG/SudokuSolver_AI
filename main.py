# -*- coding: ISO-8859-1
import imgProcessing
import fileSelector as fs

# open window to select original sudoku puzzle
file_sel = fs.WindowCreator(fs.win)
file_sel.buttons_creator()
fs.win.mainloop()
 
imgProcessing.Mkdir() # create folder where splitted images will be stored
imgProcessing.ImgProc(file_sel.sdk_path) # run image processing applying threshold and split

