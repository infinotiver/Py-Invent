"""
Made by Pranjal Prakarsh
Originally Made for AISC COTW

This is my entry and a part for  a proposed project
What can be added
- Database
- Multiple User Login
- Hashing or Salting to store password instead of plaintext

"""
# Step 0: Import required modules
import os
import re
import time
from termcolor import colored
import string
import random

# Step 1: Declare a password variable with a strong password and set the number of password attempts to 0.

password_attempts = 0
PIN = "0000"
global password
password = "0000000"
# Step 2: Define a function is_valid_password to check if a password meets the required criteria
def is_valid_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return colored("[!] Password must be at least 8 characters long", "light_yellow")

    # Check if the password contains base 10 digits (0 through 9)
    if not any(char.isdigit() for char in password):
        return colored("[!] Password must contain digits from 0 - 9", "light_yellow")

    # Check if the password contains non-alphanumeric characters (special characters)
    if not re.search("[~!@#$%^&*_\-+=`|\\(){}\\[\\]:;\"'<>,.?/]", password):
        return colored("[!] Password must contain non-alphanumeric characters (special characters)", "light_yellow")

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return colored("[!] Password must contain at least one uppercase letter", "light_yellow")

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return colored("[!] Password must contain at least one lowercase letter", "light_yellow")

    return True

# Step 3: Add a generate_password function to automatically generate a strong password

def generate_password(length):
    # Define a string containing all possible characters for password
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices() to randomly select characters from all_chars
    while True:
        password = ''.join(random.choices(all_chars, k=length))

        # Check if password meets the minimum requirements
        if (any(char.isdigit() for char in password) and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            len(password) >= 8):
            return password
# Step 4: Make the main signup function which displays information and asks for setting password and pin

def signup():
    print(colored("PASSWORD MANAGER", "blue"))
    print(colored("Please set up your password", "green"))
    print(colored("Requirements of a Secure Password","green"))
    print("- At least 8 characters long")
    print("- Contains digits from 0 - 9")
    print("- Contains non-alphanumeric characters (special characters)")
    print("- Contains at least one uppercase letter")
    print("- Contains at least one lowercase letter")
    while True:
        pas = input(colored("Please enter your password (type generate to let me generate/gen one for you): ", "blue"))
        if pas in ("generate","gen"):
            pas=generate_password(12)
            print(f"Generated\n")
            print(colored(pas,"green"))
        if is_valid_password(pas) ==True:
            global password
            password = pas
            print(colored("[+] Password set successfully!", "green"))
            break
        else:
            print(is_valid_password(pas))
            print(colored("[-] Invalid password. Please try again.", "yellow"))

def pinset():
    print(colored("Please set up a four-digit PIN for password recovery", "green"))
    
    while True:
        pas = int(input(colored("Please enter your four-digit PIN: ", "blue")))
        if len(str(pas)) == 4 and pas >= 0:
            global PIN
            PIN = pas
            print(colored("[+] PIN set successfully!", "green"))
            break  
        else:
            print(colored("[-] Invalid PIN. Please enter a four-digit positive number.", "yellow"))
def signin():
    global password_attempts
    while password_attempts < 5:
        user_input = input("Enter your password or type 'reset' to reset your password: ")
        if user_input == "reset":
            reset_password()
        elif user_input == password:
            print(colored("[+] Login successful!", "green"))
            display_info()
            return
        else:
            password_attempts += 1
            print(colored(f"[-] Incorrect password. {5 - password_attempts} attempts remaining.", "yellow"))
    print(colored("Login limit exceeded. Resetting Password", "yellow"))
    reset_password()


def reset_password():
    print(colored("Please wait for 30 seconds before entering your PIN.", "green"))

    # Start the timer for 30 seconds
    for i in range(30, 0, -1):
        # Calculate the progress bar length
        progress_len = int((i / 30) * 20)
        # Print the progress bar and time remaining
        print(f"\r[{'=' * progress_len}{' ' * (20 - progress_len)}] {i} seconds left", end="")
        # Sleep for 1 second
        time.sleep(1)

    pin_attempts = 0
    while pin_attempts < 3:
        user_pin = int(input(colored("\n Enter your PIN: ", "blue")))
        if user_pin == PIN:
    
            while True:
                new_password = input(colored("Enter a new password: ", "blue"))
                if is_valid_password(new_password)==True:
                    password = new_password
                    print(colored("[+] Password changed successfully to\n", "green"))
                    print(password)
                    return
                else:
                    print(colored(is_valid_password(new_password),"red"))
                    print(colored(f"\nInsecure password. Please make sure password fulfills the requirements.", "yellow"))

        else:
            pin_attempts += 1
            print(colored(f"Incorrect PIN. Please try again. {3-pin_attempts} Attempts left.", "yellow"))
    print(colored("[-] PIN attempts limit exceeded.", "yellow"))


def display_info():
    os.system("cls")
    print(colored("=" * 30, "cyan"))
    print(colored("=" * 30, "cyan"))
    print(colored("Made by Infinotiver", "cyan"))
    print(colored("=" * 30, "cyan"))
    print(colored("=" * 30, "cyan"))
    print(colored("Password Security and You", "cyan"))
    print(colored("=" * 30, "cyan"))
    print(colored("With the increasing number of cyberattacks, password security has become crucial in today's digital age. Shockingly, in 2022, over 80% of cyberattacks involved password compromise, resulting in an average cost of $4.35 million for data breaches.", "magenta"))
    print(colored("To prevent unauthorized access to personal and sensitive information, a strong password is essential. According to the National Institute of Standards and Technology (NIST), a password must be at least 8 characters long and should include a combination of uppercase and lowercase letters, numbers, and special characters. Here are some additional tips to help you stay secure:\n", "magenta"))
    print(colored("- Avoid using the same password for multiple accounts", "magenta"))
    print(colored("- Avoid using personal information such as your name or birthdate in your password", "magenta"))
    print(colored("- Use a password manager to generate and store complex passwords", "magenta"))
    print(colored("- Enable two-factor authentication (2FA) wherever possible", "magenta"))
    print(colored("- Change your passwords regularly\n", "magenta"))
    print(colored("Here are some frequently asked questions about password security:\n", "magenta"))
    print(colored("- What is the best way to create a strong password?", "magenta"))
    print(colored("\t-- A strong password should be at least 8 characters long and include a combination of uppercase and lowercase letters, numbers, and special characters.", "magenta"))
    print(colored("- Is it safe to use a password manager?", "magenta"))
    print(colored("\t-- Yes, password managers use encryption to store your passwords securely. However 'browser' password managers arent safe", "magenta"))
    print(colored("- What is two-factor authentication?", "magenta"))
    print(colored("\t-- Two-factor authentication (2FA) is a security feature that requires you to provide two forms of identification (such as a password and a code sent to your phone) to access your account.", "magenta"))
    print("follow infinotiver and star and fork his repos on github")
    print(colored("=" * 30, "cyan"))

def login():
    os.system("cls")
    signup()
    pinset()
    signin()
login()




