import numpy as np
a = np.arange(15).reshape(3, 5).transpose() + 1
print a
print('-------------')
b = a[1:4:2]
print b
