from collections import deque

# Graph represented as an adjacency list 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def breadth_first_search(graph, start, goal):
  
    #Performs BFS to find the path from start to goal.
    # Initialize the queue with the starting path
    queue = deque([[start]])
    visited = set()

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last node from the current path
        node = path[-1]

        # Goal Check: Return path if goal is reached
        if node == goal:
            return path

        # If the node hasn't been visited, explore its neighbors
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return "Path not found."

#  Execution
start_node, goal_node = 'A', 'F'
result_path = breadth_first_search(graph, start_node, goal_node)

print("--- BFS SEARCH RESULTS ---")
print(f"Initial Node: {start_node}")
print(f"Goal State: {goal_node}")
print(f"Search Path: {' -> '.join(result_path)}")
