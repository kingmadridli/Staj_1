import pandas as pd

# pandas is used for dataframes


dict_1 = {
        "NAME":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }

data_frame_1 = pd.DataFrame(dict_1)            # Creating a dataframe using dict_1
print(data_frame_1)

head_data_frame = data_frame_1.head(2)         # returns first x row 
print(head_data_frame)


tail_data_frame = data_frame_1.tail(3)         # returns last x row
print(tail_data_frame)
