# the \t will print a tab.
tabby_cat = "\tI'm tabbed in."
# the \n will print a newline.
persian_cat = "I'm split\non a line."
# the \\ will print a single \.
backslash_cat = "I'm \\ a \\ cat."

BLACK = "Black Cat"
RED = "Red Cat"
BLUE = "Blue Cat"
PURPLE = "Purple Cat"

# you can put quotes inside a """ and you don't need to escape them, but escape sequences will still work for things like \t and \n etc.
fat_cat = f'''
I'll do a list:
\t* {BLACK}
\t* {RED}
\t* {BLUE}\n\t* {PURPLE}
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#Here are all of the escape sequences in Python:
print("ES backslash -->\\\\<-- prints this: \\")
print("ES single-quote -->\\'<-- prints this: \'")
print("ES double-quote -->\\\"<-- prints this: \"")
print("ES ASCII bell -->\\a<-- prints this: \a (it's the bell sound you hear)")
print("ES ASCII backspace -->\\b<-- prints this: \b (it's the ascii backspace)")
print("ES ASCII formfeed -->\\f<-- prints this: \f (it's a newline starting at the same column)")
print("ES ASCII linefeed -->\\n<-- prints this: \n (it's just a newline)")
print("ES Unicode Character named name -->\\N{name}<-- prints this: \N{GREEK CAPITAL LETTER DELTA}")
print("				-->\\r<-- prints this: \r (ES carraige return...)")
print("ES Horizontal Tab -->\\t<-- prints this: \t (it's a tab...)")
print("ES 16-bit hex value -->\\uxxxx<-- prints this: \u0394")
print("ES 16-bit hex value -->\\Uxxxxxxxx<-- prints this: \U00000394")
print("ES ASCII vertical -->\\v<-- prints this: \v (a vertical tab...)")
print("ES Character with octal value ooo -->\\ooo<-- prints this: \777")
print("ES Character with hex value hh -->\\xhh<-- prints this: \x42")