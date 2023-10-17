# STRENGTH CHECK

import string
import re
import requests


def check_password_strength(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return "Weak: Password is too short (minimum length is 8 characters)."

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    # Check if the password contains at least one special character
    if not any(char in string.punctuation for char in password):
        return "Weak: Password must contain at least one special character."

    # Check if the password is not a common password or a dictionary word
    if is_common_password(password):
        return "Weak: Password is too common."
    
    if re.search(r'(.)\1{2,}', password):
        return "Weak Password : It has Reccuring Characters"
    
    TimetoCrack = estimate_crack_time(password)
    Formatted_TTK=format_number(TimetoCrack)

    # Password meets all complexity criteria
    passstrength = "Strong"

    return [passstrength,Formatted_TTK]

def format_number(number):
    if number < 1000:
        return str(number)
    elif number < 1000000:
        return f"{number / 1000:.1f} Thousand"
    elif number < 1000000000:
        return f"{number / 10000000:.1f} Million"
    elif number < 1000000000000:
        return f"{number/ 10000000000:.1f} Billion"
    else :
        return f"{number/1000000000000:.1f} Trillion"

def is_common_password(password):
    try:
        # Read common passwords from a local file
        filepath = "G:\\PY\\passowordgen\\Ananypass\\common_passwords.txt"
        with open(filepath, 'r') as file:
            common_passwords = set(file.read().splitlines())

        # Check if the password is in the list of common passwords
        return password in common_passwords
    except FileNotFoundError:
        print("Common passwords file not found.")
        return False

def estimate_crack_time(password, attempts_per_second=100000000000):
    # Calculate the number of possible combinations
    character_set_size = 94  # Printable ASCII characters
    password_length = len(password)
    combinations = character_set_size ** password_length
    
    # Calculate time to crack in seconds
    seconds_to_crack = combinations / attempts_per_second
    
    # Convert seconds to years
    seconds_in_a_year = 60 * 60 * 24 * 365.25
    years_to_crack = seconds_to_crack / seconds_in_a_year
    #years_to_crack = years_to_crack/100
    
    return round(years_to_crack)

if __name__ == '__main__':
    PassStrength = check_password_strength('Hel4542$%$@#')
    print(PassStrength)