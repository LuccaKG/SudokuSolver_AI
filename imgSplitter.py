# -*- coding: ISO-8859-1 

from split_image import split_image
import fileSelector as fs

file_sel = fs.WindowCreator(fs.win)
file_sel.buttons_creator()
fs.win.mainloop()

