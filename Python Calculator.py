#code by Elis Clarke
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
def squareroot(x):
    return math.sqrt(x)

print("Operation list.")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Square root")

while True:
    num1_is_Float = False
    num2_is_Float = False
    operation = input("Which operation would you like to perform? 1, 2, 3, 4 or 5?: ")
    if operation in ('1', '2', '3', '4'):
        while (num1_is_Float == False):
            try:
                num1 = float(input("Enter the first number: "))
            except Exception:
                print("Invalid Entry")
            else: 
                num1_is_Float = True
                
        while (num2_is_Float == False):
            try:
                num2 = float(input("Enter the second number: "))
            except Exception:
                print("Invalid Entry")
            else: 
                num2_is_Float = True
                
        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == '4':
            if num2 == 0:
                print("Anything divided by 0 is infinity.")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
    
        new_calc = input("Do you want to do another calculation? (yes/no): ")
        if new_calc == "no":
            break
            
        num1_is_Float = False
        num2_is_Float = False
    
    elif operation == '5':
        while (num1_is_Float == False):
            try:
                num1 = float(input("Enter the number: "))
            except Exception:
                print("Invalid Entry")
            else: 
                num1_is_Float = True
    
        print("Squareroot", num1, "=", squareroot(num1))
    
        new_calc = input("Do you want to do another calculation? (yes/no): ")
        if new_calc == "no":
            break
            
        num1_is_Float = False
        num2_is_Float = False
    
    else:
        print("Invalid Input")