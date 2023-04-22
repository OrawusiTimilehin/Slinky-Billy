import pygame, sys
from pygame import *
from random import randint
from pygame import Vector2

# CONSTANTS

# dimensions of the screen
WIDTH = 800
HEIGHT = 600
# Inatialization of the Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the Frames Per Second for our game so it is consistent for all systems.
FPS = 60
clock = pygame.time.Clock()
# Setting the Name of the Game
pygame.display.set_caption("Slinky Billy")




# FOOD SECTION

# CONSTANTS
SIZE = 40
class Food():
    ''' This is the Doc string for this Class. This is the food class that would contain all the functionality for the snake's food.'''
    def __init__(self,):
        # This sets the coordinates for the fruit, it randomly selects the position using the randint function
        #  and that x and y coordinate is multiplied by a factor to suit the dimensions of the board.

        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.coor = Vector2(self.x * 80, self.y * 60)

    def display(self, ):
        food_rect = Rect(self.coor.x, self.coor.y, SIZE, SIZE)
        pygame.draw.rect(WINDOW, (200, 0, 0), food_rect)


food = Food()

def main():
    game_is_running = True
    while game_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                game_is_running = False

            else:
                pass
        WINDOW.fill((195, 229, 84))
        food.display()
        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()




if __name__ =="__main__":
    main()