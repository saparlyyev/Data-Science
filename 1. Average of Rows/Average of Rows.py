import numpy as np
n, p = [int(x) for x in input().split()]
matrix = []
for i in range(n):
    matrix.append(input().split())
x = np.array(matrix).astype(float)
z = (x.sum(axis = 1))/p
y = np.round(z, 2)
print(y)