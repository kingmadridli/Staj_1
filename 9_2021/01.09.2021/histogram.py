import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")
# print(df.info())
print(df.columns)


df.Speed.plot(kind = "hist",bins = 50,figsize = (12,12))
plt.show()
plt.clf() # Çizilen plotu temizler


