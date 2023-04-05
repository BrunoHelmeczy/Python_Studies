from random import randint

def get_hands():
    return {0: 'scissor', 1: 'rock', 2: 'paper'}

def get_my_hand():
    hands = get_hands()
    hand = None

    while hand not in [str(x) for x in hands.keys()]:
        hand = input(f"Pick rock, paper, or scissor: {hands}. Your selection: ")

        if hand not in [str(x) for x in hands.keys()]:
            print(f"You typed '{hand}'. Please select from {hands}")

    out = hands[int(hand)]
    print(f"You picked '{out}'")

    return out

def play_rps():
    opp_hand = get_hands()[randint(0, 2)]
    my_hand  = get_my_hand()

    print(f"You picked '{my_hand}' while your opponent picked '{opp_hand}'")

    if opp_hand == my_hand:
        print(f"It's a Draw!")
    elif opp_hand == 'rock' and my_hand == 'paper': 
        print(f"You Won!")        
    elif opp_hand == 'rock' and my_hand == 'scissor': 
        print(f"You Lost!")
    elif opp_hand == 'paper' and my_hand == 'rock': 
        print(f"You Lost!")
    elif opp_hand == 'paper' and my_hand == 'scissor': 
        print(f"You Won!")
    elif opp_hand == 'scissor' and my_hand == 'rock': 
        print(f"You Won!")
    elif opp_hand == 'scissor' and my_hand == 'paper':     
        print(f"You Lost!")


play_rps()
