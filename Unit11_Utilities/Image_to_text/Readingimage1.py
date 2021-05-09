# python.exe -m pip install --upgrade pip
# pip install pytesseract
# dowmload and install tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe from https://github.com/UB-Mannheim/tesseract/wiki
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
file_name = "image_2.jpeg"
img = cv2.imread(file_name)
text = pytesseract.image_to_string(img)
print(text)