import numpy as np
import matplotlib.pyplot as pl

file = np.genfromtxt("cb2_winds.txt", dtype=float, usecols=(0,1))
file2 = np.genfromtxt("cb2_winds.txt", dtype=float, usecols=(0,2))
print(file)
y = file[:,0]
x = file[:,1]
print(file2)

y2 = file2[:,0]
x2 = file2[:,1]

figplot = pl.figure(figsize=(6,3))

axes1 = figplot.add_subplot(1,2,1)
axes2 = figplot.add_subplot(1,2,2)

axes1.set_ylabel('u (m/s)')
axes1.set_xlabel('lat (pc)')
axes1.plot(y,x, '--b')

axes2.set_ylabel('u (m^2/s^2)')
axes2.set_xlabel('lat (pc)')
axes2.plot(y2,x2, '--g')

pl.show()