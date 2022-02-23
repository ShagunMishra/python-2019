car_dict={
    "Brand":"Tata",
    "Model":"Safari",
    "Year":2016
    }
print(car_dict)
car_dict["Year"]=2019#to change the value of particular key
print(car_dict)
car_dict["Engine Type"]="Diesel"#to add key and value
print(car_dict)
car_dict.update({"Color":"Silver"})#to update key and value
print(car_dict)
print(len(car_dict)) #to find length of dictionary
car_dict.pop("Model")
print(car_dict)#to remove particular item in dictionary
del car_dict["Year"]#to remove particular item
print(car_dict)
car_dict.clear()#to empty whole dictionary
print(car_dict)
del car_dict#to delete whole dictionary
# print(car_dict) #error because car_dict is no more exist
