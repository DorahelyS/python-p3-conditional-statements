#!/usr/bin/env python3

def admin_login(username, password):
    if ((username == "admin" or username == "ADMIN") and password == "12345"):
        return  "Access granted"
    else:
        return "Access denied"

'''
INCORRECT:
def admin_login(username, password):
    if ((username == "admin" or username == "ADMIN") and password == "12345"):
        return  "Access granted"
    elif:
        return "Access denied"

*if I try to do that way would need another condition after elif condition:
since I dont have another conition simply return can do it how I have it originally or:

def admin_login(username, password):
    if ((username == "admin" or username == "ADMIN") and password == "12345"):
        return  "Access granted"
    return "Access denied"

'''

def hows_the_weather(temperature):
    if (temperature < 40):
        return  "It's brisk out there!"
    elif (temperature >= 40 and temperature <= 65):
        return "It's a little chilly out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

'''
can also do it this way:
def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

    return "It's perfect out there!"
'''



def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0 ):
        return "Buzz"
    else:
        return num 

'''
CAN'T DO IT THIS WAY BECAUSE ORDER OD THE EVALUATION IS IMPORTANT:
By checking for multiples of both 3 and 5 (num % 3 == 0 and num % 5 == 0) first, we ensure that if a number is 
divisible by both 3 and 5, it will be correctly identified as "FizzBuzz" before checking for multiples of 3 or 5.
def fizzbuzz(num): 
    if (num % 3 == 0): 
        return "Fizz" 
    elif (num % 5 == 0 ): 
        return "Buzz" 
    elif (num % 3 == 0 and num % 5 == 0): 
        return "FizzBuzz"
    else: 
        return num

'''

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None
'''
To write the code using dictionary mapping, you can create a dictionary where the keys represent the operations and the values represent the corresponding functions. Each function will perform the desired operation on the given numbers. Here's an example:

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator(operation, num1, num2):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    if operation in operations:
        return operations[operation](num1, num2)
    else:
        print("Invalid operation!")
        return None

In this code, we define separate functions for each operation, and then create a dictionary called operations 
where the keys are the operation symbols and the values are the corresponding functions. Inside the calculator 
function, we check if the given operation is in the operations dictionary. If it is, we retrieve the corresponding
function using the operation as the key and call it with the given numbers. Otherwise, we print an error message 
and return None.


dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
    
'''
