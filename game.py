from sequence import *
from player import *
import time
import os

class Game:
    def __init__(self):
        self.display = 2
        self.sequence = Sequence()
        self.player = Player()

    def initialize_player(self):
        """insert player's attributes in game"""
        self.player.user_name()

    def launch_sequence(self):
        """get and display simon's sequences in amount of time"""
        self.sequence.random_sequence()
        for i in self.sequence.sequence:
            print(i)
            time.sleep(self.display)
            self.clear_screen()
            
    def clear_screen(self):
        """erase display on screen"""
        os.system('clear' if os.name =='posix' else 'cls')

    def player_turn(self):
        """get input from the player"""
        return int(input("Your turn !: "))
        

    def comparison(self):
        """simon's rules"""
        for element in self.sequence.sequence:
            player_choice = self.player_turn()
            self.clear_screen()
            if player_choice != element:
               return False
               
            