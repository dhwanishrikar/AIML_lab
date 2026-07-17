#Develop a game playing agent in python for tic tac toe using minimax algorithm to determine optimal moves

import math
import time

class TicTacToeAgent:
    def __init__(self, ai_player='X', human_player='O'):
        self.ai = ai_player
        self.human = human_player

    def is_moves_left(self, board):
        """Checks if any empty cells remain on the board."""
        return any(cell == ' ' for row in board for cell in row)

    def evaluate(self, board):
        """
        Static evaluation function. 
        Returns +10 if AI wins, -10 if Human wins, 0 otherwise.
        """
        # Checking Rows for a win
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return 10 if row[0] == self.ai else -10

        # Checking Columns for a win
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return 10 if board[0][col] == self.ai else -10

        # Checking Diagonals for a win
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return 10 if board[0][0] == self.ai else -10

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return 10 if board[0][2] == self.ai else -10

        return 0

    def minimax(self, board, depth, is_max):
        """Recursively evaluates all possible board states using Minimax."""
        score = self.evaluate(board)

        # Terminal conditions: Return score if game is over
        if score == 10 or score == -10:
            return score
        if not self.is_moves_left(board):
            return 0

        # Maximizing Player (AI Turn)
        if is_max:
            best = -math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ' ':
                        board[r][c] = self.ai
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[r][c] = ' ' # Undo move
            return best

        # Minimizing Player (Human Turn)
        else:
            best = math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ' ':
                        board[r][c] = self.human
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[r][c] = ' ' # Undo move
            return best

    def find_best_move(self, board):
        """Evaluates all legal moves and returns the absolute best coordinates."""
        best_val = -math.inf
        best_move = (-1, -1)

        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = self.ai
                    move_val = self.minimax(board, 0, False)
                    board[r][c] = ' ' # Undo move

                    if move_val > best_val:
                        best_val = move_val
                        best_move = (r, c)

        return best_move


# --- Interactive Simulation Game Loop ---

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

if __name__ == "__main__":
    # Initialize empty 3x3 game board matrix
    game_board = [[' ' for _ in range(3)] for _ in range(3)]
    agent = TicTacToeAgent(ai_player='X', human_player='O')
    
    print("=== TIC-TAC-TOE MINIMAX AI ===")
    print("You are 'O' (Minimizer). AI is 'X' (Maximizer).")
    print_board(game_board)

    # Human goes first
    current_turn = 'HUMAN' 

    while agent.is_moves_left(game_board) and agent.evaluate(game_board) == 0:
        if current_turn == 'HUMAN':
            try:
                move = input("Enter your move (row and col 0-2, space separated like '1 2'): ")
                r, c = map(int, move.split())
                if game_board[r][c] != ' ':
                    print(" Position already taken! Try again.")
                    continue
                game_board[r][c] = agent.human
                current_turn = 'AI'
            except (ValueError, IndexError):
                print(" Invalid input. Please enter valid coordinates between 0 and 2.")
                continue
        else:
            print("Agent is calculating the optimal move...")
            time.sleep(0.5)
            r, c = agent.find_best_move(game_board)
            game_board[r][c] = agent.ai
            current_turn = 'HUMAN'

        print_board(game_board)

    # Game Over Evaluation
    final_score = agent.evaluate(game_board)
    if final_score == 10:
        print("Agent Wins! Better luck next time.")
    elif final_score == -10:
        print(" You won!")
    else:
        print(" It's a draw!")
