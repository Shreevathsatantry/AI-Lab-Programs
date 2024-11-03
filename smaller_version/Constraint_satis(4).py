VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]

# Constraints defined as which subjects cannot be on the same day
CONSTRAINTS = {
    "csc": ["maths", "phy"], 
    "maths": ["phy", "che", "tam"],
    "phy": ["tam", "eng"], 
    "che": ["eng"], 
    "tam": ["eng", "bio"], 
    "eng": ["bio"]
}

# Function to check if the current assignment is valid
def is_valid(assignment):
    for var, neighbors in CONSTRAINTS.items():
        if var in assignment:
            for neighbor in neighbors:
                if neighbor in assignment and assignment[var] == assignment[neighbor]:
                    return False
    return True

# Backtracking function to find a valid assignment
def backtrack(assignment):
    if len(assignment) == len(VARIABLES):
        return assignment  # Return the complete and valid assignment

    # Select the next variable to assign
    var = [v for v in VARIABLES if v not in assignment][0]
    
    for value in DOMAIN:
        assignment[var] = value  # Assign a value to the variable
        if is_valid(assignment):  # Check if the assignment is valid
            result = backtrack(assignment)  # Recurse
            if result:  # If a valid assignment is found, return it
                return result
        del assignment[var]  # Remove the value and backtrack

    return None  # Return None if no valid assignment is found

# Start the backtracking algorithm
solution = backtrack({})
print(solution)
