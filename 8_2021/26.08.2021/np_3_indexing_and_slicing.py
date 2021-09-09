import numpy as np

arr_1 = np.array([1,2,3,4,5,6,7])

# Returning index 
print(arr_1[3])
print(arr_1[0:4])

# Reversing arrays
reverse_arr_1 = arr_1[::-1]    
print(reverse_arr_1)

print("*"*40)

array_1 = np.array([
                    [1,2,3,4,5],
                    [6,7,8,9,10]
                    ])

print(array_1[1][2])     # 1.satır 1. sütüna erişme   ==> 8

print(array_1[:,1])     # Satırlardan hepsini al ve 1. sütün al    [satır bilgileri,sütün bilgileri]
print(array_1[1,:])     # 1 .satırdaki bütün sütünlar
print(array_1[1,1:4])     # 1. satırdaki 1-4 arası sütünları göster   ==> [ 7 8 9 ]

print(array_1[-1,:])     # En son satırı göster  
print(array_1[:,-1])     # En son sütünü göster 
