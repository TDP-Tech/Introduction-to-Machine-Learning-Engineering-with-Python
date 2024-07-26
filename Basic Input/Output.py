# Write a program that asks the user for their name and age and then prints a message with that information.
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")


# Write a program that asks the user for a message and writes it to a file.
message = input("Enter a message: ")
with open("message.txt", "w") as file:
    file.write(message)
print("Message written to message.txt")

# Write a program that reads and prints the content of a file.
with open("message.txt", "r") as file:
    contents = file.read()
    print(contents)

# Write a program that appends a new message to an existing file.
new_message = input("Enter a new message to append: ")
with open("message.txt", "a") as file:
    file.write("\n" + new_message)
print("Message appended to message.txt")


