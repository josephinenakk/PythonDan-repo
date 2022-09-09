"""
36
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
[4, 16, 64, 256, 1024]
"""

def sqaure_num(x):
    return(x*x)
sqaure=sqaure_num(6)
print(sqaure)

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
x=[]
def time_table():
    for i in range(1,13):  
        x.append(2*i)
    print(x)
time_table()

#[4, 16, 64, 256, 1024]
y=[]
z=4
def solution():
    for i in range(1,6):
        y. append(z**i)
    print(y)
solution()