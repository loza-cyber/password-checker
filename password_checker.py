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


# Main program
print("🔐 Password Security Checker")
print("----------------------------")

while True:
    password = input("Enter your password: ")

    if password == "":
        print("❌ Password cannot be empty. Please try again.")
    else:
        break

score = check_password(password)

print("----------------------------")
print("Score:", score, "/ 5")

if score <= 2:
    print("🔴 Password strength: Weak")
elif score <= 4:
    print("🟡 Password strength: Medium")
else:
    print("🟢 Password strength: Strong")