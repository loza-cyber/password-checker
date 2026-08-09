
import getpass


def check_password(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        print("✅ Length: Good")
        score += 1
    else:
        print("❌ Length: Too short")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        print("✅ Uppercase letter: Yes")
        score += 1
    else:
        print("❌ Uppercase letter: No")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        print("✅ Lowercase letter: Yes")
        score += 1
    else:
        print("❌ Lowercase letter: No")

    # Check for numbers
    if any(char.isdigit() for char in password):
        print("✅ Number: Yes")
        score += 1
    else:
        print("❌ Number: No")

    # Check for special characters
    if any(not char.isalnum() for char in password):
        print("✅ Special character: Yes")
        score += 1
    else:
        print("❌ Special character: No")

    return score


def get_strength(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def show_strength_meter(score):
    meter = "█" * score
    print("Strength meter:", meter, f"{score}/5")


def is_common_password(password):
    common_passwords = [
        "password",
        "password123",
        "12345678",
        "qwerty123",
        "admin123"
    ]

    return password.lower() in common_passwords


# Main program

print("🔐 Password Security Checker")
print("----------------------------")

while True:
    password = getpass.getpass("Enter your password: ")

    if password == "":
        print("❌ Password cannot be empty. Please try again.")
    elif len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
    else:
        break


# Check if password is common
if is_common_password(password):
    print("⚠️ Warning: This is a common password.")
    print("⚠️ Consider choosing a more unique password.")


# Check password
score = check_password(password)

print("----------------------------")
print("Score:", score, "/ 5")

strength = get_strength(score)

show_strength_meter(score)

if strength == "Weak":
    print("🔴 Password strength:", strength)
elif strength == "Medium":
    print("🟡 Password strength:", strength)
else:
    print("🟢 Password strength:", strength)

