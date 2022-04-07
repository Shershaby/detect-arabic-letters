import matplotlib.pyplot as plt
import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import re

path = r'F:\AI Diploma\New\images\Arabic imgs\dream.jpg'

def text_image(path):
    image = cv.imread(path)
    rgb_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    plt.imshow(rgb_img)
    plt.title('Original Image')
    plt.show()
    
    gray_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2GRAY)
    plt.imshow(gray_img, cmap='gray')
    plt.title('Gray Image')
    plt.show()
    
    adap = cv.ADAPTIVE_THRESH_MEAN_C
    thresh_1 = cv.adaptiveThreshold(gray_img, 255, adap, cv.THRESH_BINARY, 51, 3)
        
    text = pytesseract.image_to_string(thresh_1, config='--psm 9', lang='ara')
    characters = re.sub(r'[\d\W\s]'," ", text)
    
    letters = list(characters)
    
    print(characters)
    print(letters)
     
text_image(path)
