# transposistion cypher


#encryption function

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1

    cipherText = oddChars + evenChars
    return cipherText




def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]   # half length to the end
    oddChars = cipherText[:halfLength]      # half length from the beginning

    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]


    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]


    return plainText



def CesarEncrypt():

    input("type a letter")

    if "a"
        print("b")
    else
        if b
            print("c")
    else
        if c
            print("e")
    return CesarEncrypt()





plainText = input("What is your plaintext? ")
shift = input("What is your shift? ")

def caesar(plainText, shift):

    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
        cipherText = ""
        cipherText += finalLetter

    print("Your ciphertext is: ", cipherText)

    return cipherText

caesar(plainText, shift)





