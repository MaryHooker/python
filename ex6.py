# Strings & Text

# initializing a variable and giving it the value of 10
types_of_people = 10
# setting variable x to be equal to an f-string that includes the property established above
x = f"There are {types_of_people} types of people."
# initializing variable and assigning a string value
binary = "binary"setting it equal to a
# initializing variable and assigning a string value
do_not = "don't"
# calling both variables inside an f-string
y = f"Those who know {binary} and those who {do_not}."
# return value of x
print(x)
# return value of y
print(y)
# return value of x inside f-string
print(f"I said: {x}")
# return value of y inside f-string
print(f"I also said: '{y}'")
# setting the property hilarious to be False
hilarious = False
# setting variable equal to a string with empty curly braces in order to be able to apply a format onto an already created string
joke_evaluation = "Isn't that joke so funny?! {}"
# return variable joke_evaluation and call the format method to input the hilarious variable into the string
print(joke_evaluation.format(hilarious))
#initializing variable
w = "This is the left side of..."
#initializing variable
e = "a string with a right side."
#return concatonated variable strings
print(w + e)
