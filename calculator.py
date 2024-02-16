#addition
def add(num1,num2):
   return num1+num2;

#subtraction
def subtract(num1,num2):
   return num1-num2;

#multiplication
def multiply(num1,num2):
   return num1*num2;

#division
def divide(num1,num2):
   return num1/num2;

#operation to be done 
print("enter any number to perform operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

#Taking inputs 
operator=input()
num1=int(input("enter a number"))
num2=int(input("enter a number"))

#writing a if-else blocks for performing the operation
if(operator=="1"):
   sum=add(num1,num2)
   print("The sum is:",(float(sum)))

elif(operator=="2"):
    sub=subtract(num1,num2)
    print("The difference is:",(float(sub)))

elif(operator=="3"):
   mul=multiply(num1,num2)
   print("The product is:",(float(mul)))

elif(operator=="4"):
   div=divide(num1,num2)
   print("The division is:",(float(div)))

else:
  print("Invalid! Enter a valid operator")
