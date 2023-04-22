from pygame import *
from random import randint
from pygame import Vector2
class Food():
    ''' This is the Doc string for this Class. This is the food class that would contain all the functionality for the snake's food.'''
    def __init__(self,):
        # This sets the coordinates for the fruit, it randomly selects the position using the randint function
        #  and that x and y coordinate is multiplied by a factor to suit the dimensions of the board.

        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.coor = Vector2(self.x * 80, self.y * 60, 40, 40)

    def display_food(self, ):
        food_rect = Rect(self.coor.x, self.coor.y)

        