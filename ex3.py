print("I will now count my chickens:")
#this line first divides 30 by 6 which gives you 5 and then adds 5 to 25, giving you 30
print("Hens", 25 + 30 / 6)
#this line first first multiples 25 * 3 (75), then divides 4 into 75 and leaves the remainder of 3, and 100 - 3 gives you 97
print("Roosters", float(100 - 25 * 3 % 4))
#The float() method is used to return a floating point number from a number or a string.
print(float(97))
print("Now I will count the eggs:")
#this line first divides 4 by 2 leaving a remainder of 0, then 1 divided by 4 gives you .25
#now start back at the beginning adding 3, 2, and 1 which is 6, then -5 (1), 1 - .25 (.75), and finally .75 + 6, giving you 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")
# this statement is false because 5 is not less than -2
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
