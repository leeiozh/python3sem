# import numpy as np
#
# x, y = map(int, input().split())
#
# map = np.zeros(shape=(x, y), dtype=np.int64)
#
# for i in range(x):
#     map[i, :] = np.fromstring(input(), sep=" ")
#
# print(np.sum((map < -5)))
# print(int(-np.sum(map[map < 0])))
# print(int(np.max(map)))

import numpy as np

a = np.loadtxt(input())
b = np.loadtxt(input())
x = np.fromstring(input(), sep=" ")

print(np.dot(np.dot(np.dot(a, a), x), b))
