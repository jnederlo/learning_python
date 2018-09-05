# this one is like your scripts with argv --> the '*' tells python to take all of the arguments to the function and then put them in a list. It's kind of useless.
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that's *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'.")

print_two("Jarvis", "Nederlof")
print_two_again("Jarvis", "Nederlof")
print_one("First!")
print_none()