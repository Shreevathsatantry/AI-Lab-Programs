VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [("csc", "maths"), ("csc", "phy"), ("maths", "phy"), ("maths", "che"), 
               ("maths", "tam"), ("phy", "tam"), ("phy", "eng"), ("che", "eng"), 
               ("tam", "eng"), ("tam", "bio"), ("eng", "bio")]

def backtrack(assignment):
    if len(assignment) == len(VARIABLES): 
        return assignment
    
    # Select the next unassigned variable
    var = next(v for v in VARIABLES if v not in assignment)
    
    # Try assigning each value in the domain to the variable
    for value in DOMAIN:
        # Flag to track if the current value for 'var' violates any constraints
        is_valid = True
        
        # Check each constraint in CONSTRAINTS
        for v1, v2 in CONSTRAINTS:
            # Check if 'var' is involved in the current constraint
            if var in (v1, v2):
                # Check if the value is already assigned to any variable involved in the constraint
                if assignment.get(v1) == value or assignment.get(v2) == value:
                    is_valid = False
                    break  # Stop checking further if the constraint is violated

        # If the value is valid, proceed to assign it to 'var'
        if is_valid:
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            # Remove 'var' from the assignment if the recursive call does not yield a solution
            assignment.pop(var)

    return None

# Call the backtrack function with an empty assignment
solution = backtrack({})
print(solution)
