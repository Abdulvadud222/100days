import random

# head_or_tail = random.randint(1, 2)
# if head_or_tail == 1:
#     message = "Heads"
# else:
#     message = "Tails"
# print(f"It is {message}")

# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
#     "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", 
#     "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
#     "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", 
#     "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
#     "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", 
#     "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
#     "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", 
#     "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# # print(states_of_america[4]) #this will print out the 5th item in the list

# states_of_america[2] = "Arizona21" #this changes the third item into Arizona21
# addition = ["Newland"] #created a variable to use later
# states_of_america.extend(addition) #using the variable to use in extend method or i could just use a list inside the parenthesis
# print(states_of_america)

# names_string = input("Give me the names and I will tell who shall pay!\n")
# names = names_string.split(",")
# names = [name.strip() for name in names if name.strip()]
# number_of_people = len(names)
# payer_number = random.randint(0, number_of_people - 1)
# payer = names[payer_number]
# print(f"Well, {payer} has been granted to pay for his amazing friends!")



# #another way of writing down the code above, with fewer lines of course)
# names_string = input("Give me the names and I will tell who shall pay!\n"
#                      "They should be separated by comma: ")
# names = names_string.split(",")
# payer = random.choice(names)
# print(f"Well, {payer} has been granted to pay for his amazing friends!")


# level1 = ["Bob", "jane", "lucy"]
# level2 = ["sam", "Bruce", "Nelson"]
# students = [level1, level2] #an example of a nested list
# print(students)



# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# location = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position_string = input("Where do you want to put the treasure?\n"
#                  "Coulmn first and row second. Write with a space: ")
# position_list = position_string.split(" ")
# for column in position_list[0]:
#     column_number = int(column)

# for row in position_list[1]:
#     row_number = int(row)
# if row_number == 1:
#     row1[column_number - 1] = "x"
#     print(f"{row1}\n{row2}\n{row3}")
# elif row_number == 2:
#     row2[column_number - 1] = "x"
#     print(f"{row1}\n{row2}\n{row3}")
# elif row_number == 3:
#     row3[column_number - 1] = "x "
#     print(f"You hid the treasure here: \n{row1}\n{row2}\n{row3}")
# else:
#     print("You input an invalid number. Please, input a valid one!")


# ###this one is suggested by chatgpt!
# # Initial grid setup
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# location = [row1, row2, row3]

# # Display initial grid
# print(f"{row1}\n{row2}\n{row3}")

# # Get user input
# position_string = input("Where do you want to put the treasure?\n"
#                         "Column first and row second (e.g., '2 3'): ")

# # Parse column and row numbers
# position_list = position_string.split(" ")
# if len(position_list) != 2 or not all(x.isdigit() for x in position_list):
#     print("Invalid input! Please provide two numbers separated by a space.")
# else:
#     column_number = int(position_list[0])
#     row_number = int(position_list[1])

#     # Validate input range
#     if 1 <= column_number <= 3 and 1 <= row_number <= 3:
#         # Update the correct row
#         location[row_number - 1][column_number - 1] = "X"

#         # Display updated grid
#         print("You hid the treasure here:")
#         print(f"{row1}\n{row2}\n{row3}")
#     else:
#         print("You input an invalid number. Please, input a valid one!")






import random

rock_pic = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_pic = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_pic = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = [rock_pic, paper_pic, scissors_pic]
number = random.randint(0, 2)
computer_choice = choices[number]
player_choice = input("Welcome to Rock, Paper, Scissors game!\n"
"Type R for rock, P for paper, and S for scissors: ").lower()
if player_choice not in ["r", "p", "s"]:
    print("PLease, input a valid letter!")
else:
    #if a player chooses rock
    if player_choice == "r":
        player_choice = rock_pic
        if computer_choice == player_choice:
            print(f"You chose: {rock_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "It is a draw!")
        elif number == 1:
            print(f"You chose: {rock_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You lose!")
        elif number == 2:
            print(f"You chose: {rock_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You win!")
    if player_choice == "p":
        player_choice = paper_pic
        if computer_choice == player_choice:
            print(f"You chose: {paper_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "It is a draw!")
        elif number == 2:
            print(f"You chose: {paper_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You lose!")
        elif number == 0:
            print(f"You chose: {paper_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You win!")
    if player_choice == "s":
        player_choice = scissors_pic
        if computer_choice == player_choice:
            print(f"You chose: {scissors_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "It is a draw!")
        elif number == 0:
            print(f"You chose: {scissors_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You lose!")
        elif number == 1:
            print(f"You chose: {scissors_pic}\n"
            f"The computer chose: {computer_choice}\n"
            "You win!")

        


# #the code suggested by chatgpt
# import random

# # ASCII art for each choice
# rock_pic = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper_pic = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors_pic = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# # Map choices to ASCII art and values
# choices = {
#     "r": {"name": "Rock", "art": rock_pic},
#     "p": {"name": "Paper", "art": paper_pic},
#     "s": {"name": "Scissors", "art": scissors_pic},
# }

# # Get computer's random choice
# computer_choice = random.choice(list(choices.keys()))

# # Get player's choice
# player_choice = input("Welcome to Rock, Paper, Scissors game!\n"
#                       "Type R for rock, P for paper, and S for scissors: ").lower()

# if player_choice not in choices:
#     print("Please input a valid letter!")
# else:
#     player_art = choices[player_choice]["art"]
#     computer_art = choices[computer_choice]["art"]
    
#     # Display choices
#     print(f"You chose:\n{player_art}")
#     print(f"The computer chose:\n{computer_art}")
    
#     # Determine the winner
#     if player_choice == computer_choice:
#         print("It's a draw!")
#     elif (player_choice == "r" and computer_choice == "s") or \
#          (player_choice == "p" and computer_choice == "r") or \
#          (player_choice == "s" and computer_choice == "p"):
#         print("You win!")
#     else:
#         print("You lose!")




































