import random
import string

def generate_password(password_length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) 
    for i in range(password_length))
    return password

password_length = int(input("Enter the password length: ")) 
if password_length < 1:
    print("Password length should be at least 1.")
else:
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
