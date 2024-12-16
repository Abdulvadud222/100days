# dic_tionary = {
#     "commonsense": "A valuable and very rare asset that people are supposed to have but don't have.",
#     "AI": "The very advancement of twenty first century that is believed to revolutionize the field of IT particularly.",
# }

# dic_tionary["money"] = "the root of all evil."
# for thing in dic_tionary:
#     print(thing)
#     print(dic_tionary[thing])


# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Nerville": 62,
# }

# student_grades = {}
# for student_score in student_scores:
#     score = student_scores[student_score]
#     if score >= 91:
#         student_grades[student_score] = "Outstanding"
#     elif 81 <= score <= 90:
#         student_grades[student_score] = "Exceeds Expectation"
#     elif 71 <= score <= 80:
#         student_grades[student_score] = "Acceptable"
#     else:
#         student_grades[student_score] = "Fail"
# print(student_grades)


# ###nesting
# capitals = {
#     "France": "paris",
#     "Germany": "Berlin",
# }
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stutgart"]
# }

# travel_log = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12,
#     },
#     {
#     "country": "Germany", 
#     "cities_visited": ["Berlin", "Hamburg", "Stutgart"],
#     "total_visits": 25
#     },
# ]
# def add_new_country(country_name, number_of_visited_cities, list_of_cities):
#     travel_log.append(
#         {
#         "country": country_name,
#         "cities_visited": list_of_cities,
#         "total_visits": number_of_visited_cities
#         },
#         )
# add_new_country("Russia", 2, ["Moscow", "Saint Peterburg", "Kazan"])
# print(travel_log)



import os
def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f"{logo}\n"
      "Welcome to Secret-Auction\n"
      "\n" "Today, this amazing watch is in Auction\n")
name_of_bidder = input("What's your name: ")
amount_of_bid = int(input("\nWhat's your bid: $"))
another_bidder = input("Is there any another person who wants to bid? Yes or No\n").lower()
bidder_list = {}
def winner_bidder(name, amount):
    bidder_list[name] = amount
winner_bidder(name=name_of_bidder, amount=amount_of_bid)
clear_console()
while another_bidder != "no":
    print(f"{logo}\n"
      "Welcome to Secret-Auction\n"
      "\n" "Today, this amazing watch is in Auction")
    name_of_bidder = input("What's your name: ")
    amount_of_bid = int(input("What's your bid: $"))
    another_bidder = input("Is there any other person who wants to bid? Yes or No\n").lower()
    winner_bidder(name=name_of_bidder, amount=amount_of_bid)
    clear_console()

clear_console()
winner = ""
winning_amount = 0
for key, value in bidder_list.items():
    if value > winning_amount:
        winning_amount = value
        winner = key
print(f"The winner is {winner} with the bid of {winning_amount}$")
        
    




















