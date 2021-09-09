import pandas as pd


dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)           
print(data_frame_1)

print(data_frame_1.columns)        # Returns columns' name


print(data_frame_1.info())        
 # RangeIndex: 6 entries, 0 to 5,   Data columns (total 3 columns)

# dtypes: int64(2), object(1)     memory usage: 272.0+ bytes

# 0   Name    6 non-null      object(string)
# 1   Age     6 non-null      int64
# 2   Salary  6 non-null      int64

print(data_frame_1.dtypes)

# Name      object
# Age        int64
# Salary     int64
# dtype: object



print(data_frame_1.describe())      # returns only numeric features (age,salary)

#           Age        Salary
# count   6.000000    6.000000    Adet
# mean   32.000000  195.000000    Ortalama
# std    20.474374   94.815611    Standart devision
# min    15.000000  100.000000    Minimum
# 25%    16.250000  120.000000
# 50%    25.000000  185.000000
# 75%    42.000000  235.000000
# max    66.000000  350.000000     maximum