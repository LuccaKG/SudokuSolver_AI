# -*- coding: ISO-8859-1 

from split_image import split_image
import pathlib
import os
import datetime as dt
import fileSelector as fs

file_sel = fs.WindowCreator(fs.win)
file_sel.buttons_creator()
fs.win.mainloop()

# create the folder where pictures is going to be stored 
actual_dir = pathlib.Path().resolve()  # store the current path


today = dt.date.today()
current_time = dt.datetime.now().strftime("%Hh%Mm")
directory = os.path.join("C:\\", actual_dir, f"Sudoku cells - {today} - {current_time}")
if not os.path.exists(directory):
    os.mkdir(directory)

split_image(f"{file_sel.sdk_path}", 9, 9, True, False, True, directory)


