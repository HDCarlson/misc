import sys
import math
special_characters = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
def Encoder(s):
    result = ""
    for i in range(len(s)):
        char = s[i]
        if i % 2 == 0:
            if char.isnumeric():
                char = int(char) + 3
                if char >= 10:
                    char -= 10
                if char < 0:
                    char += 10
                result+= str(char)
            elif (char.isupper()):
                result += chr((ord(char) - 3 -65) % 26 + 65).lower()
            elif (char.islower()):
                result += chr((ord(char)  -3 - 97) % 26 + 97).upper()
            elif any(c in special_characters for c in char):
                index = special_characters.find(char)
                index += 3
                if index >= len(special_characters):
                    index -= len(special_characters)
                result += special_characters[index]
            else:
                result += char
        else:
            if char.isnumeric():
                char = int(char) - 3
                if char > 10:
                    char -= 10
                if char < 0:
                    char += 10
                result+= str(char)
            elif (char.isupper()):
                result += chr((ord(char) + 3 -65) % 26 + 65).lower()
            elif (char.islower()):
                result += chr((ord(char) + 3 - 97) % 26 + 97).upper()
            elif any(c in special_characters for c in char):
                index = special_characters.find(char)
                index -= 3
                if index < 0:
                    index += len(special_characters)
                result += special_characters[index]
            else:
                result += char
    print(result)
def Decoder(s):
    result = ""
    for i in range(len(s)):
        char = s[i]
        if i % 2 == 0:
            if char.isnumeric():
                char = int(char) - 3
                if char >= 10:
                    char -= 10
                if char < 0:
                    char += 10
                result+= str(char)
            elif (char.isupper()):
                result += chr((ord(char) + 3 -65) % 26 + 65).lower()
            elif (char.islower()):
                result += chr((ord(char) + 3 - 97) % 26 + 97).upper()
            elif any(c in special_characters for c in char):
                index = special_characters.find(char)
                index -= 3
                if index < 0:
                    index += len(special_characters)
                result += special_characters[index]
            else:
                result += char
        else:
            if char.isnumeric():
                char = int(char) + 3
                if char >= 10:
                    char -= 10
                if char < 0:
                    char += 10
                result+= str(char)
            elif (char.isupper()):
                result += chr((ord(char) - 3 -65) % 26 + 65).lower()
            elif (char.islower()):
                result += chr((ord(char) - 3 - 97) % 26 + 97).upper()
            elif any(c in special_characters for c in char):
                index = special_characters.find(char)
                index += 3
                if index >= len(special_characters):
                    index -= len(special_characters)
                result += special_characters[index]
            else:
                result += char
    print(result)

def main():
    choice = input("Encode or Decode? ")
    message = input("Code?")
    if choice.lower() == "encode":
        Encoder(message) 
    if choice.lower() == "decode":
        Decoder(message)

if __name__ == "__main__":
    main()

