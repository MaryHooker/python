# Escape Sequences

# using backslash + t (\t) to insert a tab in front of the content
tabby_cat = "\tI'm tabbed in."
# using \n to start content on new line
persian_cat = "I'm split\non a line."
# using \\ will render a single backslash (\)
backslash_cat = "I'm \\ a \\ cat."
# using three double-quotes and \t to be able to list multiple lines as well as indent each new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Additional Escape Sequences

# carriage return (\r)
carriage_return = "Heyyo\ru!"

print(carriage_return)
