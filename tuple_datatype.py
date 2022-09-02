tuple1=(1,2,3)
print("\ntype(tuple1) :",type(tuple1))

#*****************************************************************
a= 1,2,3,4,5
print("\nline 5- type(a) :",type(a))
#but with single variable
b=1
print("\nline 8- type(b) :",type(b))
c=1,
print("\nline 10- type(c) :",type(c))
"""
line 4- type(a) : <class 'tuple'>
line 7- type(b) : <class 'int'>
line 9- type(c) : <class 'tuple'>
"""
#*******************************************************************

tuple2=(1,2,3,True,(1,2,4),[6,7,8],{1:2,3:5},6.7)
print("\nline 18 -tuple2[0]", tuple2[0])
print("line 19 -tuple2[3]",tuple2[3])
print("line 20 -tuple2[4]",tuple2[4])
print("line 21 -tuple2[4][1]",tuple2[4][1])
print("line 22 -tuple2[4][-1]",tuple2[4][-1])

""" 
Tuple  is immutable i.e we can not make any changes in tuple
tuple2[4]="list"
print(tuple2)
#TypeError: 'tuple' object does not support item assignment """

#**********************************************************
newvar=list(tuple2)
print(newvar) #[1, 2, 3, True, (1, 2, 4), [6, 7, 8], {1: 2, 3: 5}, 6.7]
newvar[4]="list"
print("\n")
print(type(newvar),"\nline 33- newvar: ",newvar) #[1, 2, 3, True, 'list', [6, 7, 8], {1: 2, 3: 5}, 6.7]

tuple3=tuple(newvar)
print(type(tuple3),"\nline 36- tuple3: ",tuple3)

#note: in tuple true consider True as number 1 and  Flase as 0
# because true is boolean representation of 1 and 0 is false in python

"""count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value."""
 #**********************************************************************

tuple5=(1,2,3,True,(1,2,4),[6,7,8],{1:2,3:5},6.7 ,1,8,9, True,False)
print("\nline 47- tuple5.count(1):",tuple5.count(1))
#tuple5.count(1): 4  it check only number 1 and True 
print("line 49- tuple5.count(1):",tuple5.count(0))
#tuple5.count(1): 1

print("line 52- tuple5.count(2):",tuple5.count(2))
print("line 53- tuple5.count(6.7):",tuple5.count(6.7))
print("line 54- tuple5.count(True):",tuple5.count(True))
print("line 55- tuple5.count(Flase):",tuple5.count(False))

print("\nline 57- tuple5.index(1):",tuple5.index(1))
print("line 58- tuple5.index(1,1,):",tuple5.index(1,1,)) # getting next index of 1  that is True
print("line 59- tuple5.index(1,4,):",tuple5.index(1,4,))
#print("line 60- tuple5.index(1,4,7):",tuple5.index(1,4,7))
"""
line 57- tuple5.index(1): 0
line 58- tuple5.index(1,1,): 3
line 59- tuple5.index(1,4,): 8
# print("line 60- tuple5.index(1,4,7):",tuple5.index(1,4,7))
ValueError: tuple.index(x): x not in tuple
"""
print(tuple5)
for e in tuple5:
    print("\nline 75- ",e)
print(tuple5)
for i in range(len(tuple5)):
    print("\nline 77 -" ,tuple5[i])

gool=[(1,2),(3,4),(4,5),(5,6)]
for i in gool:
     print("\n line 83- ", i)
     for v in i:
        print("\n line 86-", v)
# if tuple has two elements then only we can iterate two variable but its more than two it wont work
for x,y in gool:
    print("\nline 88- ", x,y)

list1=[[1,2],[2,3],[4,5]]
for a,b in list1:
    print("\nline 92- ", a,b)

list1=[[1,2,3],[2,3,4],[4,5,8]]
for a,b,c in list1:
    print("\nline 96- ", a,b,c)

dic = {1:"a", 2:"b", 3:"c"}
print (type(dic))

for c ,d in dic.items():
    print("\nline 102- ", c,d)



# Assignment 
no_dic=4
input_list=[]
b=1
for i in range(no_dic):
    x=100*i+1
    y=x+100
    input_list.append((x,y))
    b+=1
print("\n line 115- ",input_list)

result_list=[]
#range_limits=[(1,101),(201,301),(301,401)]
for x,y in input_list:
    b= 1
    dict = {} 
    for a in range(x,y): 
        if (a%2 == 0 ):
            dict.update({b:a}) 
            b+=1
    result_list.append(dict)
print ("\nline 127- result_list\n",result_list)
    
#*******************************************************