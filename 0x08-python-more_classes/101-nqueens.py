#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""
def is_safe(board, row, col, N):
    """
    Checks if it's safe to place a queen at the given position on the board.
    
    Parameters:
    board (list of lists): The chess board configuration
    row (int): The row to check
    col (int): The column to check
    N (int): The size of the board
    
    Returns:
    bool: True if it's safe to place a queen, False otherwise
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N, solutions):
    """
    Recursive backtracking function to solve the N-Queens problem.
    
    Parameters:
    - board: a 2D list representing the chess board
    - row: the current row being explored
    - N: the size of the board (number of rows and columns)
    - solutions: a list to store the valid solutions
    
    Returns:
    None
    """
    if row == N:
        solutions.append([[(i, j) for j in range(N) if board[i][j] == 1] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_n_queens(N):
    """
    Solve the N-Queens problem for a given board size.

    Args:
        N (int): The size of the board.

    Returns:
        None
    """
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)