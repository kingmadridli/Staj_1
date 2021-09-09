import numpy as np


#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

print("-"*30)

# Çok boyutlu bir python listesi
py_multi = [[1,2,3],[4,5,6],[7,8,9]]

# Çok boyutlu bir numpy dizisi
np_multi = np_array.reshape(3,3)
# ==> [3,3] bir matris oluşturmuş oluyoruz.


print(py_multi)
print(np_multi)

print("-"*30)

# Oluşturmuş olduğumuz numpy dizilerinin boyutlarına bakıcak olursak
print(np_array.ndim)
print(np_multi.ndim) 

print("-"*30)

# Oluşturmuş olduğumuz numpy dizilerinin şekillerine bakıcak olursak
print(np_array.shape)
print(np_multi.shape)