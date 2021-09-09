import pandas as pd


dict_1 = {
        "Name":["Ali","Veli","Kenan","Hilal","Ayşe","Evren"],
        "Age":[15,16,17,33,45,66],
        "Salary":[100,150,240,350,110,220]
        }


data_frame_1 = pd.DataFrame(dict_1)


# Showing existing columns

print(data_frame_1["Name"])    # Shows Name Column
print(data_frame_1["Age"]) 
print(data_frame_1["Salary"])

print("*"*40)    # Or

print(data_frame_1.Name)
print(data_frame_1.Age)
print(data_frame_1.Salary)

print("*"*40)    # Or

print(data_frame_1.loc[:,"Name"])
print(data_frame_1.loc[:,"Age"])        # location = loc
print(data_frame_1.loc[:,"Salary"])


print("*"*40)



# Indexing

print(data_frame_1.loc[:3,"Age"])          # in list and numpy, the value 3 is exklusive but in pandas inklusive 

print(data_frame_1.loc[0:2,"Name":"Salary"])   # Show the columns from Age to Salary

print(data_frame_1.loc[0:3,["Name","Salary"]])  # Show the columns Age and Salary

print(data_frame_1.loc[::-1,:])    # Show the all columns by reversing the rows


print("*"*40)

# These are Same
print(data_frame_1.loc[:,"Age"])  # Show all rows up to "Age" column
print(data_frame_1.iloc[:,1])     # iloc = integer location

# iloc uses the numbers instead of columns' name



# Adding New Columns
data_frame_1["New Column"] = [-1,-2,-3,-4,-5,-6]