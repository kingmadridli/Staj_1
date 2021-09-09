import pandas as pd
from pandas.core.tools.datetimes import Scalar
import numpy as np


# numbers = [20,30,40,51]
# letters  = ["a","b","c","d"]
# # letters  = ["a","b","c",20]
# scalar = 5
# dictionary = {"a":10,"b":20,"c":30,"d":40}




# # pandas_series = pd.Series(numbers)
# # pandas_series = pd.Series(letters)
# # pandas_series = pd.Series(scalar,[0,1,2,3])
# # pandas_series = pd.Series(numbers,["a","b","c","d"])
# # pandas_series = pd.Series(dictionary)

# # random_numbers = np.random.randint(10,100,6)
# # pandas_series = pd.Series(random_numbers)

# pandas_series = pd.Series([20,30,40,51],["a","b","c","d"])
# result = pandas_series[0]
# result = pandas_series[-1]
# result = pandas_series[:2]
# result = pandas_series[-2:]
# result = pandas_series["a"]
# result = pandas_series[["a","d"]]
# # result = pandas_series[["a","d","e"]]
# result = pandas_series.ndim
# result = pandas_series.dtype
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.min()
# result = pandas_series + pandas_series
# result = pandas_series + 50
# result = np.sqrt(pandas_series)

# result = pandas_series >= 50
# result  = pandas_series %2 == 0






# # print(random_numbers)
# print(pandas_series)
# print(result)
# print(pandas_series[result])



#Opel Satış bilgileri :

opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total = opel2018 + opel2019

print(total)
print(total["astra"])
# print(total["combo"])    #  ==> Hata

