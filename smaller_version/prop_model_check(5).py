def DPLL(KB):
    def unit_propagate(clauses, assignments):
        # Simplifies clauses with unit propagation
        unit_clauses = [c for c in clauses if len(c) == 1]
        while unit_clauses:
            unit = unit_clauses.pop()
            lit = next(iter(unit))
            assignments[abs(lit)] = lit > 0
            # Remove satisfied clauses
            clauses = [c for c in clauses if lit not in c]
            # Remove negations of the literal
            clauses = [{l for l in c if l != -lit} for c in clauses]
            unit_clauses = [c for c in clauses if len(c) == 1]
        return clauses, assignments

    def solve(clauses, assignments):
        clauses, assignments = unit_propagate(clauses, assignments)
        if not clauses:  # No more clauses: satisfied
            return assignments
        if any(not c for c in clauses):  # Empty clause found: unsatisfiable
            return None
        # Pick a variable that hasn't been assigned yet
        var = next(
            iter(abs(l) for c in clauses for l in c if abs(l) not in assignments)
        )
        # Try both True and False assignments for the variable
        for value in [var, -var]:
            result = solve(
                [{l for l in c if l != -value} for c in clauses if value not in c],
                {**assignments, abs(var): value > 0}
            )
            if result:
                return result
        return None

    # Start solving
    result = solve(KB, {})
    return result or False

# Example usage
KB = [{1, -3}, {2, -1}, {4, -1, 2}]
print(DPLL(KB))
