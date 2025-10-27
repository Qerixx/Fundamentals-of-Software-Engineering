import re


def IsValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    checkSum = 0
    for i, char in enumerate(reversed(string)):
        digit = int(char)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checkSum += digit
    return checkSum


def isValidCheckSum(checkSum):
    return checkSum % 10 == 0


def getCardType(string):
    if len(string) == 13 or len(string) == 16 and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and string.startswith("34") or string.startswith("37"):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    else:
        return "Invalid"


cardNumber = input("Enter card number: ")
if IsValidNumber(cardNumber):
    if isValidCheckSum(getCheckSum(cardNumber)):
        print("Valid")
        print(getCardType(cardNumber))

else:
    print("Wrong Input. Try again.")