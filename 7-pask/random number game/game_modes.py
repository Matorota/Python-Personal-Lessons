import random
class Easy:
    def __init__(self):
        self.wins = 0
        self.lives = 3
        self.number = random.randint(0, 100)
        self.tries = 0
        self.is_on  = True

    def set_difficulty(self):
            choose_difficulty = input("Choose difficulty: easy, medium, hard")
            if choose_difficulty == 'easy':
                self.lives = 20
            elif choose_difficulty == 'medium':
                self.lives = 15
            elif choose_difficulty == 'hard':
                self.lives = 10
            #version need fixing this one play
    # def play(self):
    #     """Play"""
    #     print("you have 3 tries")
    #     while not self.winner:
    #         guess = int(input("Number from 0 - 10 guess"))
    #         if guess < self.number:
    #             print('Your guess is too low')
    #         if guess > self.number:
    #             print('Your guess is too high')
    #         if guess == self.number:
    #             print("CORRECT YOU WIN \n do you wanna continue?")
    #             self.winner = True
    #             self.wins + 1
    #             print(f"you won {self.wins}")
    #             choice = input()
    #             if choice == "Yes":
    #                 self.winner = False
    #             elif choice == "No":
    #                 self.winner = True
    #         if guess == self.number:
    #             print('You guessed the number in ' + str(self.tries) + ' tries!')
    #         else:
    #             print('You did not guess the number, The number was ' + str(self.number))



    def play(self):
        """ Play's the game """
        self.set_difficulty()
        while self.is_on:
            guess = int(input(f"Input your number (0 - 100)"))
            self.tries = self.tries + 1
            if guess == self.number:
                print(f"Congrats, you guessed the right number: {self.number}\n Your remaining lives were: {self.lives - self.tries}")
                self.is_on = False
            elif guess > self.number:
                print(f"▼   Your remaining lives: {self.lives -self.tries}")
                if self.tries >= self.lives:
                    print("You lost :(")
                    self.is_on = False
            elif guess < self.number:
                print(f"▲  ||  Your remaining lives: {self.lives -self.tries}")
                if self.tries >= self.lives:
                    print("You lost :(")
                    self.is_on = False






