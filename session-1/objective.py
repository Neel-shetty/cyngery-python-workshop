import os
import time


def getnums():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    return num1, num2


def addnums():
    try:
        num1, num2 = getnums()
        print(f"Addition of {num1} and {num2} is {num1 + num2}")
    except:
        print("Enter Valid numbers")


def subnums():
    try:
        num1, num2 = getnums()
        print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
    except:
        print("Enter Valid numbers")


def mulnums():
    try:
        num1, num2 = getnums()
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    except:
        print("Enter Valid numbers")


def divnums():
    try:
        num1, num2 = getnums()
        quotient, remainder = divmod(num1, num2)
        print(
            f"Division of {num1} and {num2} is {quotient} with remainder of {remainder}")
    except:
        print("Enter Valid numbers")


def checkOperations():
    for operation_name in AVAILABLE_OPERATIONS:
        if operation_name not in OPERATIONS_MAP.keys():
            return False
    return True


def menu():
    while True:
        os.system("cls")
        print("\t\tDemo Calculator")
        print("Available operations")
        for i in range(len(AVAILABLE_OPERATIONS)):
            print(i+1, ".", AVAILABLE_OPERATIONS[i])
        try:
            choice = int(input("Enter Your choice number: "))
            choice -= 1
        except:
            print("Enter valid option number")
            time.sleep(4)
            continue
        if 0 <= choice < len(AVAILABLE_OPERATIONS):
            operationName = AVAILABLE_OPERATIONS[choice]
            operation = OPERATIONS_MAP.get(operationName)
            operation()
            print("\n")
            time.sleep(2)
        else:
            print("Enter valid option number")
            time.sleep(4)


AVAILABLE_OPERATIONS = ["Add", "Subtract", "Multiply", "Divide", "Quit"]
OPERATIONS_MAP = {"Add": addnums, "Subtract": subnums,
                  "Multiply": mulnums, "Divide": divnums, "Quit": quit}

if __name__ == "__main__":
    if checkOperations == False:
        print("Warning NOT ALL operation names are mapped to their functions")
    menu()
