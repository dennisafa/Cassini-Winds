import numpy as np
import matplotlib.pyplot as pl

file = np.genfromtxt("cb2_winds.txt", dtype=float, usecols=(0,1))
print(file)
file.reshape(2,2)

pl.plot(file[0:], )
pl.show()