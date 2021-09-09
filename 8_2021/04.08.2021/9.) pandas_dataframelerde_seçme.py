import  pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

# result =  df

result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]


# loc["row","column"]  ==> loc["row"] ,  loc[":","column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.iloc[2]  # 2. indexe karşılık gelen seri



result = df.loc[:,"Column1"]
result = df.loc[:,["Column1","Column2"]]

result = df.loc[:,"Column1":"Column2"]   # Column1 den Column3 de kadar
result = df.loc[:,:"Column2"]
result = df.loc[:,"Column2":]
result = df.loc["A":"B",:"Column2"]

result = df.loc["A","Column2"]
result = df.loc["C","Column1"]
result = df.loc[["A","B"],"Column1"]


df["Column4"] = pd.Series(randn(3),["A","B","C"])   # Yeni sütun ekleme
df["Column5"] = df["Column1"] + df["Column3"]

print(df.drop("Column5",axis=1))   # COlumn5  silinir ancak orjinal dataframede değişiklik olmaz.
print(df)
# print(df.drop("Column5",axis=1,inplace=True))  #  ==> Orjinal versiyonu değiştirmek için 


# print(result)