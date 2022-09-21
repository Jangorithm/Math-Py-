import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plotVectors(vecs, cols, alpha=1):

    plt.figure()
    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                  alpha=alpha)

red = 'r'
blue = 'b'
green = 'g'

plotVectors([[1/np.sqrt(3**2), 3], [-1, 1],[2,1]], [red, blue,green])
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
