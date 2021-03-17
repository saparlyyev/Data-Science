import numpy as np
import pandas as pd
lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]
df = pd.Series(lst)
df_replaced = df.replace(np.NaN, df.mean())
y = np.round(df_replaced, 1)
print(y)