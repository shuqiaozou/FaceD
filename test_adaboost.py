import math


def test_exp(a, y, g1, w):
    return w * (math.exp(-a * y * g1))


z1 = test_exp(0.4236, 1, 1, 0.1)
z2 = test_exp(0.4236, 1, 1, 0.1)
z3 = test_exp(0.4236, 1, 1, 0.1)
z4 = test_exp(0.4236, -1, -1, 0.1)
z5 = test_exp(0.4236, -1, -1, 0.1)
z6 = test_exp(0.4236, -1, -1, 0.1)
z7 = test_exp(0.4236, 1, -1, 0.1)
z8 = test_exp(0.4236, 1, -1, 0.1)
z9 = test_exp(0.4236, 1, -1, 0.1)
z10 = test_exp(0.4236, -1, -1, 0.1)

Z = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10

print(Z, z1 / Z, z2 / Z, z7 / Z)
print z1, z7
