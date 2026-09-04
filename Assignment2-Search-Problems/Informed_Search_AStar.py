import heapq

# Input graph details
n = int(input("Enter number of nodes: "))

print("Enter node names:")
nodes = input().split()

graph = {}

# Initialize graph
for node in nodes:
    graph[node] = []


# Input edges with costs
m = int(input("\nEnter number of edges: "))

print("Enter edges with cost (example: A B 5):")

for _ in range(m):
    u, v, cost = input().split()
    cost = int(cost)

    graph[u].append((v, cost))
    graph[v].append((u, cost))


# Input heuristic values
heuristic = {}

print("\nEnter heuristic value for each node:")

for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))


# A* Search Algorithm
def a_star(start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    best_cost = {start: 0}
    nodes_explored = 0

    while priority_queue:
        # Remove node with lowest f(n) value
        f, current_cost, current, path = heapq.heappop(
            priority_queue
        )

        nodes_explored += 1

        # Check if goal is reached
        if current == goal:
            return path, current_cost, nodes_explored

        # Explore neighboring nodes
        for neighbor, edge_cost in graph[current]:

            new_cost = current_cost + edge_cost

            # Update if a better path is found
            if neighbor not in best_cost or new_cost < best_cost[neighbor]:

                best_cost[neighbor] = new_cost

                # Calculate f(n) = g(n) + h(n)
                f_value = new_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (
                        f_value,
                        new_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, None, nodes_explored


# Input start and goal nodes
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Perform A* Search
path, cost, nodes_explored = a_star(start, goal)


# Display result
print("\n--- A* Search Result ---")

if path:
    print("Path:", " -> ".join(path))
    print("Path Cost:", cost)
else:
    print("Goal not found")

print("Nodes Explored:", nodes_explored)