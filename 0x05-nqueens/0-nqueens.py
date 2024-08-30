#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def is_safe(board, row, col, N):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions."""
    def backtrack(row):
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    backtrack(0)
