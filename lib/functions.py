#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Guido"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    if name == "programmer":
        print(f"Hello, {name}!")
    else:
        print("Hello, Guido!")

def add(num1, num2):
    return num1 + num2
    

def halve(number):
    return number / 2
