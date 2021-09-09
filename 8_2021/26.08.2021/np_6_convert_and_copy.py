import numpy as np


liste = [1,2,3,4]
arr = np.array([1,2,3,4])   # already creating a list to define an array


# From list to array
arr_1 = np.array(liste) 
print(arr_1)    

# From array to list
list_1 = list(arr)
print(list_1)


print("*"*40)


a = np.array([1,2,3])    
b = a                     # 3 arrays created
c = a
print(a)
print(b)
print(c)

b[0] = 5                # first index of b is changed

print(a)
print(b)                # But all arrays are changed
print(c)

print("*"*40)

# Solution of this problem
d = np.array([1,2,3])
e = d.copy()              # Occupied a different place in memory this time
f = d.copy()
print(d)
print(e)
print(f)

e[0] = 5

print(d)
print(e)                # Just array e is changed
print(f)


