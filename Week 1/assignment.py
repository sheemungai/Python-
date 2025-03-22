num1=int(input ("enter a number"))
num2 = int(input("enter another number"))
operator=input("Enter an operator(+,-,*,/)")

if operator == '+':
 result = num1 + num2
elif operator == '-':
  result = num1 - num2   
elif operator == '*':
  result = num1 * num2
elif operator == '/':
  result = num1 / num2
else:
  result="Invalid Syntax"
print(f"{num1} {operator} {num2} = {result}")