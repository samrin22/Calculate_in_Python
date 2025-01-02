def add(X,Y):
    return X+Y
def sub(X,Y):
    return X-Y
def mul(X,Y):
    return X*Y
def div(X,Y):
    return X/Y
print("Please select the operation. ")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Division")
choice=input("Please enter choice: ")
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
if choice=='a':
    print(num1,"+", num2,"=", add(num1, num2))
elif choice=='b':
    print(num1,"-", num2,"=", sub(num1, num2))
elif choice=='c':
    print(num1,"*", num2,"=", mul(num1, num2))
elif choice=='d':
    print(num1,"/", num2,"=", div(num1, num2))
else:
    print("This is an invalid input")

                          
               
