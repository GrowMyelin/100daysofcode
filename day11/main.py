# Blackjack capstone project
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def comp():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    c1 = random.choice(cards)
    c2 = random.choice(cards)
    hand = [c1,c2]
    while sum(hand) < 16:
        hand.append(random.choice(cards))
    return sum(hand)

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)
    game = 'y'
    while game == 'y':
        c1 = random.choice(cards)
        c2 = random.choice(cards)
        hand = [c1,c2]
        cont = 'y'
        while cont == 'y':
            total = sum(hand)
            if total == 21:
                print(hand)
                print('You win!')
                break
            elif total > 21:
                print(hand)
                print('Bust')
                break
            else:
                print(f"Current total is {total}.")
                cont = input("Would you like to hit? ('y' or 'n') ")
                if cont == 'y':
                    new_card = random.choice(cards)
                    hand.append(new_card)
                else:
                    break
        comp_total = comp()
        print(f"Your total is {total}. Computer's total is {comp_total}.")
        if comp_total > 21 and total > 21:
            print('Tie')
        elif comp_total > 21 and total <= 21:
            print('You win')
        elif comp_total <= 21 and total > 21:
            print('You lose')
        elif total > comp_total:
            print('You win')
        elif total == comp_total:
            print('Tie')
        else:
            print('You lose')
    
        game = input("Would you like to play another game? ('y' or 'n') ")
        
if __name__ == "__main__":
    main()

