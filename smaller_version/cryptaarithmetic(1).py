def find_value(word, assigned):
    num = 0
    for char in word:
        num = num * 10 + assigned[char]  # Build the number based on assigned values
    return num

def is_valid(assigned, word1, word2, result):
    # Ensure the first letters of each word are not zero
    return assigned[word1[0]] != 0 and assigned[word2[0]] != 0 and assigned[result[0]] != 0

def solve(word1, word2, result):
    letters = list(set(word1 + word2 + result))  # Get unique letters from all words
    if len(letters) > 10: 
        return '0 Solutions!'  # More than 10 letters means no valid assignments

    solutions = []  # List to store valid solutions

    def backtrack(assigned):
        if len(assigned) == len(letters):  # All letters are assigned
            if is_valid(assigned, word1, word2, result):
                num1 = find_value(word1, assigned)  # Convert word1 to a number
                num2 = find_value(word2, assigned)  # Convert word2 to a number
                num_result = find_value(result, assigned)  # Convert result to a number
                if num1 + num2 == num_result:  # Check if the sum is valid
                    # Format the solution with the assignment details
                    solutions.append(f"{num1} + {num2} = {num_result} {assigned}")
            return

        # Select the next letter to assign
        next_letter = letters[len(assigned)]

        for num in range(10):  # Try assigning digits from 0 to 9
            if num not in assigned.values():  # Ensure no duplicate digits
                assigned[next_letter] = num  # Assign current letter
                backtrack(assigned)  # Recur to assign the next letter
                del assigned[next_letter]  # Clean up the assignment after backtracking

    backtrack({})  # Start backtracking with an empty assignment
    return '\n'.join(solutions) if solutions else '0 Solutions!'  # Return all solutions or no solutions

if __name__ == '__main__':
    # Get user input for the words
    word1 = input('Enter WORD1: ').upper()
    word2 = input('Enter WORD2: ').upper()
    result = input('Enter RESULT: ').upper()
    print("Solutions:")
    print(solve(word1, word2, result))  # Print the solutions
