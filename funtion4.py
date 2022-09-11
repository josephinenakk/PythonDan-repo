"""
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
line 13 factorial of 7 =  5040
line 22  factorial of 7 =  5040
"""
y=[]
def fun2(a):
    for i in range(a,0,-1):
        y.append(i)
    print(y)
fun2(10)

def factorial(n):
   if n == 1:
      return n
   else:
    return (n*factorial(n-1))
num=7
print("line 13 factorial of 7 = ",factorial(num))

res=1
def factorial1(res,l):
    res*=l
    l-=1
    if (l>0):
       factorial1(res,l)
       if(l==1):
        print("line 22  factorial of 7 = ",res)
factorial1(res,7)   