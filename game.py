from sequence import *
from player import *
import time
import os

class Game:
    def __init__(self):
        self.display = None
        self.sequence = Sequence()
        self.player = Player()

    def initialize_player(self):
        """insert player's attributes in game"""
        self.player.user_name()

    def launch_sequence(self):
        """get and display simon's sequences in amount of time"""
        self.sequence.random_sequence()
        for i in self.sequence.number:
            print(i)
            time.sleep(self.display_difficulty())
            self.clear_screen()
            
    def clear_screen(self):
        """erase display on screen"""
        os.system('clear' if os.name =='posix' else 'cls')

    def player_turn(self):
        """get input from the player"""
        return int(input("Your turn !: "))
        

    def comparison(self):
        """simon's rules: check if the input is the same than sequence"""
        for element in self.sequence.number:
            player_choice = self.player_turn()
            self.clear_screen()
            if player_choice != element:
               return False

    def level_difficulty(self):
        self.difficulty = input("Choose the difficulty : easy, medium, hard: \n")


    def display_difficulty(self):
        if self.difficulty == "easy":
            self.display = 3
        if self.difficulty == "medium":
            self.display = 2
        if self.difficulty == "hard":
            self.display = 1
        return self.display

               
            