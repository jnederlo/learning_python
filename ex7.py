# printing a string.
print("Mary had a little lamb.")
# printing a string and adding a format string variable to the end.
print("Its fleece was white as {}.".format('snow'))
#printing a string.
print("And everywhere that Mary went.")
# multiplying a string by a number and printing that many instances of it.
print("." * 10) # what'd that do?

#setting variables to strings.
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
# strings are declared with either ' (single quotes), or " (double quotes), either works, but they have to match for each instance.
end11 = 'e'
end12 = "r"

# the comma at the end before 'end' indicated a seperate value to execute. The 'end' keyword is replacing the default \n at the end of the print to just a space ' '.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
