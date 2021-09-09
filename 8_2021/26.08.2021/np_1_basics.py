import numpy as np


arr_1 = np.array([1,2,3,4,5,6])   # vektör oluşturma  

print(arr_1.shape)  #    tip inceleme  (6,)  4x1 lik bir vektör
print(arr_1.ndim)   #    Boyut  = 1 Boyutlu vektör

print("*"*20)

matris = arr_1.reshape(3,2)   # 3x2 lik bir matris oluşturduk
print(matris)
print(matris.shape)
print(matris.ndim)      # 2 boyutlu 

print("datatype = ",matris.dtype)     #   int32
print("Size = ",matris.size)       # Size = 6
print("type = ",type(matris))      # type =  <class 'numpy.ndarray'>


print("*"*40)


# # reshape metodu kullanmadan biçimlendirme
arr_2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])    
print(arr_2)
print(arr_2.shape)

print("*"*20)

# Zero Matris
zero_matris = np.zeros((3,4))   # 3x4 lük 0 matris oluşturmuş olduk
print(zero_matris)               # ==>  Yer ayırtmak için kullanılır, daha sonra veri eklenebilir.

print("*"*20)

# Indis Değiştirme
zero_matris[0,0] = 5   #   (0,0) elemanına 5 ata
print(zero_matris)               

print("*"*20)

# Birim Matris
once_matris = np.ones((2,3))
print(once_matris)

print("*"*20)

# Boş Matris
empty_matris = np.empty((2,5))
print(empty_matris)


print("*"*40)



# Aralıklı Sayı yazdırma

numbers_1 = np.arange(10,50,5)        # 10-50 arasına    5 ER    atlatarak yazdır   ( 50 Hariç ) 
print(numbers_1)    

numbers_2 = np.linspace(10,50,10)     # 10-50 arasına    10 TANE    sayı yaz        ( 50 Dahil )
print(numbers_2)  

