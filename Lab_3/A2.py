import string

password=input('Enter password: ')

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
special = '#-*'
errors=[]

if len(password)!=8:
    errors.append('The password length is not equal to 8')

if password==password.lower():
    errors.append('There are no uppercase letters in the password')

if password==password.upper():
    errors.append('The password is missing lowercase letters')

if not any(symbol.isdigit() for symbol in password):
    errors.append('There are no numbers in the password')

if not any(symbol in special for symbol in password):
    errors.append('There are no special characters in the password')

if not all(symbol in allowed for symbol in password):
    errors.append('The password uses unintended symbols')

if not errors:
    print('Good password')
else:
    for errors in errors:
        print(errors)



