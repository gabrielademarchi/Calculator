from unittest import result
from art import logo
import os


def clear(): return os.system('cls')


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1*num2


def divide(num1, num2):
    return num1/num2


possibilites = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    for key in possibilites:
        print(key)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calc_function = possibilites[operation]
        result = calc_function(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        continue_operation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if continue_operation == "y":
            first_number = result
        else:
            should_continue = False
            clear()
            calculator()


calculator()
