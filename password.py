import random
import string

def generate_password(length):
    # Define the character sets to be used
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation  # Feel free to customize with your own set

    # Combine all the character sets to form the full set of characters to pick from
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a password by randomly selecting 'length' number of characters from 'all_characters'
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the length of the password you would like to generate: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

if _name_ == "_main_":
    main()