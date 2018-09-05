name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
weight_in_pounds = 180 # lbs
weight_ratio_constant = 2.5000000
height_ratio_constant = 2.25000000 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_in_KG = round(weight_in_pounds / weight_ratio_constant, 4)
height_in_CM = round(height_in_inches * height_ratio_constant, 4)

print(f"Let's talk about {name}.")
print(f"He's {height_in_CM} CM tall.")
print(f"He's {weight_in_KG} KG's heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is trickym try to get it exactly right
total = age + height_in_CM + weight_in_KG
print(f"If I add {age}, {height_in_CM}, and {weight_in_KG} I get {total}.")
