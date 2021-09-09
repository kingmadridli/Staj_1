import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv("Matplotlib\iris.csv")

df_2 = df_1.drop("Id",axis=1)


df_setosa = df_1[df_1.Species == "Iris-setosa"]
df_versiolor = df_1[df_1.Species == "Iris-versicolor"]
df_virginica = df_1[df_1.Species == "Iris-virginica"]


plt.subplot(3,1,1)   # 2 tane, 1.nin 1.'si 
plt.plot(df_setosa.Id,df_setosa.PetalLengthCm,color = "red",label = "Setosa")
plt.ylabel("Setosa - PetalLengthCm")

plt.subplot(3,1,2)   # 2 tane, 1.nin 2.'si 
plt.plot(df_versiolor.Id,df_versiolor.PetalLengthCm,color = "blue",label = "Versicolor")
plt.ylabel("Versicolor - PetalLengthCm")

plt.subplot(3,1,3)   # 2 tane, 1.nin 3.'si 
plt.plot(df_virginica.Id,df_virginica.PetalLengthCm,color = "yellow",label = "Virginica")
plt.ylabel("Virginica - PetalLengthCm")

plt.show()