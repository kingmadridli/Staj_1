import pandas as pd

df_1 = pd.read_csv("Matplotlib\iris.csv")

# print(df_1.columns)  # ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']

print(df_1.Species.unique())

print(df_1)

print(df_1.describe())

setosa = df_1[df_1.Species == "Iris-setosa"]
versicolor = df_1[df_1.Species == "Iris-versicolor"]
print(setosa.describe())
print(versicolor.describe())