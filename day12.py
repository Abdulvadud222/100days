logo = """
 ######   ##     ## ########  ######   ######     ######## ##     ## ########    ##    ## ##     ## ##     ## ########  ######## ########  
##    ##  ##     ## ##       ##    ## ##    ##       ##    ##     ## ##          ###   ## ##     ## ###   ### ##     ## ##       ##     ## 
##        ##     ## ##       ##       ##             ##    ##     ## ##          ####  ## ##     ## #### #### ##     ## ##       ##     ## 
##   #### ##     ## ######    ######   ######        ##    ######### ######      ## ## ## ##     ## ## ### ## ########  ######   ########  
##    ##  ##     ## ##             ##       ##       ##    ##     ## ##          ##  #### ##     ## ##     ## ##     ## ##       ##   ##   
##    ##  ##     ## ##       ##    ## ##    ##       ##    ##     ## ##          ##   ### ##     ## ##     ## ##     ## ##       ##    ##  
 ######    #######  ########  ######   ######        ##    ##     ## ########    ##    ##  #######  ##     ## ########  ######## ##     ## 
"""
level = input(f"{logo}\n\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100\nChoose a difficulty. Type 'easy' or 'hard': ").lower()



def easy_version():
    import random
    number = random.randint(1, 100)
    lives = 10
    guess = int(input(f"You have {lives} attempts remaining to guess a number\nMake a guess: "))
    while lives:
        if guess == number:
            print("Congratulations! You win!"
                  f"\nIt was {number}")
            break
        else:
            if guess > number:
                if lives > 0:
                    guess = int(input(f"Too high.\nYou have {lives} attempts remaining to guess a number\nGuess again: "))
                    lives -= 1
                
            else:
                if lives > 0:
                    guess = int(input(f"Too low.\nYou have {lives} attempts remaining to guess a number\nGuess again: "))
                    lives -= 1
                
        if lives == 0:
            print("You ran out of attempts( You lose!"
                  f"\nIt was {number}")


def hard_version():
    import random
    number = random.randint(1, 100)
    lives = 5
    guess = int(input(f"You have {lives} attempts remaining to guess a number\nMake a guess: "))
    lives -= 1
    while lives:
        if guess == number:
            print("Congratulations! You win!"
                  f"\nIt was {number}")
            break
        else:
            if guess > number:
                if lives > 0:
                    guess = int(input(f"Too high.\nYou have {lives} attempts remaining to guess a number\nGuess again: "))
                    lives -= 1
                
            else:
                if lives > 0:
                    guess = int(input(f"Too low.\nYou have {lives} attempts remaining to guess a number\nGuess again: "))
                    lives -= 1
                
        if lives == 0:
            print("You ran out of attempts( You lose!"
                  f"\nIt was {number}")    

def direction(level):
    if level == "easy":
        easy_version()
    else:
        hard_version()

direction(level)


