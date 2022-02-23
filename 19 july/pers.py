class person:
    def __init__(myself,age,name):#name of reference variable may be change
        myself.age=age
        myself.name=name
    def myfun(abc):#we can give name whatever we want
        print("My name is:",abc.name)
a=person(23,"Rohan")
a.myfun()
