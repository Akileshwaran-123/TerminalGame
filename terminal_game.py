import random

def intro():
    print("Welcome to The Legend of Python: Terminal Adventure!")
    print("You are Alex, a brave explorer lost in the mysterious Forest of Loops.")
    print("Your goal: Escape the forest before your health runs out!")
    print("Let the adventure begin!\n")

def game():
    health = 10
    has_sword = False
    
    while True:
        print(f"\nYour health: {health}")
        print("You see two paths ahead.")
        print("1. Take the left path (deeper into the woods).")
        print("2. Take the right path (towards the sound of water).")
        choice = input("Which path do you choose? (1/2): ")

        if choice == "1":
            print("\nYou walk deeper into the woods and find a shiny sword!")
            has_sword = True
            print("But... a wild Python appears!")
            print("Do you want to:")
            print("a) Fight the Python")
            print("b) Run away")

            action = input("Choose a or b: ")
            if action == "a":
                if has_sword:
                    print("You defeat the Python with your new sword! You gain 2 health.")
                    health += 2
                else:
                    print("You try to fight with your bare hands. The Python bites you! You lose 4 health.")
                    health -= 4
            elif action == "b":
                print("You run, but trip over a root! You lose 2 health.")
                health -= 2
            else:
                print("You hesitate. The Python bites you! You lose 4 health.")
                health -= 4

        elif choice == "2":
            print("\nYou follow the sound and find a sparkling river.")
            print("Do you want to:")
            print("a) Drink the water")
            print("b) Rest by the riverbank")

            action = input("Choose a or b: ")
            if action == "a":
                outcome = random.choice(['good', 'bad'])
                if outcome == 'good':
                    print("The water refreshes you! You gain 3 health.")
                    health += 3
                else:
                    print("Oops! The water was contaminated. You lose 3 health.")
                    health -= 3
            elif action == "b":
                print("You rest and recover 2 health.")
                health += 2
            else:
                print("A mosquito bites you while you hesitate. You lose 1 health.")
                health -= 1

        else:
            print("\nInvalid choice. Please choose 1 or 2.")
            continue

        if health <= 0:
            print("\nYou have lost all your health. Game Over!")
            break
        elif health >= 20:
            print("\nCongratulations! You found your way out of the forest with great health!")
            break

        print("\nDo you want to keep adventuring or try again?")
        print("1. Continue")
        print("2. Quit")
        next_step = input("Choose 1 or 2: ")
        if next_step == "2":
            print("Thanks for playing! Goodbye adventurer.")
            break

if __name__ == "__main__":
    intro()
    game()