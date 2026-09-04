# Check whether a queen can be placed safely
def is_safe(board, row, col):
    for previous_row in range(row):

        previous_col = board[previous_row]

        # Check same column
        if previous_col == col:
            return False

        # Check diagonals
        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True


# Solve N-Queens using Backtracking
def solve_n_queens(n):
    board = [-1] * n
    nodes_explored = [0]

    def backtrack(row):

        # All queens are placed
        if row == n:
            return True

        for col in range(n):
            nodes_explored[0] += 1

            # Check if the position is safe
            if is_safe(board, row, col):
                board[row] = col

                if backtrack(row + 1):
                    return True

                # Backtrack
                board[row] = -1

        return False

    if backtrack(0):
        return board, nodes_explored[0]

    return None, nodes_explored[0]


# Display the board
def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):

            if board[row] == col:
                print("Q", end=" ")

            else:
                print(".", end=" ")

        print()


# Input number of queens
n = int(input("Enter number of queens: "))

# Solve the problem
solution, nodes_explored = solve_n_queens(n)

# Display result
print("\n--- N-Queens Result ---")

if solution:
    print("Solution:")
    print_board(solution)
else:
    print("No solution found")

print("Nodes Explored:", nodes_explored)