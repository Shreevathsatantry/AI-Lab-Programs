import heapq
from itertools import permutations

# A* solver function to rearrange 'start' string to match 'goal'
def a_star_solver(start, goal):
    if sorted(start) != sorted(goal):
        return ["Goal not possible"]  # Return if characters do not match

    visited = set()  # Set to keep track of visited states
    heap = [(0, start, [start])]  # Priority queue with initial state

    while heap:
        _, current, path = heapq.heappop(heap)  # Get the state with the lowest distance
        if current == goal:  # If goal is reached, return the path
            return path
        if current in visited:  # Skip if the state is already visited
            continue
        visited.add(current)  # Mark the current state as visited

        # Generate all possible one-step permutations of adjacent characters
        for i in range(len(current) - 1):
            # Swap adjacent characters to generate a new state
            new_value = list(current)
            new_value[i], new_value[i + 1] = new_value[i + 1], new_value[i]
            new_value = ''.join(new_value)

            if new_value not in visited:  # If the new state hasn't been visited
                # Calculate heuristic: distance based on character position mismatch
                dist = sum(1 for a, b in zip(new_value, goal) if a != b)
                # Push the new state into the priority queue
                heapq.heappush(heap, (dist, new_value, path + [new_value]))

    return ["Goal not possible"]  # Return if no solution is found

# Running the solver
if __name__ == "__main__":
    path = a_star_solver("secure", "rescue")
    # Print each step in the solution path
    for i, step in enumerate(path):
        print(f"{i}) {step}")
