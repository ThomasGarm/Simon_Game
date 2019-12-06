from sequence import Sequence
from player import Player
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

    #def initialize_sequence(self):
        #self.sequence.random_sequence()

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
        self.difficulty = input("Choose the difficulty : easy, medium, hard: \n").lower()
        try:
            assert self.difficulty == "easy" or self.difficulty == "medium" or self.difficulty == "hard"
        except AssertionError as a:
            return self.level_difficulty()


    def display_difficulty(self):
        """set the speed of display"""
        if self.difficulty == "easy":
            self.display = 3
        if self.difficulty == "medium":
            self.display = 2
        if self.difficulty == "hard":
            self.display = 1
        return self.display

    """def random_difficulty(self): # set the range of self.number
        if self.difficulty == "easy":
            self.sequence.last_number = 10
        if self.difficulty == "medium":
            self.sequence.last_number = 50
        if self.difficulty == "hard":
            self.sequence.last_number = 100
        return self.sequence.last_number"""

    

               
            