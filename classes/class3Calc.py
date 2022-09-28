class Calc:
    model = "Calci"

    def __init__(self,name):
        self.name = name
        Calc.model = "New one"
    

a = Calc("hello")
print (a.name) # hello
print (a.model) #New one

b = Calc("world")
b.model = "Calc"
print (b.name) #world"
print (b.model) #Calc
print (a.model) #New one
a.model="me"
print (a.model) #me

c = Calc("hai")
print (c.model) #New one