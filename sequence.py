from random import randint
import threading

class Sequence:
    def __init__(self):
        self.sequence = []
        
        

    def random_sequence(self):
        self.sequence.append(randint(0,10))

