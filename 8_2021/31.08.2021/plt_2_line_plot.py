import pandas as pd
import matplotlib.pyplot as plt


df_1 = pd.read_csv("Matplotlib\iris.csv")

# print(df_1.columns)  # ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']

df = df_1.drop("Id",axis=1)


df_setosa = df_1[df_1.Species == "Iris-setosa"]
df_versicolor = df_1[df_1.Species == "Iris-versicolor"]
df_virginica = df_1[df_1["Species"] == "Iris-virginica"]


plt.plot(df_setosa.Id,df_setosa.PetalLengthCm,color = "red",label = "Setosa")
plt.plot(df_versicolor.Id,df_versicolor["PetalLengthCm"],color = "blue",label ="Versicolor" ) 
plt.plot(df_virginica.Id,df_virginica.PetalLengthCm,color = "yellow",label = "Virginica")
plt.grid()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend() # Ne çizdiğimizi görmemizi sağlar
plt.show()