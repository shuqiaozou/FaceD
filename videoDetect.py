# coding=utf-8
'''对视频中人像的捕捉'''

import cv2
import numpy

cap = cv2.VideoCapture("./imgs/demo.mp4")

# 创建haar级联分类器
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while (1):

    # 读取画面
    ret, frame = cap.read()

    # 将每一帧画面进行灰度处理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 抓取图片中的人脸
    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 输出捕获到的人脸数
    print("Found {0} faces!".format(len(faces)))

    # 用矩形标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示画面
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 释放capture，关闭窗口
cap.release()
cv2.destroyAllWindows()
