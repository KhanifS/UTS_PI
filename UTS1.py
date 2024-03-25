import math

number = int(input("Enter a whole number: "))
result = round(number / 365, 11) 
print(f"Your monthly salary is: {result:.11f}")
