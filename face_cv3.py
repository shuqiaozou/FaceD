#!/usr/bin/env python
# coding=utf-8
import cv2
# import sys

# 获取输入的图片
imagePath = "./imgs/1.jpeg"
cascPath = "haarcascade_frontalface_default.xml"

# 创建haar级联分类器对象
faceCascade = cv2.CascadeClassifier(cascPath)

# 读取图片
image = cv2.imread(imagePath)
# 将图片转为灰度格式
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 识别图片中的人脸
faces = faceCascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 打印出识别的人脸数
print("Found {0} faces!".format(len(faces)))

# 在人脸周围画出矩形
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
