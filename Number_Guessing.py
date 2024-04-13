import random
import sys


def difficulty_level():
    level_guess = True
    diff_level = 0
    while level_guess:
        level = input("Enter the Difficulty Level.. Easy/Hard: ").lower()
        if level == 'easy' or 'hard':
            if level == 'easy':
                diff_level = 6
                level_guess = False
            else:
                diff_level = 4
                level_guess = False
        else:
            continue
    return diff_level


def main():
    print("=================================")
    print("Welcome to Number Guessing Game")
    print("=================================")

    is_guess = True

    number = random.randint(1, 10)

    No_Attempts = difficulty_level()

    while is_guess:
        choice = int(input("Enter a Number to Guess: "))
        if choice < number:
            No_Attempts -= 1
            print("Number is Less")
            print(f"You have {No_Attempts} left")
            if No_Attempts == 0:
                print("!! You Lost the Game ||")
                is_guess = False
        elif choice > number:
            No_Attempts -= 1
            print("Number is Bigger")
            print(f"You have {No_Attempts} left")
            if No_Attempts == 0:
                print("!! You Lost the Game ||")
                is_guess = False
        else:
            print("You Win, You Guessed it Correctly")
            print(f"Number is {number}")
            play_again = input("Want to Play Again, enter Yes/No: ").lower()
            if play_again == 'no':
                print("Bye!!! See you Again")
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
