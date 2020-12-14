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
carriage_return = "Hey yo\ru!"
print(carriage_return)

# back space (\b)
# outcome "Heyyou!"
back_space = "Hey \byou!"
print(back_space)

# form feed (\f)
# returns hey you on seperate lines
form_feed = "Hey \fyou!"
print(form_feed)

# vertical tab
vertical_tab = "Hey \vyou!"
print(vertical_tab)

# horizontal tab
horizontal_tab = "Hey \vyou!"
print(horizontal_tab)
