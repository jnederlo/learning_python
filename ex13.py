from sys import argv
# import sys
# this is how you set your arguuments to the argv variable:
#	argv[0] = script = executable
#	argv[1] = first = first argument from input
#	argv[2] = second = second argument from input
#	argv[3] = third = third argument from input
script, first, second, third = argv

# this replaces argv with the input from the user.
argv = input()

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", argv)