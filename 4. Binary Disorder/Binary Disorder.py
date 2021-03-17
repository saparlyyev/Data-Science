import numpy as np
from sklearn.metrics import confusion_matrix
y_true = [float(x) for x in input().split()]
y_pred = [float(x) for x in input().split()]
matrix = confusion_matrix(y_true, y_pred, labels=[1, 0]).T
end_matrix = np.round(matrix, 1).astype(float)
print(end_matrix)
