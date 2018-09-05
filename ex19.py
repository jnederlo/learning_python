# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# 	print(f"You have {cheese_count} cheeses!")
# 	print(f"You have {boxes_of_crackers} boxes of crackers!")
# 	print("Man that's enough for a party!")
# 	print("Get a blanket.\n")


# print("We can just give the functions numbers directly:")
# cheese_and_crackers(20, 30)

# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50

# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6)

# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def schools(school1, school2):
	print()
	if school1 == "U of A":
		print(f"{school1} is located in Edmonton")
	else:
		print(f"{school1} is NOT located in Edmonton")
	
	if school1 == "U of A" and (school2 == "42" or school2 == 42):
		print(f"I have attended both {school1} and {school2}")

def take_input():
	return input("Enter a school\n")

## it's bad practice to have global variables defined with the same name as local variables.
# first_school = input("Enter a school\n") 
# second_school = input("Enter another school\n")

# schools(school1, school2)
# schools("U of C", 42)
# schools("U of A", 42)
# schools(input("Enter a school\n"), input("Enter another school\n"))
# schools(school1 = take_input(), school2 = take_input())
schools(take_input(), take_input())