# Asking Questions

# you use end='' to tell print to not end the line with a newline character and go to the next line
print("How old are you?", end='')
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# another way to use input in python

age = input("How old are you?")
print(age)

# getting a number from someone using input and converting it from a string into an integer so I can use the input to do math
x = int(input("Type a number: "))
print(x + 2)
