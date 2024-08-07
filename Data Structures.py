# Create a list of numbers and find the sum of all elements.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print("Sum:", total)


# Create a list of colors and print each color.
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

count = 0
while count < 5:
    print(count)
    count += 1

# Create a dictionary to store information about a book and print the values.
book = {
    "title": "Python Programming",
    "author": "John Doe",
    "year": 2020
}

print("Title:", book["title"])
print("Author:", book["author"])
print("Year:", book["year"])


# Create a dictionary to store student names and their grades. Print each student and their grade
grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C"
}

for student, grade in grades.items():
    print(f"{student}: {grade}")


# Create a tuple to store coordinates of a point and print the coordinates.
coordinates = (10, 20)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Create a tuple to store names of fruits and print each fruit.
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)


# Create a set of numbers and add a new number to the set.
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # Outputs: {1, 2, 3, 4}


# Create a set of colors and remove a color from the set.
colors = {"red", "green", "blue"}
colors.remove("green")
print(colors)  # Outputs: {'red', 'blue'}
