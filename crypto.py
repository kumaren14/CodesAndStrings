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


alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?!"

def cesar(word):
    encrypt = ""
    for ch in word:
        Letters = alphabet.find(ch)
        nextLetters = (Letters + 3) % 57
        encrypt += alphabet[nextLetters]
    return encrypt


print(cesar("My name is Kumaren."))

def decrypt(encrypt):
    translate = ""
    for ch in encrypt:
        Letters = alphabet.find(ch)
        pastLetters = (Letters - 3) % 57
        translate += alphabet[pastLetters]
    return translate


print(decrypt("PACqdphClvCNxpduhq!"))




