# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():

    # - The function should prompt the user to enter a letter (a-z or A-Z)
    # - It should handle both uppercase and lowercase letters.
    letter = input('Enter a letter (a-z or A-Z)').lower()

    # - Ensure to provide feedback for non-alphabetical or invalid entries.
    if not letter.isalpha() or len(letter) != 1:
        print(f'"{letter}" is not a valid letter.')

    # - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
    elif letter in 'aeiou':
        print(f'The letter {letter} is a vowel.')

    # - If the letter is a consonant, print: "The letter x is a consonant."
    else:
        print(f'The letter {letter} is a consonant.')

# Call the function
check_letter()

#python3 exercise_b.py
