import random
import string

def get_password_length():
    while True:
        try:
            password_length = int(input("Enter passowrd length: "))
            if password_length < 8:
                print("Your password should have length of at least 8")
            else:
                return password_length
        except ValueError:
            print("Please enter a valid integer.")


def password_function(password_length):

    numbers = string.digits
    alhpanumeric_b = string.ascii_uppercase
    alhpanumeric_s = string.ascii_lowercase
    special_characters = string.punctuation

    all_characters= list(numbers + alhpanumeric_b + alhpanumeric_s + special_characters)

#print(all_characters)

    password = ''

    for characters in range (password_length):
        password += random.choice(all_characters)

    return password

password_length = int(input("Enter passowrd length: "))

password_length = get_password_length()

print(f"Generated password: {password_function(password_length)}")
