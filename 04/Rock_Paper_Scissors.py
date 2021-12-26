import random


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

#Write your code below this line 👇
options = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scisors."))
print(options[player])

robot = random.randint(0,2)
print("python robot choose")
print(options[robot])

if player == 0 and robot == 2: #if rock vs scisors we win
    printf("you win")
elif player == 1 and robot == 0: #if paper vs rock we win 
    print("you win")
elif player == 2 and robot == 1: #if scisors vs paper we win 
    print("you win")
elif player == robot: #if player 1 and robot are equal its a draw 
    print("it's a Draw")
else:
    print("You Loose") #any other option will be a loose 