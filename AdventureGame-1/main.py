import pygame
import sys
from pygame.locals import QUIT
import time
import os

os.system('clear')


def introduction():
    os.system('clear')
    print("Welcome to Escape from Pocock Game featuring Zombies!\n")
    time.sleep(1)
    print(
        "You find yourself trapped in Philip Pocock Secondary School, overrun by zombies."
    )
    time.sleep(2)
    print(
        "Your mission is to escape the school and survive the zombie apocalypse!"
    )
    time.sleep(2)
    print("What is your name?")
    username = input().lower()
    print("Alright, " + username + ", let's begin...\n")


def game_over():
    print("\nOh no! The zombies got you.")
    pygame.init()
    X = 700
    Y = 700
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('image')
    imp = pygame.image.load("gameover.gif").convert()
    scrn.blit(imp, (0, 0))
    pygame.display.flip()
    time.sleep(2)
    print("Game over.")
    time.sleep(2)
    print("Better luck next time.")
    print("Do you want to play again? (yes/no)")
    while True:
        usersresponse = input().lower()
        if usersresponse == "yes":
            play_game()
        elif usersresponse == "no":
            print("Thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def knock_knock_joke():
    print("Knock, knock.")
    time.sleep(2)
    response = input("Who's there? (type hatch) ").strip().lower()
    if response == "hatch":
        print("Hatch who?")
        time.sleep(2)
        print("Bless you!\n")
        time.sleep(1)
        print(
            "You ran away from the first zombie by answering the joke correctly! Lucky you!"
        )
    else:
        print("You didn't answer the joke correctly!")
        game_over()


def choose_room():
    print("\nNow you are on the first floor of the school.")
    time.sleep(2)
    print("You can go to the cafeteria, the main office, or the music room.")
    time.sleep(2)
    while True:
        choice = input(
            "Where do you want to go? (cafeteria/main office/music room): "
        ).strip().lower()
        if choice == "cafeteria":
            return cafeteria()
        elif choice == "main office":
            return main_office()
        elif choice == "music room":
            return music_room()
        else:
            print("Invalid choice. Please choose again.")


def cafeteria():
    print("\nYou are in the cafeteria.")
    time.sleep(3)
    print("You find some canned food and water. You take them with you.")
    time.sleep(3)
    print("You hear noises coming from the hallway.")
    time.sleep(3)
    print("You go back to the first floor hallway.\n")
    time.sleep(3)
    while True:
        choice1 = input(
            "Now you decide whether to go to the second or third floor. Type (second/third) \n"
        ).strip().lower()
        if choice1 == "second":
            return "second"
        elif choice1 == "third":
            return "third"
        else:
            print("Invalid choice. Please choose again.")


def main_office():
    print("\nYou are in the main office.")
    time.sleep(3)
    print("You find a keycard on the reception desk.")
    time.sleep(3)
    print("You hear growling sounds nearby.")
    time.sleep(3)
    print("You go back to the first floor hallway.\n")
    time.sleep(3)
    while True:
        choice1 = input(
            "Now you decide whether to go to the second or third floor. Type (second/third) \n"
        ).strip().lower()
        if choice1 == "second":
            return "second"
        elif choice1 == "third":
            return "third"
        else:
            print("Invalid choice. Please choose again.")
    return "first floor hallway"


def second():
    print("\nYou are going upstairs and hearing someone behind you.\n")
    time.sleep(2)
    print("You are running as fast as you can and ...\n")
    time.sleep(3)
    print("You closed the door on time and escaped from that zombie!!!\n")
    time.sleep(3)
    print("You are in the second floor.\n")
    time.sleep(3)

    while True:
        choice3 = input(
            "You can go to the lifting room, science room, and religion room. Type (lifting, science, religion)\n"
        ).strip().lower()
        if choice3 == "lifting":
            return lifting()
        elif choice3 == "science":
            return science()
        elif choice3 == "religion":
            return religion()
        else:
            print("Invalid choice. Please choose again.")


def lifting():

    print("\nYou are in the lifting room.\n")
    time.sleep(3)
    print("You are trying to find some useful things to help you escape.")
    time.sleep(3)
    print("But you can't find any.")
    time.sleep(3)
    print("You hear growling sounds nearby.")
    time.sleep(3)
    print("You are trying to go to the exit, but...")
    time.sleep(3)
    print("You are trapped by zombies!")
    time.sleep(3)
    print("You should have not go to the gym.\n")
    time.sleep(2)
    game_over()


def science():
    print("\nYou are in the science room.\n")
    time.sleep(3)
    print("You found microscope and tried to think why would you need it for.")
    time.sleep(3)
    print("You realized that going to the science room was a stupid idea.")
    time.sleep(3)
    print("But it was too late ...")
    time.sleep(3)
    print("They surrounded you!\n")
    time.sleep(3)
    game_over()


def religion():
    print("\nYou are in the religion room.\n")
    time.sleep(3)
    print("You found a bible and a cross.")
    time.sleep(3)
    print("You can't think of where to use them.")
    time.sleep(3)
    print("You are thinking for a long time.")
    time.sleep(3)
    print(
        "You come up with two ideas, either to stay and pray or come back to the hallway. Type (pray/hallway)\n"
    )
    time.sleep(2)
    while True:
        choice4 = input().strip().lower()
        if choice4 == "pray":
            print("\nYou are praying for a long time.\n")
            time.sleep(3)
            print("And at some point you didn't hear these weird noises.")
            time.sleep(3)
            print(
                "You decided to look what happened and comeback to the hallway."
            )
            time.sleep(3)
            print("There was nobody here!")
            time.sleep(3)
            print("You are safe!\n")
            time.sleep(2)
            escape()

        elif choice4 == "hallway":
            print("Now you are in the hallway.\n")
            time.sleep(3)
            print("You see a lot of zombies here.\n")
            time.sleep(3)
            print("They all are looking at you.\n")
            time.sleep(3)
            print("You are trying to run away, but ...\n")
            time.sleep(3)
            print("You are trapped by zombies!\n")
            time.sleep(3)
            print("You realized that going out was a bad idea.\n")
            game_over()

        else:
            print("Invalid choice. Please choose again.")


def third():
    print("\nNow you are going to the third floor")
    time.sleep(2)
    print("You see Mr. Brady is lying on the floor with injury!\n")

    pygame.init()
    X = 700
    Y = 700

    # create the display surface object
    # of specific dimension..e(X, Y).
    scrn = pygame.display.set_mode((X, Y))

    # set the pygame window name
    pygame.display.set_caption('image')

    # create a surface object, image is drawn on it.
    imp = pygame.image.load("background (1).png").convert()

    # Using blit to copy content from one surface to other
    scrn.blit(imp, (0, 0))

    # paint screen one time
    pygame.display.flip()

    time.sleep(6)
    print("But you also see a lot of zombies catching up on you")
    time.sleep(2)

    choice2 = input(
        "\nNow you have to decide whether to help Mr. Brady or run away. Type (help/run)\n"
    ).strip().lower()
    while True:
        if choice2 == "help":
            print(
                "You are helping Mr. Brady and you are running away from the zombies with that person\n"
            )
            time.sleep(2)
            print(
                "You are running away from the zombies and you are running to the exit\n"
            )
            time.sleep(2)
            print("You almost there!\n")
            time.sleep(3)
            print("But It is too late already, there are too many zombies\n")
            time.sleep(3)
            print("They caught you and Mr. Brady! \n")
            game_over()
        elif choice2 == "run":
            print("You only said 'I am sorry' and ran away")
            time.sleep(2)
            print(
                "While running away you turned your head a bit and saw how zombies are eating Mr. Brady's body and you kept running\n"
            )
            time.sleep(2)
            print("\nYou are running to the exit\n")
            pygame.mixer.init()
            pygame.mixer.music.load("runawaymusic.mp3")
            pygame.mixer.music.play()

            time.sleep(15)
            print("\n...\n")
            time.sleep(5)
            print("And you escape but for the price of a human life...\n")
            time.sleep(5)
            escape()
        else:
            print("Invalid choice. Please choose again.")


def music_room():
    print("\nYou are in the music room.")
    time.sleep(2)
    print("You find an old guitar.")
    time.sleep(2)
    print("You hear footsteps approaching.")
    time.sleep(2)
    print("You go back to the first floor hallway.")
    time.sleep(2)
    while True:
        choice1 = input(
            "Now you decide whether to go to the second or third floor. Type (second/third) \n"
        ).strip().lower()
        if choice1 == "second":
            return "second"
        elif choice1 == "third":
            return "third"
        else:
            print("Invalid choice. Please choose again.")
    return "first floor hallway"


def escape():
    print(
        "\nCongratulations! You've escaped from Philip Pocock Secondary School and survived the zombie apocalypse!"
    )
    pygame.init()
    X = 700
    Y = 700
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('image')
    imp = pygame.image.load("win.jpeg").convert()
    scrn.blit(imp, (0, 0))
    pygame.display.flip()
    time.sleep(5)
    print("You are a true survivor.")
    time.sleep(3)
    print("Thanks for playing!")
    sys.exit()


def play_game():
    while True:
        introduction()
        knock_knock_joke()
        current_location = "first floor hallway"
        while True:
            if current_location == "first floor hallway":
                next_location = choose_room()
                if next_location == "cafeteria":
                    current_location = cafeteria()
                elif next_location == "main office":
                    current_location = main_office()
                elif next_location == "music room":
                    current_location = music_room()
                elif next_location == "third":
                    current_location = third()
                elif next_location == "second":
                    current_location = second()
            if current_location == "escape":
                if not escape():
                    return
                break
            if current_location == "game over":
                if not game_over():
                    return
                break


play_game()
