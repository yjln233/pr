"""Generate secure random passwords."""

import secrets
import string


def generate_password(length: int = 20, count: int = 1) -> None:
    """Generate secure passwords and print them."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"

    if length < 8:
        print("⚠️  Warning: short passwords (< 8 chars) are not recommended.")

    for i in range(count):
        password = "".join(secrets.choice(alphabet) for _ in range(length))

        # Ensure at least one of each character class
        if length >= 4:
            has_upper = any(c.isupper() for c in password)
            has_lower = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in "!@#$%^&*()-_=+" for c in password)

            if not all([has_upper, has_lower, has_digit, has_special]):
                # Regenerate this one
                password = "".join(secrets.choice(alphabet) for _ in range(length))

        if count == 1:
            print(f"🔑 Password: {password}")
        else:
            print(f"  {i + 1:>3}. {password}")

    if count == 1:
        # Show strength estimate
        charset_size = len(alphabet)
        entropy = length * (charset_size.bit_length() - 1)
        if entropy < 40:
            strength = "Weak 😱"
        elif entropy < 60:
            strength = "Moderate 😐"
        elif entropy < 80:
            strength = "Strong 💪"
        else:
            strength = "Very Strong 🛡️"

        print(f"  Length: {length} chars | Entropy: ~{entropy} bits | {strength}")


def leetify(text: str) -> str:
    """h3ll0 h0w 4r3 y0u -> Translate text to leet speak."""
    table = str.maketrans({
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
        't': '7', 'T': '7',
        'g': '9', 'G': '9',
        'l': '1', 'L': '1',
    })
    return text.translate(table)
