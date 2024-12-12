# # Challenge 1: even/odd checker
# number = float(input("Please, input the number to be checked: "))
# if number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")

# # Challenge 2: Leap year checker
# year  = int(input("Please, input the year to be checked: "))
# if year % 400 == 0:
#     print("It is a leap year")
# elif year % 4 == 0  and year % 100 != 0:
#     print("It is a leap year")
# else:
#     print("It is not a leap year")

# # Challenge 3: Pizza order

# print("Welcome to Python Pizza Deliveries!")
# size  = input("What size do you want - (S)mall, (M)edium, or (L)arge? \n"
#               "Input the first letter of the chosen size: ").lower()
# pepperoni = input("Do you want pepperoni - (Y)es or (N)o\n"
#                   "Input the first letter: ").lower()
# cheese = input("Do you want cheese - (Y)es or (N)o\n"
#                   "Input the first letter: ").lower()
# bill = 0
# if size not in ["s", "m", "l"]:
#     print("Invalid input for size! Please restart.")
# else:
#     if size == "s":
#         bill += 15
#     elif size == "m":
#         bill += 20
#     elif size == "l":
#         bill += 25
#     if pepperoni == "y":
#         if size == "s":
#          bill += 2
#         else: 
#          bill += 3
#     if cheese == "y":
#         bill += 1
#     print(f"Your final bill is ${bill}")

# # Challenge 4: Love calculator
# print("Welcome to the Love calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()
# name1_list = list(name1)
# name2_list = list(name2)
# final_list = [*name1_list, *name2_list]
# true = 0
# for i in final_list:
#     if i in ["t", "r", "u", "e"]:
#         true += 1
# love = 0 
# for j in final_list:
#     if j in ["l", "o", "v", "e"]:
#         love += 1
# true_string = str(true)
# love_string = str(love)
# final_number = true_string + love_string
# final_number_int = int(final_number)

# if final_number_int < 10 or final_number_int > 90:
#     print(f"Your score is {final_number_int}. You go together like coke and mentos")
# elif 40 <= final_number_int <= 50:
#     print(f"Your score is {final_number_int}. You are alright together")
# else:
#     print(f"Your score is {final_number_int}.")


# # The last challenge: Creating a treasure island
# treasure_chest = (
#     "*******************************************************************************\n"
#     "          |                   |                  |                     |\n"
#     " _________|________________.=\"\"_;=.______________|_____________________|_______\n"
#     "|                   |  ,-\"_,=\"\"     `\"=.|                  |\n"
#     "|___________________|__\"=._o`\"-._        `\"=.______________|___________________\n"
#     "          |                `\"=._o`\"=._      _`\"=._                     |\n"
#     " _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______\n"
#     "|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |\n"
#     "|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________\n"
#     "          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |\n"
#     " _________|___________| ;`-.o`\"=._; .\" ` '`.\"\\` . \"-._ /_______________|_______\n"
#     "|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |\n"
#     "|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________\n"
#     "____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/___\n"
#     "/______/______/______/_""\"""=._o--._     ;o|o;        ; ;/______/______/______/\n"
#     "/______/______/______/""\"""=._o--._   ;o|o;     _._;o;____/______/______/______/\n"
#     "/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_____/\n"
#     "/______/______/______/________\"=.o|o_.--\"\"___/______/______/______/______/___/\n"
#     "*******************************************************************************\n"
# )
# print(treasure_chest)
# print("Welcome to Treasure Island!\n"
# "Your mission is to find the treasure.")
# left_or_right = input("You are at a cross road. Where do you wanna go - (L)eft or (R)ight? Type the first letter: ").lower()
# if left_or_right not in ["l", "r"]:
#     print("Invalid letter. Restart!")
# else:
#     if left_or_right == "l":
#         print("You come to a dark lake. There is an island in the middle of the lake. You have to go there")
#         swim_or_wait = input("Type (S) to swim through the lake or type (W) to wait for a boat: ").lower()
#         if swim_or_wait not in ["s", "w"]:
#             print("Invalid letter. Restart!")
#         else:
#             if swim_or_wait == "s":
#                 print("Well, the lake turns out to be acidic. You are dead!")
#             else:
#                 print("You successfully crossed the lake. Now you are on the Island\n"
#                 "But the problem is that there is a person guarding the treasure. You have to fight with him")
#                 fight_or_wrestle = input("Choose (F) to fistfight or (W) to wrestle with him!: ").lower()
#                 if fight_or_wrestle not in ["f", "w"]:
#                     print("Invalid letter. Restart!")
#                 else:
#                     if fight_or_wrestle == "f":
#                         print("You won in the fistfight! The treasure is yours! Congrats)")
#                     else:
#                         print("The guard is a 10-time world champion in wrestling. You lose(")
#     else:
#         print("You found an old plane. You have two options: Fly it yourself or Call your friend who knows how to fly it.")
#         fly_or_call = input("Type (F) to fly it yourself or (C) to call: ").lower()
#         if fly_or_call not in ["f", "c"]:
#             print("Invalid letter. Restart!")
#         else:
#             if fly_or_call == "f":
#                 print("You messed up bro. You hit the plane into the tree and fell. You are dead!")
#             else:
#                 print("You successfully crossed the lake. Now you are on the Island\n"
#                 "But the problem is that there is a person guarding the treasure. You have to fight with him")
#                 fight_or_wrestle = input("Choose (F) to fistfight or (W) to wrestle with him!: ").lower()
#                 if fight_or_wrestle not in ["f", "w"]:
#                     print("Invalid letter. Restart!")
#                 else:
#                     if fight_or_wrestle == "f":
#                         print("You won in the fistfight! The treasure is yours! Congrats)")
#                     else:
#                         print("The guard is a 10-time world champion in wrestling. You lose(")



















