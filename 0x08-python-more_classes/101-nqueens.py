#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""


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
