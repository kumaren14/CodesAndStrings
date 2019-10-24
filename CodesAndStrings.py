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


# repetition
#     repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, " + "row, "*2 + "your boat,")
    print("Gently down the stream.")
    print("Merrily, " +"merrily, "*3)
    print("Life is but a dream.")

rowYourBoat()