import cv2 
import pytesseract
import os
import imgPreProcessing

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def PuzzleRec() -> list:
    # I'm not using the os.listdir() function because it doesn't order the list of files properly
    img_list = []
    for index in range(0,81):
        img_list.append(f"{imgPreProcessing.file_name}_{index}.jpg")

    # Adding Tesseract's custom options
    custom_config = r'--psm 6'

    digits_list = [] # creating a list to populate with recognized digits 
    # Running Tesseract OCR to recognize digits and blankspaces

    for filename in img_list:
        img = cv2.imread(f"{imgPreProcessing.directory}\{filename}")
        img = img[int(0.2*img.shape[0]):img.shape[0], int(0.1*img.shape[0]):int(0.9*img.shape[0])] # crop image to avoid noises on borders
        digit = pytesseract.image_to_string(img, config=custom_config)
        if digit != "": # verify if it isn't a blankspace
            digits_list.append(int(digit))
        else: # fill blankspaces as - 
            digits_list.append(0)


    # divides the list of recognized digits into sublists, where each sublist represents a puzzle line
    n = 9  # Number of elements per sublist -- 9 digits per line
    digits_grouped = [digits_list[i:i + n] for i in range(0, len(digits_list), n)]

    return digits_grouped
