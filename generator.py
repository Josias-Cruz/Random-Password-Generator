import string
import random

characters  = list(string.ascii_letters + string.digits + "!@#%&")

def generate_random_password():

    length = int(input("Enter Password Length: "))

    random.shuffle(characters)

    password = []

    for space in range(length):
        password.append(random.choice(characters))
    
    random.shuffle(password)

    print("".join(password))

generate_random_password()