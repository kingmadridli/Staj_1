import numpy as np


# Shape Manipulation

arr_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])


# to show this array like this  [1,2,3,4,5,6,7,8,9]
arr_2 = arr_1.ravel()
print(arr_2)

array_2 = arr_2.reshape(3,3)
print(array_2)

array_2_T = array_2.T
print(array_2_T)


print("*"*40)

array_3 = np.array([[1,2],[3,4],[5,6]])
print(array_3.reshape(2,3))   #  array_3 ü burada yeniden şekiilendirdik ancak array_3 aynı kaldı.
print(array_3)

print("*"*40)

print(array_3.resize(2,3))   # Burada resize() metodu ile array_3 değişmiş oldu
print(array_3)

