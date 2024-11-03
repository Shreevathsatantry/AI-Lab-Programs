from collections import deque

class Solution:
    def solve(self, board):
        # Flatten board and define target configuration and possible moves for '0'
        start = tuple(sum(board, []))  # Convert board to a flat tuple
        target = (0, 1, 2, 3, 4, 5, 6, 7, 8)  # Target configuration (solved state)
        moves = {  # Valid moves for each position of '0' in a 3x3 grid
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5], 
            3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
            6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
        }
        
        # Initialize queue with the starting configuration and visited set
        queue = deque([(start, 0)])  # Queue holds (current state, steps to reach it)
        visited = {start}  # Set to track visited configurations
        
        # BFS to find the minimum steps to reach target configuration
        while queue:
            cur, steps = queue.popleft()  # Dequeue current configuration and steps count
            
            # Check if the current configuration matches the target
            if cur == target: 
                return steps
            
            # Find the index of '0' in the current configuration
            zero = cur.index(0)
            
            # Explore all valid moves for '0' from its current position
            for move in moves[zero]:
                nxt = list(cur)  # Create a mutable list copy of cur
                nxt[zero], nxt[move] = nxt[move], nxt[zero]  # Swap '0' with target position
                nxt = tuple(nxt)  # Convert back to tuple for hashing
                
                # If the new configuration hasn't been visited, add it to queue and visited
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))  # Enqueue new config with incremented step count
        
        # Return -1 if no solution was found
        return -1

# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("NO OF MOVES==", ob.solve(matrix))
