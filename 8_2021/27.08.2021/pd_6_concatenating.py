import pandas as pd


dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)

# Adding Columns
data_frame_1["new_feature"] = [-1,-2,-3,-4,-5,-6]
print(data_frame_1)
print("We added a new columns")


# Dropping
data_frame_1.drop(["new_feature"],axis=1)
print(data_frame_1)
print("we dropped it but there werent any differences")
# In this situation there is no changing to see

# we can do this
data_frame_1 = data_frame_1.drop(["new_feature"],axis=1)
print(data_frame_1)
print("Here we dropped it manually")


# or we can do this
data_frame_1["new_feature"] = [-1,-2,-3,-4,-5,-6]
data_frame_1.drop("new_feature",axis=1,inplace=True)   # These are same direcitons
print(data_frame_1)
print("Thats the right one")



print("*"*50)


# Stacking 
data_1 = data_frame_1.head(5)
data_2 = data_frame_1.tail(5)

vertical_concantenate = pd.concat([data_1,data_2],axis=0)    # Vertical  ==> axis=0
print(vertical_concantenate)  

salary = data_frame_1.Salary
age = data_frame_1.Age 

horizontal_concatenate = pd.concat([salary,age],axis=1)    # Horizontal  ==> axis=1
print(horizontal_concatenate)