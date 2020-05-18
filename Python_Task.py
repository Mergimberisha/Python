# Define the following variables
# name, last_name, age, eye_color, hair_color
name = "Mergim"
last_name = "Berisha"
eye_color = "Brown"
hair_color = "Black"
age = "20"
# Prompt user for input and Re-assign these

name = input("What is your name?  ")
print(name)

last_name = input("What is your last name?  ")
print(last_name)

eye_color = input("What is your eye color?  ")
print(eye_color)

hair_color = input("What is your hair color?  ")
print(hair_color)

age = input("What is your age?  ")
print(age)


# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

print("Hello " + name + " " + last_name + "! Welcome, your age is " + age + ", your eyes are " + eye_color + " and your hair color is " + hair_color + ".")

# Section 2 - Calculate in what year was the person born? and respond back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

year_born = 2020 - int(age)

print("You said you were " + str(age) + " hence you were born in " + str(year_born))

# Extra - Cast your input
