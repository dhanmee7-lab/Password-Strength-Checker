
import math
import getpass

# Common passwords to reject.
# This is a small sample, not a complete leaked-password database.
COMMON_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "iloveyou",
    "letmein",
    "abc123"
}


def calculate_entropy(password):
    """Estimate password entropy in bits."""
    alphabet_size = 0

    if any(c.islower() for c in password):
        alphabet_size += 26

    if any(c.isupper() for c in password):
        alphabet_size += 26

    if any(c.isdigit() for c in password):
        alphabet_size += 10

    if any(not c.isalnum() for c in password):
        alphabet_size += 33

    if alphabet_size == 0:
        return 0

    return len(password) * math.log2(alphabet_size)


def check_password(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Use at least 12 characters.")

    # Check uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check special characters
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This password is common. Choose a unique one.")

    # Calculate estimated entropy
    entropy = calculate_entropy(password)

    # Classify password strength
    if password.lower() in COMMON_PASSWORDS:
        strength = "Weak"
    elif score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Exceptional"

    return score, entropy, strength, feedback


def main():
    print("=" * 45)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    password = getpass.getpass("Enter password to check: ")

    if not password:
        print("Password cannot be empty.")
        return

    score, entropy, strength, feedback = check_password(password)

    print("\n----- PASSWORD SECURITY REPORT -----")
    print(f"Length: {len(password)} characters")
    print(f"Policy score: {score}/5")
    print(f"Estimated entropy: {entropy:.2f} bits")
    print(f"Strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nYour password meets all policy checks.")

    print("\nNote: Entropy is an estimate, not a guarantee.")
    print("This program uses a small common-password list.")


if __name__ == "__main__":
    main()
