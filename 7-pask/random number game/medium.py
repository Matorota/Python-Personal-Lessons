import random
class Medium:

    def __init__(self):
        self.wins = 0
        self.lives = 5
        self.number = random.randint(0, 10)
        self.tries = 0
        self.winner = False



    def play(self):
        """Play"""
        print("you have 5 tries")
        while not self.winner:
            self.tries = self.tries + 1
            guess = int(input("Number from 0 - 10 guess"))
            if guess < self.number:
                print('Your guess is too low')
            if guess > self.number:
                print('Your guess is too high')
            if self.tries >= self.lives:
                print("You lost :( do you wanna continue?")
                self.winner = True
                choice = input()
                if choice == "Yes":
                    self.winner = False
                elif choice == "No":
                    self.winner = True
            if guess == self.number:
                print("CORRECT YOU WIN \n do you wanna continue?")
                self.winner = True
                choice = input()
                if choice == "Yes":
                    self.winner = False
                elif choice == "No":
                    self.winner = True