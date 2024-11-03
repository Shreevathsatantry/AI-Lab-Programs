from math import inf

def minimax(depth, node_index, is_max, values, alpha=-inf, beta=inf):
    # Base case: if we reach the leaf node (depth of 3)
    if depth == 3:
        return values[node_index]  # Return the value of the leaf node
    
    if is_max:  # Maximizing player's turn
        best = -inf  # Initialize best score for maximizing player
        for i in range(2):  # Explore two children
            # Recursively call minimax for the child node
            best = max(best, minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta))
            alpha = max(alpha, best)  # Update alpha (best score for maximizing player)
            if beta <= alpha:  # Prune branches if possible (alpha-beta pruning)
                break
        return best  # Return the best score for maximizing player
    else:  # Minimizing player's turn
        best = inf  # Initialize best score for minimizing player
        for i in range(2):  # Explore two children
            # Recursively call minimax for the child node
            best = min(best, minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta))
            beta = min(beta, best)  # Update beta (best score for minimizing player)
            if beta <= alpha:  # Prune branches if possible (alpha-beta pruning)
                break
        return best  # Return the best score for minimizing player

# Example usage
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf node values
    print("The optimal value is:", minimax(0, 0, True, values))  # Start the minimax algorithm
