import pandas as pd



dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)

# 2 ways to filter a dataframe

# 1.) 

# We define filters
filter_1 = data_frame_1.Salary > 200
filter_2 = data_frame_1.Age < 20

# we create filtered data
created_data_1 = data_frame_1[filter_1]
created_data_2 = data_frame_1[filter_2]

print(created_data_1)
print(created_data_2)

# Then we combine 
print(data_frame_1[filter_1 & filter_2])
# or
print(data_frame_1[filter_1][filter_2])    # recommend





print("*"*50)




# 2.)

# We can finish it in one line
print(data_frame_1[data_frame_1.Age < 20][data_frame_1.Salary > 200])