import random

def main(lower,upper):
    x = random.choice(range(lower,upper+1,1))
    print("Welcome to the number guessing game!")
    print(f"I'm thinking of a number between {lower} and {upper}.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print('Wrong difficulty input, exiting now.')
        return
    guess = 0
    while guess != x:
        guess = int(input("Make a guess: "))
        if guess == x:
            print('You win!')
        elif guess > x:
            print('Too high')
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess < x:
            print('Too low.')
            attempts -= 1
            print(f"You have {attempts} remaining to guess the number.")
        if attempts == 0 and guess != x:
            print('Ran out of attempts. You lose.')
            break
        
if __name__ == "__main__":
    main(1,100)