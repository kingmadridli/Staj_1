import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon.csv")
# print(df.info())
print(df.columns)


# Scatter Plot

df.plot(kind  ="scatter",x = "Attack", y = "Defense",alpha = 0.5,color = "red")
# plt.scatter(df.Attack,df.Defense,color = "red",alpha = 0.5) 
# dataframe i görselleştireceğim, türü scatter olsun, x ekseni attack olsun,y ekseni defense olsun
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack Defense Scatter Plot")
plt.show()