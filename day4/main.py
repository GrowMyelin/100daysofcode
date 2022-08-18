import random

# Rock paper scissors project

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def main():
    playerChoice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ')
    computerChoice = random.randint(0,2)
    choiceArr = [rock,paper,scissors]
    choiceArrNames = ['Rock','Paper','Scissors']
    print(choiceArr[int(playerChoice)])
    print(f"Computer chose: {choiceArrNames[computerChoice]}")
    print(choiceArr[computerChoice])
    if computerChoice == int(playerChoice):
        print('Tie')
    else:
        if (computerChoice == 0 and playerChoice == '1') or \
            (computerChoice == 1 and playerChoice == '2') or \
            (computerChoice == 2 and playerChoice == '0'):
            print('You win')
        else:
            print('You lose')

if __name__ == "__main__":
    main()
