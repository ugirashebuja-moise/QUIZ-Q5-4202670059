a= float(input("Enter the value of your first number: "))
b = float(input("Enter the value of your second number: "))
add = a + b
subtract = a - b
multiply = a * b
if b == 0:
    divide = "Error! can not divide by zero."
else:
    divide = a / b
print("\nResults:")
print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)