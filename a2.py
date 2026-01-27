import random
print("Welcome to rock, paper, scissors!")
computerscore = 0
userscore = 0
while True:

 computerchoice = random.choice(['rock', 'paper', 'scissors'])
 userchoice = input("Enter your choice (rock, paper, scissors): ")
 print(f"Computer chose: {computerchoice}")
 print(f"You chose: {userchoice}")
 if userchoice == computerchoice:
        print("It's a tie!")
 elif (userchoice == 'rock' and computerchoice == 'scissors') or \
         (userchoice == 'paper' and computerchoice == 'rock') or \
         (userchoice == 'scissors' and computerchoice == 'paper'):
        print("You win!")
        userscore=userscore + 1
        print("Your score is:", userscore)
 else:
        print("Computer wins!")
        computerscore=computerscore + 1
        print("Computer's score is:", computerscore)