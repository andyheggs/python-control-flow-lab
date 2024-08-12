# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():

    try:
    # - Prompt the user to input their age: "Please enter your age: "
        age = int(input ('Please enter your age'))

        # - Validate the input to ensure the age is a possible value (no negative numbers).
        if age < 0 or age > 120:
            print ('Please enter a valid age')

        # - Determine if the user is eligible to vote. Set a variable for the voting age.
        elif age < 18:
            print ('You are not old enough to vote!')  

        # - Print a message indicating whether the user is eligible to vote based on the entered age.
        else:
            print ('Cast your Ballot! \U0001F44D')

    # - Validate the input to ensure the age is a possible value (no negative numbers).
    except ValueError:
        print ("Please enter a valid number")


# Call the function
check_voting_eligibility()
