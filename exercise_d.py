# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():

    try: 
        # - Prompt the user to enter a dog's age: "Input a dog's age: "
        dogs_age = int(input("Input the dog's age: "))

        if dogs_age < 0:
            print ('Please enter a valid age')
            return
        
        #      - The first two years of the dog's life count as 10 dog years each.
        if dogs_age == 1:
            dog_years = 10
        
        elif dogs_age == 2:
            dog_years = 20

        #      - Each subsequent year counts as 7 dog years.
        else:
            dog_years = 20 + (dogs_age -2) * 7
            
        # - Print the calculated age: "The dog's age in dog years is xx."
        print(f"The dog's age in dog years is {dog_years}.")

    except ValueError:
        print ("Please enter a valid number")

# Call the function
calculate_dog_years()


