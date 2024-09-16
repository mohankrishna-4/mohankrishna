# Allow the user to input their name, age, and favorite color in a single line, separated by commas
user_input = input("Enter your name, age, and favorite color separated by commas: ")

try:
    # Parse the input to extract the individual pieces of information
    # Split the input string by commas and strip any leading/trailing whitespace from each piece
    user_info = [item.strip() for item in user_input.split(',')]
    
    # Validate if the correct number of pieces of information is provided (should be exactly three)
    if len(user_info) != 3:
        print("Invalid Input. Please provide exactly three items separated by commas.")
    else:
        # Extract the individual pieces of information with appropriate variable names
        user_name, user_age, favorite_color = user_info
        
        # Validate if any field is empty
        if not user_name or not user_age or not favorite_color:
            print("Invalid Input. None of the fields should be empty.")
        else:
            # Print out a summary of the information using f-strings for formatting
            print("\nSummary:")
            print(f"Name: {user_name}")
            print(f"Age: {user_age}")
            print(f"Favorite Color: {favorite_color}")

except Exception as e:
    # Handle any unexpected errors by printing "Invalid Input"
    print("Invalid Input")
