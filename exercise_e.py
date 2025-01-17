# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    
    # - The script should prompt the user to enter if it is cold (yes/no).
    cold = input("Is it cold? (yes/no): ").strip().lower()

    # - Then, ask if it is raining (yes/no).
    raining = input("Is it raining? (yes/no): ").strip().lower()

    #   - If it is cold AND raining, print "Wear a waterproof coat."
    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")

    #   - If it is cold BUT NOT raining, print "Wear a warm coat."    
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")

    #   - If it is NOT cold but raining, print "Carry an umbrella."
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")

    #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")

    #   - error handling 
    else:
        print("Please enter 'yes' or 'no' for both questions.")

# Call the function
weather_advice()

