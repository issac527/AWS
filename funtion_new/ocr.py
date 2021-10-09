# 0.필요한 라이브러리
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt

# 버전 확인
print(cv2.__version__)
print(pytesseract.__version__)

# pytesseract
from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# # TEST.짧은 단어
# img = Image.open('images/다운로드.png')
# config = ('-l kor --oem 3 --psm 11')
# text1 = pytesseract.image_to_string(img, config=config)
# print(text1)
#
# print("===========================================")
# # TEST.문장
# img = Image.open('images/안전수칙.jpg')
# config = ('-l kor --oem 3 --psm 11')
# text2 = pytesseract.image_to_string(img, config=config)
# print(text2)

print("============================================")
# Test.무등산 팽나무 표지판
img = Image.open('images/grayeun.jpg')
config = ('-l kor --oem 3 --psm 11')
text3 = pytesseract.image_to_string(img, config=config)
print(text3)

print("============================================")
# 2. 메타문자 제거
import re

text3_re = re.sub('\s+',' ',text3)
print(text3_re)

# 3. 글자 인식 한 것 - 텍스트 파일로 저장
f = open(r'C:/Users/gold7/Desktop/text/eun.txt', 'w', encoding='UTF-8')
f.write(text3_re)
f.close()

