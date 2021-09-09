import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


x = np.array([1,2,3,4,5,6,7])
y = x*2 + 5

plt.bar(x,y)
plt.xlabel("a")
plt.ylabel("y")
plt.show()

