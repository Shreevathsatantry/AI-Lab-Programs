# Input the number of queens
N = int(input("Enter the number of queens: "))

# Initialize the NxN chessboard with all elements set to 0
board = [[0] * N for _ in range(N)]

# Function to attempt to solve the N-Queens problem starting from a given row
def solve(row):
    # Base case: if all queens are placed, return True
    if row == N:
        return True
    
    # Try placing a queen in each column of the current row
    for col in range(N):
        # Check if it's safe to place a queen at (row, col)
        if all(board[i][col] == 0 and 
               (col - (row - i) < 0 or board[i][col - (row - i)] == 0) and 
               (col + (row - i) >= N or board[i][col + (row - i)] == 0) 
               for i in range(row)):
            # Place the queen
            board[row][col] = 1
            # Recur to place the rest of the queens
            if solve(row + 1):
                return True
            # Backtrack: remove the queen and try the next column
            board[row][col] = 0
    # If no column is valid, return False
    return False

# Start solving from the first row
solve(0)

# Print the final board configuration
for row in board:
    print(row)
