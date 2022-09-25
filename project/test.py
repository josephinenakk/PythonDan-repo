
"""d = {}

size = int(input("Enter the size of nested dictionary: "))

for i in range(size):
    dict_name = input("Enter the name of child dictionary: ")

    d[dict_name] = {}
    Name = input("Enter name: ")
    Age = input("Enter Age: ")
    d[dict_name]["Name"] = Name
    d[dict_name]["Age"] = Age

print(d)"""
"""
####2. progrm
d = {}
c={}
las=1
def add():
    global las
    name=input("enter name:")
    c.update({las:{name}})
    print(c)
    if (las<5):
         las+=1
         add()

add()

enter name:joe
{1: {'joe'}}
enter name:joe
{1: {'joe'}, 2: {'joe'}}
enter name:j
{1: {'joe'}, 2: {'joe'}, 3: {'j'}}
enter name:l
{1: {'joe'}, 2: {'joe'}, 3: {'j'}, 4: {'l'}}
enter name:l
{1: {'joe'}, 2: {'joe'}, 3: {'j'}, 4: {'l'}, 5: {'l'}}
"""


def add():
    add.var = "x"
def sub():
    print(add.var)
add()
sub()


