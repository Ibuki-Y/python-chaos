import numpy as np
import matplotlib.pyplot as plt


def logistic(a):
    x = [0.001]
    for i in range(1000):
        x.append(a * x[-1] * (1 - x[-1]))
    return x[-100:]


for a in np.arange(2.0, 4.0, 0.0001):
    x = logistic(a)
    plt.plot([a]*len(x), x, "c.", markersize=0.1)

plt.show()
