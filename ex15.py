# specifying the argument to pass into the program call as variable (object?) argv.
from sys import argv

# setting the script to the executable file name, and filename to equal the argument given in argv.
script, filename = argv

print(script)
print(filename)
# calling open on the filename which will set the contents to the object txt.
txt = open(filename)

# formatting the print to grab the "filename" object and print it at the end of the format string.
print(f"Here's your file {filename}:")
print("Here's your file {}".format(filename)) #this is the same as the line above it.
# calling read method on the txt object which will read the content of the object.
print(txt.read())



print("Type the filename again:")

#closing the opened file object
txt.close()

# setting another object "file_again" to the input to be passed into the program with the prompt.
file_again = input("> ")

# setting "txt_again" to equal the return from the open function with the filename specified in the input.
txt_again = open(file_again)

# calling read methon on the txt_again object which will read the contents of the object.
print(txt_again.read())

# closing the opened file object.
txt_again.close()
