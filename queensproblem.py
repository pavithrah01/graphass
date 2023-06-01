def solve_n_queens(n):
    # Create an empty chessboard
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check if it is safe to place a queen at the given position
        # Check the row and column
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        # Check the diagonals
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q' and (i+j == row+col or i-j == row-col):
                    return False
        return True

    def backtrack(row):
        if row == n:
            # All queens are successfully placed, add the solution
            solutions.append([''.join(row) for row in board])
        else:
            for col in range(n):
                if is_safe(row, col):
                    # Place the queen at the current position
                    board[row][col] = 'Q'
                    # Recur to place the queens in the next row
                    backtrack(row + 1)
                    # Remove the queen and backtrack if no solution is found
                    board[row][col] = '.'

    backtrack(0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()
