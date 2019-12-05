
from game import Game

game = Game()
game.initialize_player()
continuer = True

while continuer:
    game.launch_sequence() 
    game.comparison() 
    if game.comparison() == "n":
        continuer = False

