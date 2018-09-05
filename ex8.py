# setting a varaible as a string that will include 4 substitutions. Substitutions are identified by '{}'.
formatter = "{} {} {} {}"

# .format is a function --format()-- which indicates that 'formatter' is a format string and will contain some substitutions which are seperated by the commas.
print(formatter.format(1, 2, 3, 4))
# the format string can substitute in any object including a string, boolean, or number.
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# all data in python is treated as an object, so this line is putting the formatter object (i.e. the string literal) into each of the substitutions.
print(formatter.format(formatter, formatter, formatter, formatter))
# a comma indicates another argument.It doesn't matter if it's on the same line or not, and will go include everything up until the next argument or the end of the statement.
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))