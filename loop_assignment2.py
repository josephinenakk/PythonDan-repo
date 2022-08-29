even_numbers_dict = {}
index_variable = 1
even_numbers = []

a = 1
    
for i in range(1,300):
    if ( i%2 != 0):
        continue
    
    #print(i,index_variable)
    #even_numbers[a] = even_numbers_dict.update({index_variable:i})
    a +=1
    #index_variable +=1
    
#print (even_numbers_dict)

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

