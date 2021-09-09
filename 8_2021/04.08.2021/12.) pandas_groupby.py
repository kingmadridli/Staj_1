import pandas as pd
import numpy as np



personeller = {
    "Çalışan" : ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    "Departman" : ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","Bilgi İşlem"],
    "Yaş" : [30,25,45,50,23,34,42],
    "Semt" : ["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    "Maaş" : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller,index=[1,2,3,4,5,6,7])
result = df
result = df["Maaş"].sum()

result = df.groupby("Departman")
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name,group in df.groupby("Semt"):
#     print(name)
#     print(group)

# for name,group in df.groupby("Departman"):
#     print(name)
#     print(group)


# result = df.groupby("Semt").get_group("Kadıköy")
result = df.groupby("Departman").get_group("Muhasebe")

result = df.groupby("Departman").sum()
result = df.groupby("Departman").mean()
result = df.groupby("Departman")["Maaş"].mean()
result = df.groupby("Semt").groups
result = df.groupby("Semt").mean()
result = df.groupby("Semt")["Yaş"].mean()
result = df.groupby("Semt")["Çalışan"].count()  # Her semtte kaç adet çalışan var
result = df.groupby("Departman")["Yaş"].max()   # Her departmanda maksimum kaç yaş var
result = df.groupby("Departman")["Maaş"].max()
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]


result = df.groupby("Departman").agg(np.mean)     # Bunlar Aynı  (aggrigation)
# result = df.groupby("Departman").mean()


# Agg fonksiyonuna birden fazla parametre verebiliriz.

# result = df.groupby("Departman")["Maaş"].agg(np.sum,np.mean,np.max,np.min)
result  =df.groupby("Departman")["Maaş"].agg(np.max).loc["Muhasebe"]






print(result)