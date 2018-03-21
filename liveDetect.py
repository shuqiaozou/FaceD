#!/usr/bin/env python
# coding=utf-8
import cv2

# 创建一个VideoCapture类实例
cap = cv2.VideoCapture(0)

# 创建haar级联分类器
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while (True):

    # 捕捉每一帧画面
    ret, frame = cap.read()

    # 将每一帧画面进行灰度处理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 抓取图片中的人脸
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    # 输出捕获到的人脸数
    print("Found {0} faces!".format(len(faces)))

    # 用矩形标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示标记后的画面
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放capture
cap.release()
cv2.destroyAllWindows()
