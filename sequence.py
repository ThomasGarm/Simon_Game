from random import randint


class Sequence:
    def __init__(self):
        self.number = []
        self.last_number = None   
        
    def random_sequence(self): #get a random integer
        self.number.append(randint(0, self.last_number))