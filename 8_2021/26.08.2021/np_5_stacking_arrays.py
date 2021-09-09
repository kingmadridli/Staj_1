import numpy as np


arr_1 = np.array([[1,2],[3,4]])
arr_2 = np.array([[-1,-2],[-3,-4]])


# Vertical Stacking
arr_3 = np.vstack((arr_1,arr_2))
print(arr_3)

print("*"*40)

# Horizontal Stacking
arr_4 = np.hstack((arr_1,arr_2))
print(arr_4)


print("*"*40)