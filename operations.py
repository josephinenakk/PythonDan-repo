"""
PERFORM ON  ALL BELOW OPERATIONS ON   INTEGER, FLOAT, STRING, LIST.

A. Arithmetic operators : +, -, *,  **, /, %, //  
B. Assignment operators  :  =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
C. Comparison operators  : ==, != , > , < , >=, <=
D. Logical operators    :  and, or, not        
F. Identity operators   :  is, is not
G. Membership operators :  in, not in
H. Bitwise operators    :  & ,| ,^ ,>> ,<<
"""

################################################################################

# A. Arithmetic operators: +, -, *,  **, /, %, //. 

print("\n A. Operators ***************************************************************************")
# 1. Addition: +
a = 2+3
print("\n 1. Addtion of 2+3 (from line 16 ) =",a,)

#2.Subtraction: -
b=9-7
print("\n 2. Subtraction of 9-7 (from line 20 )=",b)

#3.Multiplication: *
c=3*4
print("\n 3. Multiplication of 3*4 (from line 24)=",c)

#4.Exponentiation :** (power of)
d=3**3
print("\n 4. Exponentiation of 3**3 (from line 28)=",d)

#5.Division: / ,the result of Division result contains 1.quotient and 2.remainder
e=12.5/4
print("\n 5. Division of 12.5/4 (from line 32)=",e)

#6.Modulus: %, gives you remaider ( or reminder+ decimal ) if a=12 is divided by b=4, and the remainder is returns zero
f=12%4
print("\n 6.a Modulus of 12%4 (from line 36)=",f ) 
g=12.4%4
print("\n 6.b Modulus of 12.4%4 (from line 38) =",g ) 
h=13.4%4
print("\n 6.c Modulus of 13.4%4 (from line 40) =",h ) 

#7. Floor division :\\ 
"""The result of regular division is 15/4=3.75, but using  floored 3.75 down to 3.
The result of regular division is always a float, 
where as if one of the operands is a float in floor division, then the output will be a float.
"""

print("\n 7.a Regular division, this is a float (from line 48) =", 15/ 2)
print("\n 7.b Floor division, this is an int (from line 49) =", 15 // 4)
print("\n 7.c Floor division, this is a float (from line 50) =", 15.0 // 4)

###################################################################################

# B. Part-1 Assignment operators  :  =, +=, -=, *=, /=, %=, **=,  //=, &=, |=, ^=, >>=, <<=
print("\n B. Part-1 Assignment operators ***************************************************************************")
print("\n Line 53 -Assignment Operators")
#1. Equals: = 
a=5
print("\n line 57- Assignment operators =", a)

#2. Add AND: adds the given value to the variable and stores in same variable 
b =6
b += 4  # that is to b thats 6 add 4 and results store in b 
print("\n line 67- Answer for Add AND operator +=:", b )

#3. Subtract AND: Subtract  the given value to the variable and stores in same variable 
c =6
c -= 4  # that is to c thats 6 subtract 4 and results store in c
print("\n line 72- Answer for Subtract AND operator -=:", c )


#4. Multiply AND: Multiply the given value to the variable and stores in same variable 
d =6
d *= 4  # that is to c thats 6 Multiply 4 and results store in d
print("\n line 78- Answer for Multiply AND operator *=:", d)

#5. Divide AND: Divide  the given value to the variable and stores in same variable 
e =6
e /= 4  # that is to c thats 6 Divide  4 and results store in e
print("\n line 83- Answer for Divide AND operator /=:", e)

#5. Modulus AND: Modulus the given values to the variable and stores in same variable 
f =6
f %= 4  # that is to c thats 6 Modulus  4 and results store in f
print("\n line 83- Answer for Modulus AND operator /=:", f)

#6. Exponent AND: Exponent the given value to the variable and stores in same variable 
g =6
g **= 4  # that is to c thats 6 Exponent  4 and results store in f
print("\n line 93- Answer for Exponent AND operator **=:", g)

#6.  Floor Division AND: Floor Division of the given values to the variable and stores in same variable 
h =6
h //= 4  # that is to c thats 6 Floor Division 4 and results store in h
print("\n line 98- Answer for Floor Division AND operator **=:", h)

# H. Bitwise operators    :  &, | ,^ ,>> ,<<
"""
Bitwise operators are used to compare (binary) numbers:

Operator	Name	                Description
&           AND	                    Sets each bit to 1 if both bits are 1
|	        OR	                    Sets each bit to 1 if one of two bits is 1
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
~ 	        NOT	                    if A is given intiger number  then ~A is equal to -(A+1).
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""
print("\n H. Bitwise operators ***************************************************************************")
#1. Bitwise AND Operator & , Sets each bit to 1 if both bits are 1
print("\n line 116- Result of (10&7)=",10 & 7 )
             #####    8 4 2 1   #####
# binary of 10     =  1 0 1 0
# binary of 10     =  0 1 1 1
# result of (10&7) =  0 0 1 0 = 2.

#2. Bitwise OR Operator | , Sets each bit to 1 if one of two bits is 1
print("\n line 123- Result of (10|7)=",10 | 7 )
             #####    8 4 2 1   #####
# binary of 10     =  1 0 1 0
# binary of 10     =  0 1 1 1
# result of (10&7) =  1 1 1 1 = 15.

#3. Bitwise xOR Operator ^ , Sets each bit to 1 if only one of two bits is 1
print("\n line 130- Result of (10^7)=",10 ^ 7 )
             #####    8 4 2 1   #####
# binary of 10     =  1 0 1 0
# binary of 10     =  0 1 1 1
# result of (10&7) =  1 1 0 1 = 13.

#4. Bitwise NOT Operator ~ ,A then ~A is equal to -(A+1).
print("\n line 137- Result of (~10)=",~10 )
             #####    8 4 2 1   #####
# binary of 10     =  1 0 1 0
# result of (~10)  =  -(10+1) =  -11

#5. Bitwise Zero fill left shift Operator << ,In a<< x means add x number of zero at end of given binary number a
x=2
print("\n line 144- Result of (10<<2)=",a << x)
             #####  32 16 8 4 2 1   #####
# binary of 10   =        1 0 1 0
#                    1  0 1 0 0 0   << x means add x number of zero at end of given binary number a
# result of (10<<7)= 1  0 1 0 0 0 = 32+8 =40


#6. Bitwise Signed right shift	 Operator >> , in a >> x means add x number of zero at begininig of given binary number a
a=10
x=2
print("\n line 154- Result of (10<<2)=",a >> x)
             #####   8 4 2 1   #####
# binary of 10   =   1 0 1 0
#                    0 0 1 0 0 0   >> x means add x number of zero at begininig of given binary number a
# result of (10<<7)= 0 0 1 0 = 2 

################################################################################################

# B. Part-2 Bitwise Assignment operators :  &=, |=, ^=, >>=, <<=
print("\n B. Part-2 Assignment operators ***************************************************************************")

#7. Bitwise AND and Assign &=: 
# This operator is used to perform Bitwise AND on both operands and then assigning the result to the left operand.
a = 3   # 0 0 1 1
b = 5   # 0 1 0 1
a &= b  # 0 0 0 1  , a = a & b result is 1
print("\n line 169- Bitwise AND and Assign 3 &= 5 =",a)
  
#8. Bitwise OR and Assign |=: 
# This operator is used to perform Bitwise OR on the operands and then assigning result to the left operand.
a = 3   # 0 0 1 1
b = 5   # 0 1 0 1
a |= b  # 0 1 1 1  , a = a | b result is 7
print("\n line 176- Bitwise OR and Assign  3 |= 5 =",a)

#9. Bitwise xOR and Assign ^=: 
# This operator is used to perform Bitwise XOR on the operands and then assigning result to the left operand.
a = 3   # 0 0 1 1
b = 5   # 0 1 0 1
a ^= b  # 0 1 1 0  , a = a ^ b result is 6
print("\n line 183- Bitwise xOR and Assign 3 ^= 5 =",a)

#9. Bitwise Right Shift and Assign >>=: 
# This operator is used to perform Bitwise right shift on the operands and then assigning result to the left operand.
a = 5  # 0 1 0 1
b = 2  
a >>= b  # 0 0 0 1 0 1  , a = a >> b result is 1 ( add  number of zeros of second number in fornt of fist number then rmove last digits)
print("\n line 190- Bitwise Right Shift and Assign 5 >>= 2 =",a)

#10. Bitwise Left Shift and Assign <<=: 
# This operator is used to perform Bitwise left shift on the operands and then assigning result to the left operand.
a = 5  # 0 1 0 1
b = 2  
a <<= b  #  0 1 0 1 0 0 , a = a >> b result is 16+4 ( add  number of zeros of second number at last of fist number)
print("\n line 197- Bitwise Left Shift and Assign 5 <<= 2 =",a)

###############################################################################################

# C. Comparison operators  : ==, != , > , < , >=, <=
print("\n C. Comparison operators ***************************************************************************")
#1. Equals To operator == :
# The equal to operator (==) compares two values and returns True if the left value is equal to the right value.
a=4
b=4
print("\n line 207- Equals To operator 4 == 4",a==b)

#2. Not Equals To operator != :
#The not equal to operator (!=) compares two values and returns True if the left value isn’t equal to the right value.
a=4
b=4
print("\n line 214- Not Equals To operator 4 != 4",a!=b)

#3. Greater than  operator(>)
#The greater than operator (>) compares two values and returns True if the left value is greater than the right value.
a=5
b=4
print("\n line 220- Greater than  operator 5 > 4 = ", a>b)

#4. Less Than operator (<)
#The Less Than operator (<) compares two values and returns True if the value on the left is less than the value on the right
a=5
b=4
print("\n line 226- Less Than operator r 5 < 4 = ", a<b)

#5. Less than or equal to operator (<=)
#The less than or equal to operator compares two values and returns True if the left value is less than or equal to the right value
a=5
b=4
print("\n line 232- Less than or equal to operator 5 <= 4 = ", a<=b)
print("\n line 233- Less than or equal to operator 4 <= 4 = ", b<=b)
print("\n line 224- Less than or equal to operator 4 <= 5 = ", b<=a)

#6. Greater Than or Equal To operator (>=)
#The greater than or equal to operator (>=) compares two values and returns True if the left value is greater than or equal to the right value.
a=5
b=4
print("\n line 240- Greater Than or Equal To operato 5 >= 4 = ", a>=b)
print("\n line 241- Greater Than or Equal To operato 5 >= 5 = ", a>=a)
print("\n line 241- Greater Than or Equal To operato 5 >= 5 = ", b>=a)

###################################################################################################################################

#D. Logical operators  :  and, or, not 

#1. The and operator :
# The and operator checks whether two conditions are both True simultaneously:
a = 10
print("\n line 251- The and operator a < 11 and a > 9 =",  a < 11 and a > 9 )
print("\n line 251- The and operator a < 11 and a > 9 =",  a < 11 and a > 10 )


#2.The or operator :
#The or operator checks multiple conditions. But it returns True when either or both of individual conditions are True:
a = 10
print("\n line 258- The or operator a > 11 or a > 10 =",  a > 11 or a > 10 )
print("\n line 259- The or operator a > 11 or a > 10 =",  a > 11 or a == 10 )

#3. The not operator
#The not operator applies to one condition. And it reverses the result of that condition, True becomes False and False becomes True.
a = 12
print("\n line 264- The not operator not a > 11  =", not a > 11 )
print("\n line 265- The not operator not a > 11  =", not a < 11 )

#######################################################################################################################################

#F. Identity operators   :  is, is not

#1. is Identity operators :
x = ["joe", "dan"]
y = ["joe", "dan"]
z = x

print("\n line 276- is Identity operators =" ,x is z)   # returns True because z is the same object as x

print("\n line 278- is Identity operators =" ,x is y)   # returns False because x is not the same object as y, even if they have the same content

print("\n line 280- == operator =" ,x == y)   # the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#2.is not Identity operators:
x = ["cell", "phone"]
y = ["cell", "phone"]
z = x
print("\n line 286- is not Identity operators =" ,x is not z) # returns False because z is the same object as x
print("\n line 287- is not Identity operators =",x is not y) # returns True because x is not the same object as y, even if they have the same content
print("\n line 288- Not eaquals to =",x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

###########################################################################################################################################

#G. Membership operators :  in, not in

#1. in Membership operators :
x = ["pot", "bat"]
print('\n line 296- in Membership operators "bat" in ["pot", "bat"]  =',"bat" in x) # returns True because a sequence with the value "bat" is in the list

#2. not in Membership operators :
x = ["pot", "bat"]
print('\n line 300- not in Membership operators "cup" in ["pot", "bat"]  =',"cup" in x) # returns True because a sequence with the value "cup" is not in the list

























