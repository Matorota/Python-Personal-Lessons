import random
class Easy:
    def __init__(self):
        self.wins = 0
        self.lives = 3
        self.number = random.randint(0, 10)
        self.tries = 0
        self.winner = False


    def play(self):
        """Play"""
        print("you have 3 tries")
        while not self.winner:
            guess = int(input("Number from 0 - 10 guess"))
            if guess < self.number:
                print('Your guess is too low')
            if guess > self.number:
                print('Your guess is too high')
            if guess == self.number:
                print("CORRECT YOU WIN \n do you wanna continue?")
                self.winner = True
                self.wins + 1
                print(f"you won {self.wins}")
                choice = input()
                if choice == "Yes":
                    self.winner = False
                elif choice == "No":
                    self.winner = True
            if guess == self.number:
                print('You guessed the number in ' + str(self.tries) + ' tries!')
            else:
                print('You did not guess the number, The number was ' + str(self.number))






