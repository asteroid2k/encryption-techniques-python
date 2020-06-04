# Special characters to represent digits 0-9
num = [chr(245), chr(246), chr(247), chr(248), chr(249), chr(250), chr(251), chr(252), chr(253), chr(254), ]


def encrypt(txt, ky):
    result = ""
    for i in range(len(txt)):
        char = txt[i]

        if char.isdigit():
            n = ord(char)
            result += assign(n)

        elif not char.isalpha():
            result += char
        elif char.isupper():
            result += chr((ord(char) + ky - 65) % 26 + 65)
        else:
            result += chr((ord(char) + ky - 97) % 26 + 97)
    return result


def decrypt(txt, ky):
    result = ""
    for i in range(len(txt)):
        char = txt[i]

        if char in num:
            result += dessign(char)

        elif not char.isalpha():
            result += char
        elif char.isupper():
            result += chr((ord(char) - ky - 65) % 26 + 65)
        else:
            result += chr((ord(char) - ky - 97) % 26 + 97)
    return result


# Encrypt digit with corresponding special character
def assign(numb):
    return num[numb - 48]


# Replace special character with corresponding digit
def dessign(chara):
    if chara == num[0]:
        return '0'
    elif chara == num[1]:
        return '1'
    elif chara == num[2]:
        return '2'
    elif chara == num[3]:
        return '3'
    elif chara == num[4]:
        return '4'
    elif chara == num[5]:
        return '5'
    elif chara == num[6]:
        return '6'
    elif chara == num[7]:
        return '7'
    elif chara == num[8]:
        return '8'
    elif chara == num[9]:
        return '9'


while True:
    print("E-Encrypt    D-Decrypt   Q-Quit")
    choice = input("choice:")
    choice = choice.upper()
    if choice == "E":
        text = input("Enter Plain Text: ")
        s = input("Enter Key: ")
        s = int(s)
        print("................................\n")
        print("Plain Text : " + text)
        print("Shift Key : " + str(s))
        print("Cipher Text: " + encrypt(text, s))
    elif choice == "D":
        text = input("Enter Cipher Text: ")
        s = input("Enter Key: ")
        s = int(s)
        print("...............................\n")
        print("Cipher Text : " + text)
        print("Shift Key : " + str(s))
        print("Plain Text: " + decrypt(text, s))
    elif choice == "Q":
        exit(900)
