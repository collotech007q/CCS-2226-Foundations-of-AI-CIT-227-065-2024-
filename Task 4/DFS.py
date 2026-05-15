# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def depth_first_search(graph, start, goal, visited=None, path=None):
   
    #Performs DFS to find the path from start to goal.
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    # Return path if goal is reached
    if start == goal:
        return path

    visited.add(start)

    # Explore neighbors recursively
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = depth_first_search(graph, neighbor, goal, visited, path + [neighbor])
            if result:
                return result
    
    return None

# Execution
start_node, goal_node = 'A', 'F'
result_path = depth_first_search(graph, start_node, goal_node)

print("--- DFS SEARCH RESULTS ---")
print(f"Initial Node: {start_node}")
print(f"Goal State: {goal_node}")
if result_path:
    print(f"Search Path: {' -> '.join(result_path)}")
else:
    print("Path not found.")
