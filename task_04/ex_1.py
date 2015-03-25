import numpy as np
import matplotlib.pyplot as pl
g = np.genfromtxt("input.txt", dtype = [float, float, float, float, float, float, float, float, float, float, float, int],
names = ['M2AB', 'M2AC', 'XA', 'XB', 'XC', 'Y1', 'Y2', 'Y3', 'Y4', 'W', 'PMIN', 'ID'], delimiter = '\t', skiprows = 1)
x = [i[0] for i in g]
fig = pl.figure()
pl.subplots_adjust(wspace = 0.3)
pl.subplot(1, 2, 2)
pl.hist(x, bins = 30, histtype = 'step', range = (0, 0.5))
y, binEdges = np.histogram(x, bins = 30, range = (0, 0.5))
bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])
menStd = np.sqrt(y)
pl.bar(bincenters, y, width = 0, color = 'w', edgecolor = 'w', ecolor = 'r', yerr=menStd)
pl.xlabel("M2AB")
pl.ylabel("N")
pl.subplot(1, 2, 1)
pl.hist(x, bins = 30, histtype = 'step')
pl.show()
