# [ Task 1 ]

# Original
'''
weather = "sunny"

if weather == "sunny":
print("Wear sunglasses!")
else:
print("Take an umbrella!")
'''

# Fixed
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

# Change: Indented the print statements



# [ Task 2 ]

# Using elif
feeling = input("How do you feel today? ")
if feeling == "happy":
    print("That's great to hear!")
elif feeling == "sad":
    print("I hope your day gets better")
else:
    print("Unknown input")

# Using if statements following assignment more closely
if feeling == "happy":
    print("That's great to hear!")
if feeling == "sad":
    print("I hope your day gets better")
