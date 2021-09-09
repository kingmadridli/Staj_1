import numpy as np


arr_1  = np.array([1,2,3])
arr_2 = np.array([4,5,6])


# Basic Operations
print(arr_1 + arr_2)
print(arr_1 - arr_2)
print(arr_1 ** arr_2)

print("*"*40)

print(np.sin(arr_1))    # Her bir indexin  sinus değerlerini alır
print(np.cos(arr_1))    # Her bir indexin  cosinus değerlerini alır
print(np.tan(arr_1))    # Her bir indexin  tanjant değerlerini alır


print(arr_1<2)          # arr_1 içindeki indisleri 2 den küçük olup olmadığını return eder.


print("*"*40)


# Element wise product
array_1 = np.array([[1,2,3],[4,5,6]])
array_2 = np.array([[1,2,3],[4,5,6]])

print(array_1*array_2)      # Her indisi kendi içinde çarpar 

print("*"*40)

# Matris product
# array_1.dot(array_2)      # array_1 x array_2   ==> Hata verir (2,3) x (2,3) çarpılamaz


# lets first get transpose of array_2
array_2 = array_2.T
print(array_2.shape)      #  array_2 is  3 x 2  matris

print(array_1.dot(array_2))   # Matris product


print("*"*40)


# Exponansiyel
print(np.exp(array_1))    # Her bir indis e^x şeklinde çarpıldı

print("*"*40)

# Create Random Matris
random_matris = np.random.random((5,5))      # 0-1 aralığında
print(random_matris)


print("*"*40)

# Some Operations
print(random_matris.sum())  
print(random_matris.max())
print(random_matris.min())

print("*"*20)

print(random_matris.sum(axis=0))   #   Her sütünü topla
print(random_matris.sum(axis=1))   #   Her satırı topla

print("*"*20)

print(np.sqrt(array_1))    
print(np.square(array_1))

print("*"*20)

print(np.add(array_1,array_1))       #   print(arr_1 + arr_1)







