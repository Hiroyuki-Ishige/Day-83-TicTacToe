from helpers import draw_board, check_turn, check_for_win
import os

spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

playing = True
turn = 0

while playing:
    # Reset the screen
    # os.system("cls" if os.name == "nt" else "clear")
    # os.system("cls")
    draw_board(spots)
    # get input from the player
    choice = input(f'It\'s your[{check_turn(turn)}] turn. Please select (1 to 9) from unselected spots,\n'
                   f'or press "q" to quit:')
    if choice == "q":
        playing = False
        print("Game is quite")
    # Check if player input number. If not number, back to begin of while
    elif not str.isdigit(choice):
        continue
    # Check if player input number 1-9
    elif not int(choice) in spots:
        continue

    else:
        # Check if spot is taken alreaday
        if spots[int(choice)] in {"X", "O"}:
            print("That number is already selected. Plaase select again")

        #Write "O" or "X" if spot isn't taken
        else:
            spots[int(choice)] = check_turn(turn)

            if check_for_win(spots) == True:
                print(f'\n----------------------------\n'
                      f'[{check_turn(turn)}] is win\n'
                      f'Thank you for playing!!\n'
                      f'----------------------------')
                playing = False

            turn += 1

    if turn >8:
        print("\n------------------------\n"
              "Game is ended with even\n"
              "Thank you for playing!!\n"
              "-------------------------")
        playing = False
