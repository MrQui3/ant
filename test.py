from pheromone import Pheromone

def b():
    a = 0
    for i in range(100000000):
        a += 1
    if a == 100000000:
        return True
    return False