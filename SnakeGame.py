import random
from Vector import Vector
import Constants

class SnakeGame:
    head: Vector
    body: list[Vector]
    direction: Vector
    food: Vector

    def __init__(self):
        self.reset()
    
    def copy(self, other):
        copy = SnakeGame()
        copy.head = Vector.from_vector(other.head)
        copy.body = [Vector.from_vector(part) for part in other.body]
        copy.direction = Vector.from_vector(other.direction)
        copy.food = Vector.from_vector(other.food)
        return copy
    
    def move(self, growing: bool = False):
        self.head = self.head + self.direction
        if (not growing):
            self.body.pop(0)
        self.body.append(Vector.from_vector(self.head))

    def reset(self):
        self.head = Vector.from_axis(0, 0)
        self.body = [Vector.from_vector(self.head)]
        self.direction = Vector.from_axis(1, 0) # right
        self.food = Vector.from_vector(self.head)
        self.create_food()
    
    def create_food(self):
        while (True):
            overlap = False
            for part in self.body:
                if (part == self.food):
                    overlap = True
                    break
            if (not overlap):
                break
            self.food.x = random.randint(0, Constants.BOARD_WIDTH - 1)
            self.food.y = random.randint(0, Constants.BOARD_HEIGHT - 1)