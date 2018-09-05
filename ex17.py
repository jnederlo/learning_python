from sys import argv
from os.path import exists

script, from_file, to_file = argv

################### >> LONG WAY << ######################
# print(f"Copying from {from_file} to {to_file}")

# # we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")

# out_file.close()
# in_file.close()

################## >> SHORT WAY << #######################

# using 'with' will guarantee that the file gets closed. Python will automatically close a file upon the end of the script, but it is good practice to ensure it.
with open(from_file) as f:
	indata = f.read()

with open(to_file, 'w') as f:
	out_file = f.write(indata)

print(f"Copied contents of {from_file} to {to_file}")