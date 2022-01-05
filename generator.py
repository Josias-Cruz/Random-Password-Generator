import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_char = list("!@#%&")
characters  = list(string.ascii_letters + string.digits + "!@#%&")

def generate_random_password():

    length = int(input("Enter Password Length: "))

    alphabets_count = int(input("Enter Letter Count in Password: "))
    digit_count = int(input("Enter Digit Count in Password: "))
    spec_char_count = int(input("Enter Special Character Count: "))

    char_count = alphabets_count + digit_count + spec_char_count

    if char_count > length:
        print("Character count is greater than total password length")
        return
    
    password = []

    for letter in range(alphabets_count):
        password.append(random.choice(alphabets))

    for number in range(digit_count):
        password.append(random.choice(digits))
    
    for special in range(spec_char_count):
        password.append(random.choice(special_char))
    
    if char_count < length:
        random.shuffle(characters)
        for i in range(length-char_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("Secure Password: ")
    print("".join(password))

generate_random_password()