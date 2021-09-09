import pandas as pd
from pandas.io.parsers import read_csv
df = pd.read_csv("IMDB.csv")

# Sorular

# 1.) Dosya hakkındaki Bilgiler
result = df
result = df.columns
result = df.info()

# 2.) İlk 5 kaydı gösterin 
result = df.head()

# 3.) ilk 10 kaydı gösterin
result = df.head(10)

# 4.) Son 5 kaydı gösterin
result = df.tail()

# 5.) Son 10 kaydı gösterin
result = df.tail(10)

# 6.) Sadece Movie_title kolonunu alın
result = df["Title"]

# 7.) Sadece Movie_title kolonunu içeren ilk 5 kaydı alın
result = df["Title"].head()

# 8.) Sadece Movie_title ve Rating  kolonunu içeren ilk 5 kaydı alın
result = df[["Title","Rated"]].head()

# 9.) Sadece Movie_title ve Rating  kolonunu içeren son 7 kaydı alın
result = df[["Title","Rated"]].tail(7)

# 10.) Sadece Movie_title ve Rating  kolonunu içeren ikinci 5 kaydı alın
result  = df[["Title","Rated"]][5:10]

# 11.) Sadece Movie_title ve Rating  kolonunu içeren 2 saatten uzun olan kayıtlardan ilk 50 tanesini alınız.
result = df[df["Runtime"] > 120][["Title","Rated","Runtime"]].head(50)


# 12.) Yayın tarihi 2014 ve 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df["Year"] >= 2014) & (df["Year"] < 2016)]["Title"]

print(result)