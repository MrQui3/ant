import home
import random

class Ant:
    def __init__(self):
        self.position = (random.randint(10, 590), random.randint(10, 590))
        self.size = (5, 10)
