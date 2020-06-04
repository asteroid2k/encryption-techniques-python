num = [chr(245), chr(246), chr(247), chr(248), chr(249), chr(250), chr(251), chr(252), chr(253), chr(254), ]


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


def dessign(chara):
    return num[chara-48]


txt = input("Enter Cipher Text: ")
print("...............................\n")
for s in range(26):
    print(f"key#{s}: " + decrypt(txt, s))
