# coding=UTF-8
import string
import random

# 激活码中的字符和数字
field = string.letters + string.digits

print field
print random.sample(field, 4)


# 获得n个数字和字母的随机组合
def getRandom():
    n = 4
    return "".join(random.sample(field, n))


# 生成每个激活码有几组序列
def concatenate(grape):
    return "-".join([getRandom() for i in range(grape)])


# 生成x个激活码
def genarate(x):
    return [concatenate(4) for i in range(x)]


if __name__ == '__main__':
    print genarate(10)
