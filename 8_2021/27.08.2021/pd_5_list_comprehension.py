import pandas as pd
import numpy as np

dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)


data_frame_1["Salary Grade"] = ["High" if each > data_frame_1.Salary.mean() else "Low" for each in data_frame_1.Salary]
print(data_frame_1)


# Sometimes we need to get lower all the columns name
print(data_frame_1.columns)
data_frame_1.columns = [ each.lower() for each in data_frame_1.columns]
print(data_frame_1.columns)


# Sometimes we need to fix columns name
data_frame_1.columns =  [each.replace(" ","_") for each in data_frame_1.columns]
print(data_frame_1.columns)
