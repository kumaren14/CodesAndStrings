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


# Method     Use example      Explanation
# Center    aStr.center(w)     Finds the center point of whatever word or phrase you put for "w".
# ljust     aStr.ljust(w)      It returns the string left of its justified length/width.   ***
# rjust     aStr.rjust(w)      It returns the string right of its justified length/width.  ***
# upper     aStr.upper()       Switches lowercase letters to uppercase.
# lower     aStr.lower()       Switches uppercase letters to lowercase.
# index     aStr.index(item)   It searches for a given element from the list that you give it.
# rindex    aStr.rindex(item)  It searches for the highest index then returns it.
# find      aStr.find(item)    It is used to find an (Item) that you tell it to
# rfind     aStr.rfind(item)   It finds the highest index and does the same as the find string


# Character Functions

print(ord('a'))# this function can give us the unicode value for a piece of text or a string
# unicode is basically a universal language for symbols and characters

print(ord('1'))

print(chr(1)) # this is the opposite. It can give you the symbol/character for the unicode you type in

print(ord('%'))

print(chr(1))
print(chr(2))
print(chr(3))
print(chr(4))






from mapper import *       # we are importing the code and functions from a different file
print(letterToIndex('a'))

print(indexToLetter(24))



from crypto import *

print(scramble2Encrypt("THE CRANE FLIES AT MIDNIGHT"))

print(scramble2Decrypt("H RN LE TMDIHTECAEFISA INGT"))




