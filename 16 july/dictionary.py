color={"col1":"Red","col2":"Blue","col3":"Green"}#dictionary is created 
print(color)#values as key:value
print(type(color))
color={"col1":"Red","col2":"Blue","col2":"Green"}
print(color)#if name of two key is same then value is get overwrited
d=dict()#empty dictionary
d={}#empty dictionary
print(d)
d[100]="001"
d[200]="Apple"#to update value in emty dictionary
d[300]="Cat"#dictionary_name[key]=value
print(d)
#d.has_key(400) #it is not working in python 3 works in python2
if 400 in d:
    print("Yes")
    print(d[400])
for x in color:
    print(x) #to access the key of the dictionary
    print(color[x])#to access the key and value of dictionary
del color["col2"]#delete particular key of the dictionary
print(color)
