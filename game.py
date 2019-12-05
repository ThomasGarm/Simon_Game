from sequence import *
from player import *
import time
import os

class Game:
    def __init__(self):
        self.display = 1
        self.sequence = Sequence()
        self.player = Player()

    def initialize_player(self):
        self.player.user_name()

    def launch_sequence(self):
        self.sequence.random_sequence()
        for i in self.sequence.sequence:
            print(i)
            time.sleep(self.display)
            self.clear_screen()
            
    def clear_screen(self):
        os.system('clear' if os.name =='posix' else 'cls')

    def player_turn(self):
        self.play = input("Your turn !: ")
        self.clear_screen()

    def comparison(self):
        for self.play in self.sequence:
            if self.play == self.sequence:
                print("good")

    