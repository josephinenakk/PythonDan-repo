x = [] # empty list
b= 1
y={}
i=1
while i<=50: #loop 50 times
  j=1
  while j<=3: #loop 3 times
    
    if (j%2 == 0 ):
       y.update({i:i*j}) 
    #else:
        #y.update({i:i*j}) 
    j+=1
    if(i==50 and j==3):
        #print(y)
        print("")
  i+=1
  #print ("\n",x)
x.append(y)
#print("\n line-28",x[0])
#print(x)

y={}
m=1
while m<=50: #loop 50 times
  n=1
  while n<=3: #loop 3 times
    
    if (n%2 == 0 ):

       y.update({m:(m+50)*n}) 
    
    #else:
        #y.update({i:i*j}) 
    n+=1
    if(m==50 and n==3):
        #print(y)
        print("")
  m+=1
  #print ("\n",x)
x.append(y)
#print("\n line -39", x)

y={}
j=1
while j<=50: #loop 50 times
  k=1
  while k<=3: #loop 3 times
    
    if (k%2 == 0 ):

       y.update({j:(j+100)*k}) 
    
    #else:
        #y.update({i:i*j}) 
    k+=1
    if(j==50 and k==3):
        #print(y)
        print("")
  j+=1
  #print ("\n",x)
x.append(y)

print(x)