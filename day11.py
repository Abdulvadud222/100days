import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")
def black_jack():
    global user_score, computer_score
    import random
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards_dic = {
        0: 'A',
        1: '2',
        2: '3',
        3: '4',
        4: '5',
        5: '6',
        6: '7',
        7: '8',
        8: '9',
        9: '10',
        10: 'J',
        11: 'Q',
        12: 'K'
        }
    def deal_card():
        """Return a random card from the deck"""
        random_index = random.randint(0, len(cards) - 1)
        random_card = cards[random_index]
        return random_card, random_index
    user_cards = []
    computer_cards = []
    user_cards_symbol = []
    computer_cards_symbol = []
    is_game_over = False
    for i in range(2):
        user_card, user_index = deal_card()
        user_cards.append(user_card)
        user_cards_symbol.append(cards_dic[user_index])
        computer_card, computer_index = deal_card()
        computer_cards.append(computer_card)
        computer_cards_symbol.append(cards_dic[computer_index])
    def calculate_score(list_of_cards):
        if 11 in list_of_cards:
            if 10 in list_of_cards:
                return 21
        overall_score = sum(list_of_cards)
        if 11 in list_of_cards:
            if overall_score > 21:
                list_of_cards.remove(11)
                list_of_cards.append(1)
                overall_score = sum(list_of_cards)
        return overall_score
    while not is_game_over:
        user_score = calculate_score(list_of_cards=user_cards)
        computer_score = calculate_score(list_of_cards=computer_cards)
        print(f"Here are your cards: {user_cards_symbol}, current_score: {user_score}")
        print(f"Here is the computer's card: {computer_cards_symbol[0]}")

        if user_score == 21:
            is_game_over = True
            print("You have a BlackJack! You win!")
        elif user_score > 21:
            is_game_over = True
            print("You are busted!")
        else:
            again = input("Do you wanna draw another card? Type y for yes or n for no:\n").lower()
            if again == "y":
                user_card, user_index = deal_card()
                user_cards.append(user_card)
                user_cards_symbol.append(cards_dic[user_index])
            else:
                is_game_over = True
    if user_score <= 21:
        while computer_score != 21 and computer_score < 17:
            computer_card, computer_index = deal_card()
            computer_cards.append(computer_card)
            computer_cards_symbol.append(cards_dic[computer_index])
            computer_score = calculate_score(computer_cards)
    def compare(user_score, computer_score):
        global should_continue
        if user_score == computer_score:
            message = "It is a draw"
        elif computer_score == 0:
            message = "Computer has a BlackJack. You lose!"
            should_continue = False
        elif user_score > 21:
            message = "You are busted. You lose!"
        elif computer_score > 21:
            message = "Computer is busted. You win!"
        else:
            if user_score > computer_score:
                message = "You win!"
            else:
                message = "You lose!"
        return message
    print(f"Your final hand: {user_cards_symbol}, final score: {user_score}")
    print(f"computer's final hand: {computer_cards_symbol}, final score: {computer_score}")
    print(compare(user_score, computer_score))

should_continue = True
while should_continue:
    play_again = input("Do you wanna play the game? If yes type y, otherwise n:\n").lower()
    if play_again == "y":
        clear_console()
        black_jack()
        should_continue = True
    elif play_again == "n":
        print("Exiting...")
        should_continue = False
    else:
        print("Invalid input! Exiting...")
        should_continue = False
