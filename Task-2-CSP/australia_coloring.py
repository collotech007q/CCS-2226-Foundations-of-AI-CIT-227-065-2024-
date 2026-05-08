# NAME: COLLINS KIPKIRUI
# REG NO: CIT-227-065/2024
# UNIT: FOUNDATIONS OF AI
# TASK: Task 2(a) - Constraint Satisfaction Program (Australia)

def is_valid(region, color, assignment, adjacency):
    """Check if the current color assignment is consistent with neighbors."""
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, adjacency):
    """Solve the CSP using backtracking search."""
    if len(assignment) == len(regions):
        return assignment

    # Select the next unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, adjacency):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, adjacency)
            if result:
                return result
            # Backtrack if no solution is found
            del assignment[region]
    return None

# Problem Definition
# Mapping: A=WA, B=NT, C=SA, D=Q, E=NSW
regions = ['A', 'B', 'C', 'D', 'E'] 
colors = ['Red', 'Green', 'Blue']   

# Adjacencies based on the 5 mainland regions [cite: 123, 124]
adjacencies = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'C'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'C']
}

solution = backtrack({}, regions, colors, adjacencies)

if solution:
    print("Map Coloring Solution (A-E):")
    for region, color in solution.items():
        print(f"Region {region}: {color}")
else:
    print("No solution exists with the given constraints.")
