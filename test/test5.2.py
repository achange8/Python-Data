# 要素の間の距離を求める
import numpy as np

data = [
    [0, 1],
    [1, 0],
    [2, 3],
    [5, 3],
    [5, 5],
]

pdata = np.array(data)
N, L = np.shape(pdata)
for n in range(N):
    for m in range(N):
        distance = np.sqrt(
            np.square(pdata[n, 0] - pdata[m, 0]) + np.square(pdata[n, 1]-pdata[m, 1]))
        print("%8.4f" % distance, end="")
    print()
