#1. Write program to get result below
# [ 
    # {1:2,2:4,3:6 ........ 49:98},
    # {1:102,2:104,3:106 ........ 49:198},
    # {1:202,2:204,3:206 ........ 49:298}
# ]
y={}
index1=1
index2=1
index3=1
list1=[{},{},{}]
for i in range(1,100):
    if( i%2 != 0):
        continue
    y.update({index1:i})
    index1 +=1
list1[0].update(y)
#print("\n",x)
for i in range(100,200):
    if(i%2 != 0):
        continue
    y.update({index2:i})
    index2 +=1
list1[1].update(y)
#print("\n",list1)
for i in range(200,300):
    if(i%2 != 0):
        continue
    y.update({index3:i})
    index3 +=1
list1[2].update(y)
print(list1)

