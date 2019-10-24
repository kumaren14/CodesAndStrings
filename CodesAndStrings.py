# Strings

# Concatenation
#   2 or more strings and put them together

firstName = "Ian"

lastName = "Malcom"

name = firstName + " " + lastName

lastFirst = lastName + ", " + firstName

print(firstName + " " + lastName)
print(name)
print(lastFirst)


print("""                                    
                                        """)


# Repetition
#     repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, " + "row, "*2 + "your boat,")
    print("Gently down the stream.")
    print("Merrily, " +"merrily, "*3)
    print("Life is but a dream.")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstCharacter = name[0] # brackets lets us grab certain characters,
# in this case the letter in posistion 0 (posistion 0 is the first posistion) in name
# we can also use negative numbers to go backwards
print(firstCharacter)

middleCharacterIndex = len(name) // 2 # we can use this to find the length of our string
print(middleCharacterIndex)
middleCharacter = name[4]
print(middleCharacter)

print(name[-1])
print(name[-3])

for i in range(0, len(name)):
    print(name[0:i])

print(name[0:3])

# slicing and dicing
print(name[4:-8])

# searching

print("Biv" in name)# it is true that the string "Biv" is IN the string "name"

print("y" not in name)# false, because why is in name

if "y" not in name:
    print("y is not in name")
else:
    print("y is in name")

