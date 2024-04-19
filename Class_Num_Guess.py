import random
import sys


class Guess:
    def __init__(self):
        print("=================================")
        print("Welcome to Number Guessing Game")
        print("=================================")

        try:
            print("Choose Game Level i.e. 0-> Easy, 1-> Medium, 3 -> Difficult")
            attempts = int(input("Choose the difficulty level either 0/1/2: "))
            if attempts == 0:
                Num_Attempts = 8
            elif attempts == 1:
                Num_Attempts = 6
            else:
                Num_Attempts = 4
            self.attempts = Num_Attempts
        except ValueError:
            self.attempts = 2
            print(f"Error: Invalid input, hence the default attempts is {self.attempts}")

    def Guess_Number(self):
        number = random.randint(1, 10)
        is_guess = True

        try:
            while is_guess:
                num = int(input("Enter a Number: "))

                print(f"User Number: {num}")

                if num > number:
                    print("Number is Greater")
                    self.attempts -= 1
                    print(f"No of Attempts Left: {self.attempts}")
                    if self.attempts == 0:
                        print("No More Attempts Left: You Loose the Game")
                        return True
                elif num < number:
                    print("Number is Less")
                    self.attempts -= 1
                    print(f"No of Attempts Left: {self.attempts}")
                    if self.attempts == 0:
                        print("No More Attempts Left: You Loose the Game")
                        return True
                else:
                    print("!! Your Guess is Correct. You Win !!")
                    return False
        except ValueError:
            print("Error!! Invalid Input, Enter only digits")
            return False


def main():
    no_attmpt = True

    while no_attmpt:
        n1 = Guess()
        na = n1.Guess_Number()
        if na:
            play_again = input("Want to Play Again!! Yes/No: ").lower()
            if play_again == 'yes':
                main()
            else:
                print("Have a good day!!")
                sys.exit()
        else:
            play_again = input("Want to Play Again!! Yes/No: ").lower()
            if play_again == 'yes':
                main()
            else:
                print("Have a good day!!")
                sys.exit()


if __name__ == '__main__':
    main()
