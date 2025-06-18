# Turtle casino
import turtle

import tug_game
from race_game import turtle_race

money = 1000
print(r"""
 _________  __  __   ______   _________  __       ______       ______   ________   ______    ________  ___   __    ______      
/________/\/_/\/_/\ /_____/\ /________/\/_/\     /_____/\     /_____/\ /_______/\ /_____/\  /_______/\/__/\ /__/\ /_____/\     
\__.::.__\/\:\ \:\ \\:::_ \ \\__.::.__\/\:\ \    \::::_\/_    \:::__\/ \::: _  \ \\::::_\/_ \__.::._\/\::\_\\  \ \\:::_ \ \    
   \::\ \   \:\ \:\ \\:(_) ) )_ \::\ \   \:\ \    \:\/___/\    \:\ \  __\::(_)  \ \\:\/___/\   \::\ \  \:. `-\  \ \\:\ \ \ \   
    \::\ \   \:\ \:\ \\: __ `\ \ \::\ \   \:\ \____\::___\/_    \:\ \/_/\\:: __  \ \\_::._\:\  _\::\ \__\:. _    \ \\:\ \ \ \  
     \::\ \   \:\_\:\ \\ \ `\ \ \ \::\ \   \:\/___/\\:\____/\    \:\_\ \ \\:.\ \  \ \ /____\:\/__\::\__/\\. \`-\  \ \\:\_\ \ \ 
      \__\/    \_____\/ \_\/ \_\/  \__\/    \_____\/ \_____\/     \_____\/ \__\/\__\/ \_____\/\________\/ \__\/ \__\/ \_____\/ 
                                                                                                                               """)

print("Welcome to the Turtle Casino!")
while money > 0:
    game = input("What do you want to play?\n"
                 "1. Turtle Race\n"
                 "2. Turtle Tug-of-War\n"
                 "3. Exit\n")

    if game.strip().lower() in ["turtle race", "1"]:
        print("Time for a Turtle Race!")
        bet = input("How much would you like to bet?\n")
        money -= int(bet)
        turtle_choice = input("Which turtle would you like to race?\n"
                       "0. Red Turtle\n"
                       "1. Blue Turtle\n"
                       "2. Green Turtle\n"
                       "3. Yellow Turtle\n"
                       "4. Orange Turtle\n"
                       "5. Purple Turtle\n"
                       "6. Pink Turtle\n"
                       "7. Brown Turtle\n"
                       "8. Black Turtle\n"
                       "9. White Turtle\n")
        if turtle_choice not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Invalid turtle")
            quit()
        int(turtle_choice)

        winner = turtle_race(bet, turtle_choice)
        print("The winner is:", winner)
        turtles = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white"]
        if winner == turtles[int(turtle_choice)]:
            print("You win!")
            money += int(bet) * 2
            print("Your new balance is:", money)
        else:
            print("You lose!")
            print("Your new balance is:", money)

    elif game.strip().lower() in ["turtle tug-of-war", "2"]:
        print("Time for a game of Turtle Tug-of-War!")
        bet = input("How much would you like to bet?\n")
        money -= int(bet)
        turtle_choice = input("Which turtle team would you like to tug?\n"
                       "0. Team Mud (Green)\n"
                       "1. Team Grass (Brown)\n")
        if turtle_choice not in ["0", "1"]:
            print("Invalid team")
            quit()
        int(turtle_choice)

        winner = tug_game.turtle_tug(bet, turtle_choice)
        print("The winner is:", winner)
        turtles = ["mud", "grass"]
        if winner == turtles[int(turtle_choice)]:
            print("You win!")
            money += int(bet) * 2
            print("Your new balance is:", money)
        else:
            print("You lose!")
            print("Your new balance is:", money)



