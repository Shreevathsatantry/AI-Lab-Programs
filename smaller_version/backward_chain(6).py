def main():
    # Options dictionary mapping each choice to its behavior, animal, and color
    options = {1: ("Eat Flies", "Frog", "Green"), 
               2: ("Sings", "Canary", "Yellow")}

    print("*-----Backward Chaining*")
    print("\n X is \n1. Frog \n2. Canary")

    try:
        # Get the user's choice for the animal and validate the input
        x = int(input("Select One: "))
        if x not in options:  # Check if the choice is valid
            raise ValueError  # Raise error for invalid input

        # Output the selected behavior
        print(f"Chance Of {options[x][0]}")  # Display the corresponding behavior

        # Get the user's choice for color and validate
        print(f"\n X is {options[x][1]}")  # Display the selected animal
        print("\n1. Green \n2. Yellow")
        color_choice = int(input("Select Color: "))  # Get color choice

        # Check if the selected color matches the expected color for the animal
        if (color_choice == 1 and options[x][2] == "Green") or (color_choice == 2 and options[x][2] == "Yellow"):
            # If the color matches, print confirmation
            print(f"Yes, it is {options[x][1]} and Color is {options[x][2]}")
        else:
            # If the color does not match, print an error message
            print("\n---Invalid Knowledge Database")
    except ValueError:
        # Handle invalid input (e.g., non-integer or out-of-range)
        print("\n---Invalid Input")

if __name__ == "__main__":
    main()
