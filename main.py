
from game import Game

game = Game()
game.initialize_player()
continuer = True


while continuer == True:
    while game.comparison() == True:
        game.launch_sequence() 
        game.comparison() 
    
        while game.comparison() == True:
            print("You lost, continue ? y/n: ")
            answer = input("")
            if answer == "n":
                continuer = False
        
    

