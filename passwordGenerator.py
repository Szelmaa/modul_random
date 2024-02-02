import random
import string

def generate_password(length, letters=True, digits=True, punctuation=True):
    pool = []
    if letters:
        pool += string.ascii_letters
    if digits:
        pool += string.digits
    if punctuation:
        pool += string.punctuation
    if pool:
        password = ''.join(random.choice(pool) for _ in range(length))
        return password
    else:
        print("The password cannot be generated.")


print("=== PASSWORD GENERATOR ===")

letters = True if input(
    "Do you want the password to contain letters? (y/n): ").lower() == 'y' else False
digits = True if input(
    "Do you want the password to contain digits? (y/n): ").lower() == 'y' else False
punctuation = True if input(
    "Do you want the password to contain punctuation? (y/n): ").lower() == 'y' else False

length = int(input("Enter the desired password length (int number): "))

password = generate_password(length, letters, digits, punctuation)

print(f"Generated password: {password}")
