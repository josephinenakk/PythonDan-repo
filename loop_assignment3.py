#1. Write program to get result below
# using nested_forloop
# [ 
    # {1:2,2:4,3:6 ........ 49:98},
    # {1:102,2:104,3:106 ........ 49:198},
    # {1:202,2:204,3:206 ........ 49:298}
# ]


x = [] # empty string
b= 1
for i in range(0,3): # getting one by one 0 ,1,2
    y = {}           #empty dect
    x.append(y)      #[{},{},{}]
    if (i < 1):      # i=0
       index= 1        
    else:
        index = i*100+1 #i= 1,2 (101, 201)
    for a in range(index,100+index): #(101,201)  (201,301)
        if (a%2 != 0 ):
            continue
        y.update({b:a}) 
        b+=1
    x[i] = y
print (x)