import random
playing= True
no=str(random.randint(1,5))
print("Guess a number between 1 and 5")
print("The game is over when you guess the correct number")

while playing:
    guess=input("Enter your guess: ")
    if guess==no:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again!")   

   
 
