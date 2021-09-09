import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]

result = numbers[-1]

result = numbers[0:3]

result = numbers[:3]

result = numbers[3:]

result = numbers[::]

result = numbers[::-1]

result = numbers[::-2]

numbers_2 = np.array([[0,5,10],[15,20,25],[50,75,85]])

result = numbers_2[0]

result = numbers_2[2]

result = numbers_2[0,2] 

result = numbers_2[2,1]


# Bütün satırlar arasından index numarası 2 olan  sütünü döndür
result = numbers_2[:,2]
# Bütün sütünlar arasından index nuamrası 1 olan satırı döndür
result = numbers_2[1,:]


# Bütün satırları seç ve index numarası 0 ile 2 arasında olan sütünları döndür 
result = numbers_2[:,0:2]
# sondan 1 satırdaki tüm sütünü geriye döndür.
result = numbers_2[-1,:]


# Dizi bize olduğu  gibi gelir.
result = numbers_2[:3,:3]
result = numbers_2[::]


# İlk 2 satırın 2 ilk 2 sütünün geriye gönder
result = numbers_2[0:2,0:2]
result = numbers_2[:2,:2]


# print(numbers_2) 

# print("-"*30)

# print(result)



arr_1 = np.arange(0,10)
# arr_2 = arr_1   # referans    ==> Bellekteki adresleri aynı
arr_2 = arr_1.copy()     # ==>  Farklı bir adreste tanımlanır.




arr_2[0] = 20
# Bu değişiklik arr_1 i de etkiler


print(arr_1)
print(arr_2)




