import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = np.cos(x)
plt.plot(x, y, 'k-')
plt.title("y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
