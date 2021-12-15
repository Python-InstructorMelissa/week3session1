import random
from .user import User

class Game:
    def __init__(self):
        self.answer = 0
        self.leave = 0
        self.game = True


    def getRandomNumber(self):
        self.answer = random.randint(1, 11)
        self.answer
        return self.answer
    
    def checkInput(self, choice, player):
        if choice > 10 or choice < 1:
            message = print("Number is out of range\n")
            self.leave = 0
            return self.leave
        else:
            if choice == self.answer:
                message = print(f"Great guess {player.name}!\n{choice} was the correct answer")
                self.leave = 1
                self.game = False
                return self.game
            else:
                message = print("Sorry wrong answer try again\n")
                if choice > self.answer:
                    message = print(f"Your guess of {choice} was to high")
                    self.leave = 0
                    return self
                else:
                    message = print(f"Your guess of {choice} was too low")
                    self.leave = 0
                    return self
    
    def start(self):
        self.getRandomNumber()
        game = True
        while game:
            userName = str(input("Please let us know your name:  "))
            player = User(userName)
            player.printUser()
            message = print("You have 3 tries to guess the right number\n")
            round = [1,2,3]
            for r in round:
                if r == 1 or 2:
                    message = print(f"Round {r}")
                    choice = input(f"{player.name}, please pick a number between 1 and 10\n")
                    choice = choice.split()
                    self.checkInput(int(choice[0]), player)
                    if self.leave == 1:
                        return game == False
                else:
                    message = print(f"Round {r}")
                    choice = input(f"Please pick a number between 1 and 10\n")
                    choice = choice.split()
                    self.checkInput(int(choice[0]), player)
                    if self.leave == 1:
                        return game == False
            message = print(f"The answer was {self.answer}")
            message = print(f"Sorry out of rounds\n")
            self.leave = 1
            return game == False
