
def show_probability(event, sample_space, name):
    p = len(event) / len(sample_space)
    print(f"  {name}: {event}")
    print(f"  P({name}) = {len(event)}/{len(sample_space)} = {p:.3f}\n")

def coin():
    print("\n=== TOSSING A FAIR COIN ===")
    S = {"H", "T"}
    print("Sample Space S =", S)
    print("|S| =", len(S), "\n")

    heads = {"H"}
    tails = {"T"}

    show_probability(heads, S, "Heads")
    show_probability(tails, S, "Tails")

def die():
    print("\n=== ROLLING A FAIR SIX-SIDED DIE ===")
    S = {1, 2, 3, 4, 5, 6}
    print("Sample Space S =", S)
    print("|S| =", len(S), "\n")

    even   = {2, 4, 6}
    odd    = {1, 3, 5}
    
    show_probability(even,  S, "Even")
    show_probability(odd,   S, "Odd")
    
def card():
    print("\n=== DRAWING ONE CARD FROM A STANDARD DECK ===")
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    # Sample space as (rank, suit) tuples
    S = {(r, s) for r in ranks for s in suits}
    print("Sample Space S has", len(S), "cards (52)")
    print("Example outcomes: ('A','Hearts'), ('K','Spades'), ...\n")

    # Events
    hearts   = {(r, "Hearts") for r in ranks}
    face     = {(r, s) for r in ["J", "Q", "K"] for s in suits}
    ace      = {( "A", s) for s in suits}
    red      = {(r, s) for r in ranks for s in ["Hearts", "Diamonds"]}
    black    = {(r, s) for r in ranks for s in ["Clubs", "Spades"]}

    show_probability(hearts, S, "Hearts")
    show_probability(face,   S, "Face card (J/Q/K)")
    show_probability(ace,    S, "Ace")
    show_probability(red,    S, "Red card")
    show_probability(black,  S, "Black card")

def main():
    print("Basic Probability Notations")
    print("===========================")
    print("1. Tossing a Coin")
    print("2. Rolling a Die")
    print("3. Drawing a Card")
    
    while True:
        choice = input("\nChoose experiment (1/2/3) or q to quit: ").strip().lower()
        
        if choice == "1":
            coin()
        elif choice == "2":
            die()
        elif choice == "3":
            card()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or q.")

if __name__ == "__main__":
    main()
