import sys

# input_encoding is specified as utf-8, error is set to 'strict'
script, input_encoding, error = sys.argv #this is a tuple

def main(language_file, encoding, errors):
	line = language_file.readline() #the readline method will take a file object and read 1 line at a time, moving to the next line.

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors) # recursively calling main to read the next line so long as there is a line to read.


#This function takes in a line, the encoding codec, and the codec error specifyer. It will strip the newline character and set a variable to the encoded bytes of the line, and another varaiable to the decoded string of the line.
def print_line(line, encoding, errors):
	next_lang = line.strip() #Strip will remove all of the chars specified in () from the beginning or end of the string. Defaults to remove the \n.
	raw_bytes = next_lang.encode(encoding, errors=errors) #Encode will encode the string using the codec registered for encoding. errors is a data descriptor that specifies the unicode error handler, we are setting it to 'strict'
	cooked_string = raw_bytes.decode(encoding, errors=errors) #Decode will decode the string using the codec registered for encoding. The 'strict' error handling will raise a "UnicodeDecodeError" if the string can't be converted according to the encoding rules.

	print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8") #We are setting the codec used for encoding to be the utf-8 codec. This is the default codec so we don't actually need to specify it.

main(languages, input_encoding, error)


# in python we use utf-8, which will encode only the bytes that it requires.
# Asii remains the same.
# the .encode() method will return a byte representation of the unicode string in the requested encoding.
# the .decode() method will return a unicode string of the byte representation in the requested encoding.