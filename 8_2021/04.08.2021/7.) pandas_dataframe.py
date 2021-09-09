import pandas as pd

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])

# data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
# df = pd.DataFrame(data, columns=["Name","Note"], index=[1,2,3,4], dtype=float)

list =  [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name" : ["Ahmet","Ali","Yağmur","Çınar"],"Note" : [50,60,70,80]}
# df = pd.DataFrame(dict,index=[1,2,3,4])
dict_list = [
    {"Name":"Ahmet","Note":50},
    {"Name":"Ali","Note":60},
    {"Name":"Yağmur","Note":70},
    {"Name":"Çınar","Note":80}
]
df = pd.DataFrame(dict_list, [1,2,3,4],dtype=float)

print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)

# df = pd.DataFrame(data)

# print(df)

