
import random

while True:
 print('Make your choice:'  )
 choice = input()
choice = choice.lower()

 print("My choice is" , choice ) 

 choices = ['rock', 'paper', 'scissors']

 computer_choice = choices[random.randint(0, len(choices)-1)]

 print("Computer choice is", computer_choice)

 if choice == 'rock':
     if computer_choice == 'rock':
         print('it is a tie!')
     elif computer_choice == 'paper':
         print('you lose, sorry!')
     elif computer_choice == 'scissors':
         print('You win, yay!')

 if choice == 'paper':
     if computer_choice == 'paper':
         print('it is a tie!')
     elif computer_choice == 'scissors':
         print('you lose, sorry!')
     elif computer_choice == 'rock':
         print('You win, yay!')

 if choice == 'scissors':
     if computer_choice == 'scissors':
         print('it is a tie!')
     elif computer_choice == 'rock':
         print('you lose, sorry!')
     elif computer_choice == 'rock':
         print('You win, yay!')

print():
