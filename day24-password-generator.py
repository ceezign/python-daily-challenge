# password Generator script

import random
import string

def password_strength(password):
    length = len(password)
    categories = sum([
        any(c.islower()  for c in password),
        any(c.isupper()  for c in password),
        any(c.isdigit()  for c in password),
        any(c in "!@#$%^&*"  for c in password),
    ])
    score = length + categories * 2
    if score < 12:
        return "Weak"
    elif score < 18:
        return "Medium"
    else:
        return "Strong"

def generate_password(length, use_lower, use_upper, use_digits, use_special,
                      exclude_ambiguous):
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*"

    if exclude_ambiguous:
        for ch in "0o1I":
            chars = chars.replace(ch, "")

    if not chars:
        raise ValueError("No Character types selected! ")

    return "".join(random.choice(chars) for _ in range(length))

def main():
    length = int(input("Enter password length (minimum 8): "))
    if length < 8:
        print("Password must be at least 8 characters long.")
        return

    use_lower = input("Include lowercase letter? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase letter? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_special = input("Include special character? (y/n): ").lower() == "y"
    exclude_ambiguous = input("Exclude ambiguous? (y/n): ").lower() == "y"

    num_passwords = int(input("How many passwords to generate? "))

    with open("password.txt", "w") as file:
        for i in range(num_passwords):
            pwd = generate_password(length, use_lower, use_upper, use_digits, use_special, exclude_ambiguous)
            strength = password_strength(pwd)
            print(f"Password {i+1}: {pwd} ({strength})")
            file.write(f"{pwd} ({strength})\n")

    print("Password saved to password.txt")

if __name__ == "__main__":
    main()