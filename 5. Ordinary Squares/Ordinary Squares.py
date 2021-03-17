import numpy as np
n, p = [int(x) for x in input().split()]
list_X = []
for i in range(n):
    list_X.append([float(x) for x in input().split()])
X = np.array(list_X)
list_y = [float(x) for x in input().split()]
y = np.array(list_y)
Xt = np.transpose(X)
XtX = np.dot(Xt, X)
Xty = np.dot(Xt, y)
beta = np.linalg.solve(XtX, Xty).round(2)
print(beta)
