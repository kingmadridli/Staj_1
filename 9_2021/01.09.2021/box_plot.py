import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Box Plot


df = pd.read_csv("pokemon.csv")
print(df.columns)

df.boxplot(column="Attack",by="Legendary")
plt.show()