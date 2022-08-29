y=[]
for i in range(100):
    if( i%2 == 0):
        continue
    #print(i)
    y.append(i)
print('\n',y)

y=[]
for i in range(100):
    if( i%2 != 0):
        continue
    #print(i)
    y.append(i)
print('\n', y)

y={}
index1=1
for i in range(100,200):
    if( i%2 != 0):
        continue
    y.update({index1:i})
    index1 +=1
print("\n",y)