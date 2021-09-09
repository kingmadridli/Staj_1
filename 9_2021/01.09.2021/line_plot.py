import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("pokemon.csv")
# print(df)
# print(df.columns)
# print(df.info())
print(df.corr())



# Heatmap

# f,ax = plt.subplots(figsize = (18,18))
# sns.heatmap(df.corr(),annot=True,linewidths=5,fmt='.1f',ax = ax)
# plt.show()

# print(df.head())





# Line Plot

df.Speed.plot(kind ="line",color = "green",label = "Speed",linewidth = 1,alpha = 0.5,grid = True,linestyle = ":")
df.Defense.plot(color = "red",label = "Defense",linewidth = 1,alpha = 0.5,grid  =True,linestyle = "--")
plt.legend(loc = "upper right")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Plot")
plt.show()







