import numpy as np


# result = np.array([1,3,5,7,9])  ==> Bir dizi oluşturmak için uzun bir yol




# 1-10 arasında bir dizi oluşturmak için :
# result = np.arange(1,10)



# 3. bir parametre alırsa 
# result = np.arange(10,100,3)




# Sadece 0 dan oluşan biri dizi tanımlamak istersek  ==> 10 tane 0
# result = np.zeros(10)    
# result = np.ones(5)  



# aralık belirterek liste oluşturma    == 0-100 arasındaki sayıalrı 5 eşit parçaya bölerek geri döndürür.
# result = np.linspace(0,99,5)   


# Rastgele bir sayı üretmek için
# result = np.random.randint(0,10)
# result = np.random.randint(5,15,3)



# 0 ile 1 arasında x adet sayı üret
# result = np.random.rand(6)
# result = np.random.randn(6)         # ==> Neegatif değerler de dahildir.



# np_array = np.arange(50) 
# np_multi = np_array.reshape(5,10)      # ==> 5-10 luk bir matris
# print(np_multi.sum(axis=1))
# print(np_multi.sum(axis=0))





# dizideki max ve min değeri bulma
rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
print(type(rnd_numbers))
print(rnd_numbers.max())
print(rnd_numbers.min())

# Ortalama bulmak için 
# result = rnd_numbers.mean()

# Üretilen en büyük sayının index numarasını bulmak için
result = rnd_numbers.argmax()
# Üretilen en büyük sayının index numarasını bulmak için
result = rnd_numbers.argmin() 







print(result)


