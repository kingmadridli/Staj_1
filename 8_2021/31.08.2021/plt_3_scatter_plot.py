import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv("Matplotlib\iris.csv")

df_2 = df_1.drop("Id",axis=1)


df_setosa = df_1[df_1.Species == "Iris-setosa"]
df_versiolor = df_1[df_1.Species == "Iris-versicolor"]
df_virginica = df_1[df_1.Species == "Iris-virginica"]

plt.scatter(df_setosa.PetalLengthCm,df_setosa.PetalWidthCm,color = "red",label = "Setosa")
plt.scatter(df_versiolor.PetalLengthCm,df_versiolor.PetalWidthCm,color = "blue",label = "Versicolor")
plt.scatter(df_virginica.PetalLengthCm,df_virginica.PetalWidthCm,color = "yellow",label = "Virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.grid()
plt.legend()
plt.show()