import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


img = cv2.imread(
    "C:/Users/lucca/OneDrive/Documentos/Projetos/Sudoku Solver/Sudoku cells - 2023-07-30 - 18h07m/ex2_1.jpg"
)

# Adding custom options
custom_config = r"--oem 3 --psm 6"
a = pytesseract.image_to_string(img, config=custom_config)
print(a == "")
