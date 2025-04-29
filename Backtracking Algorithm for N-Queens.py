def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row, N):
    if row == N:  # All queens are placed
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1, N):
                return True
            board[row][col] = 0  # Backtrack
    
    return False

def print_board(board):
    for row in board:
        print(' '.join('Q' if col == 1 else '.' for col in row))

# Example usage:
N = 4  # 4-Queens problem
board = [[0 for _ in range(N)] for _ in range(N)]

if solve_n_queens(board, 0, N):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")
