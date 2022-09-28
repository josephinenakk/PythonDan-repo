from unittest import result


class Calculator:
    # default method-  this method is going to be called on object creation
    # init constructor which accepts some arguments
    result = 100   # Class variable
    def __init__(self,op1,op2):
        self.op1 = (int(input("Enter a number : ")))
        self.op2 = (int(input("Enter a number : ")))
    def add(self):
        return self.op1+self.op2
    def sub(self):
        return self.op1-self.op2
    def mul(self):
        return self.op1*self.op2
    def div(self):
        return self.op1/self.op2

#1.class variables
print(Calculator.result)
#2. assigning differnt value to class variable result
Calculator.result=200
print(Calculator.result)

#3. creating first instance
calc_1 = Calculator(1,2)

print (calc_1,type(calc_1))

print(calc_1.add())
print(calc_1.sub())
print(calc_1.mul())
print(calc_1.div())
print(Calculator.result)

#4. creating second instance
calc_2 = Calculator(1,2)
print (calc_2,type(calc_2))
print(calc_2.add())
print(calc_2.sub())
print(calc_2.mul())
print(calc_2.div())