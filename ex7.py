# More Printing

print("Mary had a little lamb.")
# printing a string with empty curly braces followed by the format method and passing in 'snow' as the parameter to be displayed in the string
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
# this line prints out 10 periods because the string is being times by 10
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# concatonation of variable strings / providing a space to prevent the next print from staring on a new line
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# continued concatonation
print(end7 + end8 + end9 + end10 + end11 + end12)
