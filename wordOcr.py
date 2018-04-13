# coding=utf-8
'''文字ocr'''
import sys
import time
from PIL import Image
import pytesseract

reload(sys)
sys.setdefaultencoding('utf-8')

time1 = time.time()

img = Image.open('/Users/mac/Learn/LearnPython/imgs/4.png')
text = pytesseract.image_to_string(img)
print text
# print time.asctime(time.localtime(time.time()))
# print time.ctime()
# s = repr(text)
# f = open("output.text", "w")
# f.write(s)
# f.close()
