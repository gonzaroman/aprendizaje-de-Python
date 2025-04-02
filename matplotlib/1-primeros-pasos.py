#primero hay que instalalro
# pip install matplotlib

import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([0, 6 , 9, 12])
ypoints = np.array([0, 250, 150, 350])

plt.plot(xpoints, ypoints, 'o')
plt.show()