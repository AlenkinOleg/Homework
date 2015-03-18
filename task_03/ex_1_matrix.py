import numpy as np
import matplotlib.pyplot as plt
matrix = np.random.rand(40, 40)
plt.imshow(matrix, cmap=plt.cm.gray)    
plt.colorbar() 
plt.show()
