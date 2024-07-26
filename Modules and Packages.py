# # Write a program that uses the random module to generate a random number between 1 and 10.
# import random
# print(random.randint(1, 10))


# # Creating and Importing Your Own Module
# # Create a module with a function that returns a greeting message. Import and use this function in another script.
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import zoomi
print(zoomi.greeting("Alice"))


# # Creating and Using a Package
# # Create a package with two modules. Each module should have a function that returns a different greeting message. Import and use these functions in another script.
# # mypackage/module1.py
# def greet():
#     return "Hello from module1!"

# # mypackage/module2.py
# def greet():
#     return "Hello from module2!"

# # main.py
# from mypackage import module1, module2
# print(module1.greet())
# print(module2.greet())

