import pandas as pd


dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)
print(data_frame_1)


print("*"*50)


data_frame_1["new_feature"] = [each*2 for each in data_frame_1.Age]
print(data_frame_1)


print("*"*50)

# transforming data
# apply()

def Multiply(age):
    return age*2

data_frame_1["appyl_feature"] = data_frame_1.Age.apply(Multiply)
print(data_frame_1)