# -*- coding: utf-8 -*-
"""Tic-Tac-Toe.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VFb7C8uVnCkxKAS_0xoR9dknvFLVtKMh
"""

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]

        if player == "X": # Human player
            print(f"Player {player}'s turn.")
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input. Row and column must be between 0 and 2.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if check_win(board, player):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                elif all([cell != " " for row in board for cell in row]):
                    print_board(board)
                    print("It's a tie!")
                    break
                turn += 1
            else:
                print("That spot is already taken. Try again.")
        else: # Computer player
            print("Computer's turn.")
            row, col = computer_move(board)
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print("Computer wins!")
                break
            elif all([cell != " " for row in board for cell in row]):
                print_board(board)
                print("It's a tie!")
                break
            turn += 1

tic_tac_toe()