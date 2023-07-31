# -*- coding: ISO-8859-1
import cv2
from imutils import contours
import numpy as np
import pathlib
import os
import datetime as dt
from split_image import split_image

today = dt.date.today()
current_time = dt.datetime.now().strftime("%Hh%Mm")
# create the folder where pictures is going to be stored
actual_dir = pathlib.Path().resolve()  # store the current path
directory = os.path.join("C:\\", actual_dir, f"Sudoku cells - {today} - {current_time}")


def Mkdir():
    if not os.path.exists(directory):
        os.mkdir(directory)


# apply pre-processing to image and split each cell from puzzle; save splitted cells on a directory
def ImgProc(path):
    image = cv2.imread(path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    file_name = f"PreProcessedSudokuPuzzle_{today}_{current_time}"
    cv2.imwrite(f"{file_name}.jpg", thresh)
    split_image(f"{file_name}.jpg", 9, 9, True, True, True, directory)
