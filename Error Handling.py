# # Write a program that catches a ZeroDivisionError when attempting to divide by zero.
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # Write a program that catches a ValueError when attempting to convert a string to an integer.
# try:
#     number = int("abc")
# except ValueError:
#     print("Could not convert string to integer")

# # Write a program that catches both ValueError and ZeroDivisionError.
# try:
#     result = 10 / 0
#     number = int("abc")
# except ValueError:
#     print("ValueError: Could not convert string to integer")
# except ZeroDivisionError:
#     print("ZeroDivisionError: You can't divide by zero")

# #Write a program that catches any exception and prints a generic error message.
# try:
#     result = 10 / 0
# except Exception as e:
#     print(f"An error occurred: {e}")


# # Write a program that uses a finally block to print a message after attempting to divide by zero.
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# finally:
#     print("This will always be executed")


# # Write a function that raises a ValueError if the input age is less than 18.
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18 or above")
#     return True

# try:
#     check_age(16)
# except ValueError as e:
#     print(e)


