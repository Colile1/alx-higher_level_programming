#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""


import sys

def is_safe(board, row, col):
    """
    Check if it is safe to place a queen at the given position on the chessboard.
    Parameters:
    - board: 2D list representing the chessboard
    - row: the row to check
    - col: the column to check
    Returns:
    - bool: True if it is safe to place a queen, False otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve(board, col):
    """
    Backtracking function to solve the N-Queens problem recursively.
    Parameters:
    - board: 2D list representing the chess board
    - col: integer representing the current column being processed
    Returns:
    None
    """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve(board, col + 1)
            board[i][col] = 0

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0 for i in range(N)] for j in range(N)]

solve(board, 0)
