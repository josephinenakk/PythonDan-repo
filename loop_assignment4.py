#1. Write program to get result below using nested_while loop.
""" [{1:2,2:4,3:6 ........ 49:98},
    {1:100,2:104,3:106 ........ 49:198},
    {1:200,2:204,3:206 ........ 49:298}  ] """

x = [] # empty list
b= 1
y={}
i=1
while i<=50: #loop 50 times
  j=1
  while j<=3: #loop 3 times
    if (j%2 == 0 ):
       y.update({i:i*j}) 
    j+=1
    if(i==50 and j==3): 
        x.append(y)
  i+=1
  
y={}
m=1
while m<=50: #loop 50 times
  n=1
  while n<=3: #loop 3 times
    if (n%2 == 0 ):
       y.update({m:(m+50)*n}) 
    n+=1
    if(m==50 and n==3):  
        x.append(y)
  m+=1
  

y={}
j=1
while j<=50: #loop 50 times
  k=1
  while k<=3: #loop 3 times
    if (k%2 == 0 ):
       y.update({j:(j+100)*k}) 
    k+=1
    if(j==50 and k==3):
        x.append(y)
  j+=1
print(x)
