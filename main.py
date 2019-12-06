
from game import Game

game = Game()
continuer = True

if __name__ == "__main__":
    game.initialize_player() #call the player name
    game.level_difficulty() #player choose between three level of difficulty
while continuer:
    game.launch_sequence() #display random integer
    if game.comparison() == False: #if player is wrong
        end =input("continue?\n y/n?").lower()
        try:
            assert end == "n"
        except AssertionError as a:
            pass
        if end == "n":
                continuer = False
        
        
    

