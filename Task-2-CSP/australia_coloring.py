# NAME: COLLINS KIPKIRUI
# REG NO: CIT-227-065/2024
# UNIT: FOUNDATIONS OF AI
# TASK: Task 2(a) - Australia Map Coloring (CSP)

def is_valid(region, color, assignment, adjacency):
    """Checks if a color can be assigned to a region without clashing with neighbors."""
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, adjacency):
    """Backtracking algorithm to find a valid coloring solution."""
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
            # Undo assignment if it doesn't lead to a solution
            del assignment[region]
    return None

# Problem Definition
# List of the five regions as specified in the assignment 
regions = [
    "Western Australia", 
    "Northern Territory", 
    "South Australia", 
    "Queensland", 
    "New South Wales"
]

# The three allowed colors: Blue, Red, Green [cite: 124]
colors = ["Blue", "Red", "Green"]

# Adjacency mapping for the mainland regions
adjacencies = {
    "Western Australia": ["Northern Territory", "South Australia"],
    "Northern Territory": ["Western Australia", "Queensland", "South Australia"],
    "South Australia": ["Western Australia", "Northern Territory", "Queensland", "New South Wales"],
    "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
    "New South Wales": ["Queensland", "South Australia"]
}

# Solve the CSP
solution = backtrack({}, regions, colors, adjacencies)

# Display Results
if solution:
    print("--- Australia Map Coloring Solution ---")
    for region, color in solution.items():
        print(f"{region:20}: {color}")
else:
    print("No valid solution found with the given constraints.")
