import random
import sys


class Ro_Pa_Sc:
    def __init__(self):
        print("!!Welcome to Rock Paper and Scissors!!")
        user_move: str = input("Rock, Paper or Scissor: ").lower()
        self.user_move = user_move

    def play_game(self):

        ai_move: str = random.choice(['rock', 'paper', 'scissor'])

        if self.user_move not in ['rock', 'paper', 'scissor']:
            return False
        else:
            self.check_move(ai_move, self.user_move)
            return True

    def check_move(self, ai_move: str, user_move: str):
        if ai_move == user_move:
            print("Tie!!")
        elif user_move == 'rock' and ai_move == 'scissors':
            print("You Win")
        elif user_move == 'scissors' and ai_move == 'paper':
            print("You Win")
        elif user_move == 'paper' and ai_move == 'rock':
            print("You Win")
        else:
            print("AI Wins")


def main():
    check_input = True
    while check_input:
        rps = Ro_Pa_Sc()
        check_input = rps.play_game()

        if check_input:
            play_again = input("Want to Play Again Y or N: ").lower()
            if play_again == 'y':
                main()
            else:
                print("Thanks for Playing!")
                sys.exit()
        else:
            print("Invalid Input...Check Again")
            main()


if __name__ == '__main__':
    main()
