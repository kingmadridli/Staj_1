import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns
result = df.head(10)  # İlk 10 kayıt
result = df.tail(6)  # Son 6  kayıt
result = df["Column1"].head()     #kolon1 ilk 5 kayıt
result = df[["Column1","Column2"]].tail(3)
result = df[5:15][["Column3","Column4"]].head() 


# Filtreleme İşlemi

result = df > 50  # True ya da False bilgisi girilir.
result = df[df > 50]    
result = df[df %2== 0]  # Çift olanları gösterir.
result = df["Column1"] > 50
result = df[df["Column1"] > 50]   # Column1 50 den büyük olan bütün satırları göster 
result = df[df["Column1"] > 50 ]["Column3"]
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]["Column1"].head(10)   # And operatörü
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)][["Column1","Column2"]].head(10)   
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)][["Column1","Column2"]].head(10)    # Or Operatörü

result = df.query("Column1 >= 50 & Column1 %2 == 0")["Column1"]
result = df.query("Column1 >= 50 | Column1 %2 == 0")["Column1"]



print(result)
