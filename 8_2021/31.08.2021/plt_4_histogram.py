import pandas as pd
import matplotlib.pyplot as plt

df_1 = pd.read_csv("Matplotlib\iris.csv")

df_setosa = df_1[df_1.Species == "Iris-setosa"]
df_versiolor = df_1[df_1.Species == "Iris-versicolor"]
df_virginica = df_1[df_1.Species == "Iris-virginica"]

plt.hist(df_setosa.PetalLengthCm,bins=30)   # PetalLengthCm değerleriini count eder
plt.xlabel("PetallengthCm")
plt.ylabel("Frekans")
plt.legend()
plt.title("Histogram")
plt.grid()
plt.show()
