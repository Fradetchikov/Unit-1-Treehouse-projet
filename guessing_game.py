import random

def start_game():

    answer = random.randint(1, 10)
    print("Welcome to the Number Guessing Game! ")
    attempt_count = 1
    player_try = input("Please enter a number between 1 and 10: ")
    while player_try != answer:
        try:
            player_try = int(player_try)
        except ValueError:
            print("This is not a valid value. Try again ...")
            player_try = input("Please enter a number between 1 and 10: ")
        else:
            if player_try < 1 or player_try > 10:
                print("This is not a valid number. Please try again")
                player_try = input("Please enter a number between 1 and 10: ")
            elif player_try < answer:
                print("It is higher!")
                attempt_count += 1
                player_try = input("Please enter a number between 1 and 10: ")
            elif player_try > answer:
                print("It is lower")
                attempt_count += 1
                player_try = input("Please enter a number between 1 and 10: ")
            elif player_try == answer:
                print("This is the answer we want")
                if attempt_count == 1:
                    print("You took {} attempt".format(attempt_count))
                    print("Closing game, see you next time!")
                else:
                    print("You took {} attempts".format(attempt_count))
                    print("Closing game, see you next time!")

start_game()