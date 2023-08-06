# -*- coding: ISO-8859-1
import cv2
from imutils import contours
import numpy as np
import pathlib
import os
import datetime as dt
from split_image import split_image

today = dt.date.today()
# create the folder where pictures is going to be stored 
actual_dir = pathlib.Path().resolve()  # store the current path
directory = os.path.join("C:\\", actual_dir, f"Sudoku cells - {today}")


def Mkdir():
    if not os.path.exists(directory):
        os.mkdir(directory)


# apply pre-processing to image and split each cell from puzzle; save splitted cells on a directory
file_name = "ThresholdedPuzzle"
def ImgPreProc(path:str):
    image = cv2.imread(path)

    # Load image, grayscale, Gaussian blur, Otsu's threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Detect horizontal lines
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50,1))
    horizontal_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)

    # Detect vertical lines
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,50))
    vertical_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=1)

    # Combine masks and remove thickest lines
    table_mask = cv2.bitwise_or(horizontal_mask, vertical_mask)
    image[np.where(table_mask==255)] = [255,255,255]

    # Apply thresh again to remove thinest lines
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    invert = 255 - thresh

    cv2.imwrite(f'{file_name}.jpg', invert)
    split_image(f"{file_name}.jpg", 9, 9, True, True, True, directory)
