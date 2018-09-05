from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

# seek will set the pointer to whatever index point in the array of the object file that was opened.
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline())

# open takes the input file, and then creates a file object called "current_file"
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

# the tell() method will give us the current position in the open file.
print(current_file.tell())

print("Now let's rewind kind of like a tape.")

# this function takes in the current file and rewinds it to some point we specifiy in the function.
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)