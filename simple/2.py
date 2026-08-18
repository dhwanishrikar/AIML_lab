import math

EMPTY, HUMAN, AI = " ", "X", "O"

def print_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]} \n---+---+---\n {b[3]} | {b[4]} | {b[5]} \n---+---+---\n {b[6]} | {b[7]} | {b[8]} \n")

def moves(b):
    return [i for i in range(9) if b[i] == EMPTY]

def winner(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in wins)

def evaluate(b):
    if winner(b, AI): return 10
    if winner(b, HUMAN): return -10
    return 0

def minimax(b, depth, max_turn, alpha=-math.inf, beta=math.inf):
    score = evaluate(b)
    if score: return score - depth if score > 0 else score + depth
    if not moves(b): return 0

    if max_turn:
        best = -math.inf
        for m in moves(b):
            b[m] = AI
            best = max(best, minimax(b, depth+1, False, alpha, beta))
            b[m] = EMPTY
            alpha = max(alpha, best)
            if beta <= alpha: break
        return best
    else:
        best = math.inf
        for m in moves(b):
            b[m] = HUMAN
            best = min(best, minimax(b, depth+1, True, alpha, beta))
            b[m] = EMPTY
            beta = min(beta, best)
            if beta <= alpha: break
        return best

def best_move(b):
    best, move = -math.inf, -1
    for m in moves(b):
        b[m] = AI
        score = minimax(b, 0, False)
        b[m] = EMPTY
        if score > best:
            best, move = score, m
    return move

def play():
    b = [EMPTY]*9
    print("You=X  AI=O\nPositions 1-9")
    print_board(b)

    while True:
        # Human
        while True:
            try:
                pos = int(input("Your move (1-9): ")) - 1
                if pos in moves(b):
                    b[pos] = HUMAN
                    break
            except: pass
            print("Invalid!")
        print_board(b)
        if winner(b, HUMAN) or not moves(b): break

        # AI
        print("AI thinking...")
        pos = best_move(b)
        b[pos] = AI
        print(f"AI → {pos+1}")
        print_board(b)
        if winner(b, AI) or not moves(b): break

    if winner(b, HUMAN): print("You win!")
    elif winner(b, AI): print("AI wins!")
    else: print("Draw!")

if __name__ == "__main__":
    play()
