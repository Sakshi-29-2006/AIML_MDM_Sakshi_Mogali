# Hill Climbing Algorithm

def objective_function(x):
    return -(x - 7) ** 2 + 49


def hill_climbing(start, minimum, maximum):
    current = start
    states_explored = 1

    while True:
        neighbors = []

        # Generate valid neighboring states
        if current > minimum:
            neighbors.append(current - 1)

        if current < maximum:
            neighbors.append(current + 1)

        best_neighbor = current
        best_value = objective_function(current)

        # Select the neighbor with better value
        for neighbor in neighbors:
            states_explored += 1

            if objective_function(neighbor) > best_value:
                best_neighbor = neighbor
                best_value = objective_function(neighbor)

        # Stop if no better neighbor exists
        if best_neighbor == current:
            break

        current = best_neighbor

    return current, objective_function(current), states_explored


# Input values
start = int(input("Enter starting state: "))
minimum = int(input("Enter minimum state: "))
maximum = int(input("Enter maximum state: "))

# Perform Hill Climbing
best_state, best_value, states_explored = hill_climbing(
    start, minimum, maximum
)

# Display result
print("\n--- Hill Climbing Result ---")
print("Best State:", best_state)
print("Maximum Value:", best_value)
print("States Explored:", states_explored)