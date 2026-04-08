# VITyarthi-Project-Assignment

# Password Generator Project
This is a simple Python script for generating a strong, random password based on a user-specified length

# Features
Custom Length: Generates a password of a length chosen by the user (minimum length of 3).
Character Diversity: Ensures the password includes a mix of:
      * Lowercase letters
      * Uppercase letters
      * Digits (0-9)
      * Special characters (`!@#$%^&*-_=+;:,.?/`)
Randomized Generation: Uses Python's `random` module to shuffle character sets and randomly select characters, enhancing security.
Regeneration Option: Allows the user to easily generate a new password without restarting the script.

# Prerequisites

You need to have **Python 3** installed on your system to run this script.

# Steps to run the program

1. Save the file: Save the provided Python code as a file named `password_generator_project.py`.

2. Run the script: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

```bash
python password_generator_project.py
```

3. Follow the prompts:

The script will first ask you to:
```
Enter the number of characters for the password:
```
Enter an integer value (e.g., `12`) and press Enter.
The generated password will be displayed.
You will then be asked:
```
Do you want to regenerate the password? (Y/N):
```
Enter `Y` to generate another password or `N` to exit the program.

Code Overview

The project is structured around several functions:

Character Sets:
The script initializes lists for lowercase, uppercase, digits, and special characters using the `string` module and a defined list. These are immediately shuffled for better randomness.
`divider(number)`:
Calculates four parts, each intended to be approximately 25% of the total password length, to ensure all character types are represented.
`p1`, `p2`, `p3`, `p4`:
Helper functions that randomly select characters from the lowercase, uppercase, digit, and special character lists, respectively, and append them to the `password` list.
`passwordGenerator()`:
Handles user input, enforcing that the input is an integer and at least 3.
Calls `divider()` and then the four helper functions (`p1` to `p4`) to build the initial password list.
Adjusts Length: Corrects for minor rounding errors by either adding remaining characters randomly or removing excess characters from the end to meet the exact desired length.
Final Shuffle: Shuffles the complete list of characters to fully randomize the password structure.
Joins the list into a final string and returns the generated password.
Main Loop:
The final `while` loop runs the `passwordGenerator()` and handles the prompt for regeneration, allowing continuous use until the user enters `N`.

Author:
Neelabh Mishra : (25BCE10791)
-----
