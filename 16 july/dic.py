color={"col2":"Red","col1":"Blue","col3":"Green"}
print(color)
for key in sorted(color):#to sort and then access all value after sorting
    print("%s:%s"%(key,color[key]))
