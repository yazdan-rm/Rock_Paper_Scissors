
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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))

game_images = [rock , paper , scissors]

computer_choice = random.randint(0 , 2)
row_1 = [1 , 0]
row_2 = [2 , 1]
row_3 = [0 , 2]
row_result = [row_1 ,
              row_2 ,
              row_3
             ]
if user_choice >= 3 or user_choice < 0 :
  print("Your input is invalid , you losed!")
elif row_result[0][0] == user_choice and row_result[0][1] == computer_choice:
  print(game_images[1])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[0])
  print("You won")
elif row_result[1][0] == user_choice and row_result[1][1] == computer_choice:
  print(game_images[2])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[1])
  print("You won")
elif row_result[2][0] == user_choice and row_result[2][1] == computer_choice:
  print(game_images[0])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[2])
  print("You won")
elif row_result[0][0] == computer_choice and row_result[0][1] == user_choice:
  print(game_images[0])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[1])
  print("You losed")
elif row_result[1][0] == computer_choice and row_result[1][1] == user_choice:
  print(game_images[1])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[2])
  print("You losed")
elif row_result[2][0] == computer_choice and row_result[2][1] == user_choice:
  print(game_images[2])
  print(f"Computer Chose:\n{computer_choice}")
  print(game_images[0])
  print("You losed")
else:
  if computer_choice == 0:
    print(game_images[0])
    print(f"Computer Chose:\n{computer_choice}")
    print(game_images[0])
    print("Equal!")
  if computer_choice == 1:
    print(game_images[1])
    print(f"Computer Chose:\n{computer_choice}")
    print(game_images[1])
    print("Equal!")
  if computer_choice == 2:
    print(game_images[2])
    print(f"Computer Chose:\n{computer_choice}")
    print(game_images[2])
    print("Equal!")
    
