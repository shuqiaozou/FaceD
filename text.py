# coding=utf-8
import pytesseract
import PIL
img = PIL.Image.open("/Users/mac/Learn/LearnPython/4.png")
text = pytesseract.image_to_string(img)
s = repr(text)
f = open("output.text", "w")
f.write(s)
f.close()
