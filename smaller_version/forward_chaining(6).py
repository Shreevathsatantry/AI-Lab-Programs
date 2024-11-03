def main():
    # Options dictionary mapping each choice to its behavior, animal, and color
    options = {1: ("Croaks", "Frog", "Green"), 2: ("Eat Flies", "Frog", "Green"),
               3: ("Shrimps", "Canary", "Yellow"), 4: ("Sings", "Canary", "Yellow")}

    try:
        # Get the user's choice for behavior and validate the input
        x = int(input("Select X (1. Croaks, 2. Eat Flies, 3. Shrimps, 4. Sings): "))
        if x not in options:  # Check if the choice is valid
            raise ValueError  # Raise error for invalid input

        # Output the selected behavior
        print(f"\nX is {options[x][0]}")

        # Get the user's choice for color and validate
        color_choice = int(input("Select Color (1. Green, 2. Yellow): "))

        # Check if the selected color matches the expected color for the animal
        if (color_choice == 1 and options[x][2] == "Green") or (color_choice == 2 and options[x][2] == "Yellow"):
            # If the color matches, print the animal and its color
            print(f"Yes, it is {options[x][1]} and Color is {options[x][2]}")
        else:
            # If the color does not match, print an error message
            print("\n---Invalid Knowledge Database")
    except ValueError:
        # Handle invalid input (e.g., non-integer or out-of-range)
        print("\n---Invalid Input")

if __name__ == "__main__":
    main()
