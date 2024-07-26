# Write a program to read and print the content of a file named sample.txt.
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Write a program to write "Hello, Python!" to a file named output.txt.
with open("output.txt", "w") as file:
    file.write("Hello, Python!\n")

# Write a program to append "Python is great!" to the file output.txt.
with open("output.txt", "a") as file:
    file.write("Python is great!\n")

# Write a program to read a file line by line and print each line.
with open("sample.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# Write a program to read all lines of a file into a list and print the list.
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

