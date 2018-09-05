# declaring a variable to a number.
types_of_people = 10
# setting a format string to a variable.
x = f"There are {types_of_people} types of people."

# setting a variable to a string.
binary = "binary"
# setting a variable to a string.
do_not = "don't"
#setting a format string to a variable.
y = f"Those who know {binary} and those who {do_not}."

# printing variable (which is a format string).
print(x)
print(y)

# printing a format string which includes a variable of a format string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# setting a variable to 'False'. I also ended the line with a semi-colon so show that it doesn't matter.
hilarious = "No, it's not funny... but it is clever";
# setting a variable which will include a format to be added later.
joke_evaluation = "Isn't that joke so funny?! {}"

# making a variable to hold a string with a format string variable added.
z = joke_evaluation.format(hilarious)

# printing a variable.
print(z)

# setting a string to a variable.
w = "This is the left side of..."
e = "a string with a right side."

# using print to concatonate two strings together.
print(w + e, "And this is a variable of a format string with a variable:", z)
