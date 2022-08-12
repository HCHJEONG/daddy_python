import pandas as pd
import numpy as np


y = np.array([[1,1,2,2,3,3],[4,4,5,5,6,6]])
print(y)
print(y[1][2])


z = pd.DataFrame(y, index=['one', 'two'], columns=list('abcdef'))
print(z)
print()
print(z['b'])