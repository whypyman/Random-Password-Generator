
import random
import string

def generate_password(length):
    if not (6 <= length <= 70):
        raise ValueError("Password length must be between 6 and 70")

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one of each required character type
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random choices
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable character positions
    random.shuffle(password)

    return ''.join(password)

# Prompt user for password length
try:
    user_length = int(input("Enter password length (6-70): "))
    password = generate_password(user_length)
    print("Generated password:", password)
except ValueError as e:
    print("Error:", e)
