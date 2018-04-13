# -*-coding:utf-8-*-
# 验证码识别
import sys
from PIL import Image
import pytesseract
import time

# 制定utf-8编码方式
reload(sys)
sys.setdefaultencoding('utf-8')

time1 = time.time()


# 二值化算法
def binarizing(img, threshold):
    '''将图片转为二值图'''
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


# 获取二值映射table
def get_bin_table(threshold=190):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table


# 去除干扰线算法
def depoint(img):  # input: gray image
    '''去除图片噪点'''
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:
                count = count + 1
            if pixdata[x, y + 1] > 245:
                count = count + 1
            if pixdata[x - 1, y] > 245:
                count = count + 1
            if pixdata[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                pixdata[x, y] = 255
    return img


# 打开图片
image = Image.open('/Users/mac/Learn/LearnPython/imgs/2.png')

# 转化为灰度图
img = image.convert('L')

# 把图片变成二值图像。
img1 = binarizing(img, 190)

# img2=depoint(img1)

# 显示转换后的图片
img1.show()

table = get_bin_table()
out = img1.point(table, '1')

# 将图片内容转换成string
code = pytesseract.image_to_string(img1)
print "识别该验证码是:" + str(code)
