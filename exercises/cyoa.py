"""EX06 - Choose your own adventure: an...atempt at Tamagotchi."""

__author__: str = "730390832"


player: str = ""
pet_name: str = ""
points: dict[str, int] = {"age": 1, "bored": randint(0, 100), "food": randint(0, 100), "exhausted": randint(0, 100), "health": 100}

BIRTHDAY_CAKE: str = "\U0001F382"
FOOD: str = "\U0001F35B"
HEALTH: str = "\U0001F49A"
QUIT: str = "\U0001F6D1"
PLAY: str = "\U0001F4A8"
WAIT: str = "\U000023F3"
PET: str = "\U0001F431"
WASH: str = "\U0001F6C1"
RIP: str = "\U00002620"
EMERGENCY: str = "\U0001F6A8"


# menu options
def tama_quit() -> None:
    health()
    print(f"\nさようなら (farewell) {player}-さん, {pet_name} will miss you!! (◕︿◕✿)")
    quit()

from random import randint


def tama_feed() -> None:
    """Action for option 'food'."""
    global points
    points["bored"] -= randint(5, 10)
    points["food"] += randint(10, 30)
    points["exhausted"] -= randint(10, 20)
    points["health"] += randint(-5, 20)
    print(f"\n\t\t\t{FOOD}{FOOD}{FOOD} om nom nom... {FOOD}{FOOD}{FOOD}")


def tama_play() -> None:
    """Action for option 'play'."""
    global points
    points["bored"] -= randint(10, 30)
    points["food"] -= randint(10, 20)
    points["exhausted"] += randint(10, 20)
    points["health"] += randint(-5, 20)
    print(f"\n\t\t\t{PLAY}{PLAY}{PLAY} racecar-like zoomies... {PLAY}{PLAY}{PLAY}")


def tama_clean() -> None:
    """Action for option 'clean'."""
    global points
    points["bored"] += randint(10, 20)
    points["food"] -= randint(5, 10)
    points["exhausted"] += randint(5, 20)
    points["health"] += randint(-5, 20)
    print(f"\n\t\t\t{WASH}{WASH}{WASH} srub a dub dub... {WASH}{WASH}{WASH}")


def tama_wait() -> None:
    global points
    points["bored"] += randint(5, 20)
    points["food"] -= randint(-10, 20)
    points["exhausted"] -= randint(10, 20)
    points["health"] -= randint(-5, 20)
    print(f"\n\t\t\t{WAIT}{WAIT}{WAIT} tik tok... {WAIT}{WAIT}{WAIT}")


# greet fuction
def greet() -> None:
   global player
   player = input("What is your name? ")
   print(f"\n{player}-さん, よろしくお願いします！(nice to meet you!)\n\nToday you will play a pet simulator inspired by たまごっち (tamagotchi, \"Egg Watch\"), a handheld digital pet created in Japan.\nYou will get to name your pet, feed them, wash them, and play with them.\nYou will also get to watch them age!\nBut take exemplary care of your new friend, or they will meet an untimely end (ノ_<、)\nYour new friend is waiting for you - じゃあ、初めって！(lets begin!)\n\n\t\t┏(-_-)┛┗(-_- )┓\n\n")


# paths 
def menu() -> None:
    """Prints player option menu."""
    print(f"\nWhen prompted, enter the letter that corresponds with your desired action.")
    option_menu: dict[str, str] = {"Quit game": "Q", "Feed": "F", "Play": "P", "Clean": "C", "Wait": "W"}
    for option in option_menu:
        print(f"{option_menu[option]}: \t{option}")


# points 
def health() -> None:
    """Prints user points / pet status."""
    print(f"\n\t\t\t{HEALTH}{HEALTH}{HEALTH} {pet_name}'s status {HEALTH}{HEALTH}{HEALTH} :")
    for category in points:
        print(f"\t\t{category} -> {points[category]}")
    print(f"note - to take great care of {pet_name}: try to maximize health & food, and minimize exhaustion & boredom as much as possible.")


# path chosen simulator procedure 
def tamagotchi() -> None:
    """Informs and initiates simulator paths."""
    menu()
    option: str = input(f"\n\nこんにちは (hello) {player}! What would you like to do with {pet_name} today?\n {PET}: ").upper()
    option_chosen: bool = False 
    while option_chosen is False:
        if option == "Q":
            option_chosen = True
            tama_quit()
        elif option == "F":
            option_chosen = True
            tama_feed()
        elif option == "P":
            option_chosen = True
            tama_play()
        elif option == "C": 
            option_chosen = True
            tama_clean()
        elif option == "W":
            option_chosen = True
            tama_wait()
        else:
            option = input("That wasn't an available option! Please try again (づ ◕‿◕ )づ: ")
    
# custom function - boost
def tama_boost(health_points: int, save_choice: str) -> int:
    """If low health, player can choose to accept a boost in health."""
    if save_choice == "Y":
        health_points += 50
        print(f"\nDon't worry {player}, {pet_name}'s health was boosted by 50.")
    if save_choice == "N":
        health_points += 0
        print(f"\nYou left it up to fate!")
    return health_points


# simulator main loop
def main() -> None:
    """The entrypoint of the program and main game loop."""
    greet()
    global pet_name
    pet_name = input("What would you like to name your pet? ")
    health()
    # game loop here 
    global points
    while points["exhausted"] < 200 and points["health"] > 0 and points["food"] > 0:
        # allow user to continue on same path, choose new path (action), or stop playing
        tamagotchi()
        points["age"] += 1
        if points["health"] < 20:
            save_choice: str = input(f"\n{EMERGENCY}{EMERGENCY}{EMERGENCY} {player}, {pet_name} is facing a medical crisis!\nWould you like a health boost to potentially save them? [Y] Yes or [N] No? ").upper()
            save_option_chosen: bool = False
            while save_option_chosen is False:
                if (save_choice == "Y") or (save_choice == "N"):
                    save_option_chosen = True
                    tama_boost(points["health"], save_choice)
                else:
                    save_choice = input("That wasn't an available option! Please try again (づ ◕‿◕ )づ: ")
        health()
    print(f"\n\n\t\t\t\t\tI'm so so sorry {player}, {pet_name} has died ˚‧º·(˃̣̣̥⌓˂̣̣̥)‧º·˚")
    print(f"\n\n\t\t\t\t\t\t---- {RIP} HERE LIES {pet_name}: {BIRTHDAY_CAKE} {points['age']} {RIP} ---- ")


if __name__ ==  "__main__":
    main()