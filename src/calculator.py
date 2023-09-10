import time
import os
os.system('title Calculator')
def calculating():
    number1 = input("Enter first number : ")
    operator = input("enter the operator ('+-/*') : ")
    number2 = input("Enter the second number : ")
    number = "1234567890"
    if number1 and number2 in number:
        if operator not in "+-/*":
            print("Program stopped\nreason : incorrect operator")
            time.sleep(2)
            os.system('cls')    
        elif operator == "+":
            result = int(number1) + int(number2)
            print(result)
            time.sleep(2)
            os.system('cls')            
        elif operator == "-":
            result = int(number1) - int(number2)
            print(int(result)) 
            time.sleep(2)
            os.system('cls')            
        elif operator == "*":
            result = int(number1) * int(number2)
            print(int(result)) 
            time.sleep(2)
            os.system('cls')            
        elif operator == "/":
            result = int(number1) / int(number2)
            print(int(result))    
            time.sleep(2)
            os.system('cls')
    else:
        print("Program stopped\nreason : must enter a number")
        time.sleep(2)
        os.system('cls')

while 1:
        c = input("start program? (y/n) : ")    
        if c.lower() == "y":    
            os.system("cls")
            calculating()
        else:
            os.system("cls")
            break          

