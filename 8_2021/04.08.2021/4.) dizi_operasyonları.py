import numpy as np
from numpy.core.fromnumeric import reshape

numbers_1 = np.random.randint(10,100,6)
numbers_2 = np.random.randint(10,100,6)

print(numbers_1)
print(numbers_2)
print("-"*30)



result = numbers_1 + numbers_2    # İki Dizinin Aynı indexteki elemanları toplanır.
result = numbers_1 + 10           # Her index 10 ile toplanır.
result = numbers_1 - numbers_2
result = numbers_1 - 10
result = numbers_1 * numbers_2    # Dizi elemanlarının her birini çarpar.
result = numbers_1 * 10
result = numbers_1 / 10

result = np.sin(numbers_1)        # Her bir elemenı ayrı ayrı sinus işlemine sokar 
result = np.cos(numbers_1)
result = np.sqrt(numbers_1)
result = np.log(numbers_1) 


multi_number_1 = numbers_1.reshape(2,3)
multi_number_2 = numbers_2.reshape(2,3)

# print(multi_number_1)
# print("-"*30)
# print(multi_number_2)
# print("-"*30)
  
result = np.vstack((multi_number_1,multi_number_2))     
# Bu iki matrisi dikey olarak birleştirir.
result = np.hstack((multi_number_1,multi_number_2))


result = numbers_1 >= 50
result = numbers_1 % 2 == 0



print(result)
print(numbers_1[result])


