import pygame, sys
from pygame import *
from random import randint
from pygame import Vector2

# CONSTANTS

# dimensions of the screen
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30
# Inatialization of the Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the Frames Per Second for our game so it is consistent for all systems.
FPS = 60
clock = pygame.time.Clock()
UPDATE_TIMER = pygame.USEREVENT 
pygame.time.set_timer(UPDATE_TIMER,150)
# Setting the Name of the Game
pygame.display.set_caption("Slinky Billy")




# FOOD SECTION

# CONSTANTS
class Food():
    ''' This is the Doc string for this Class. This is the food class that would contain all the functionality for the snake's food.'''
    def __init__(self,):
        # This sets the coordinates for the fruit, it randomly selects the position using the randint function
        #  and that x and y coordinate is multiplied by a factor to suit the dimensions of the board.

        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.coor = Vector2(self.x, self.y)

    def display(self, ):
        food_rect = Rect(int(self.coor.x) * 100, int(self.coor.y) *60, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(WINDOW, (200, 0, 0), food_rect)


# SNAKE SECTION
#CONSTANTS
class Node():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.next = None

class LinkedList():
    def __init__(self, ):
        self.head = None

    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


# Initialising snake body for the start of the game
snake_body = LinkedList()
snake_body.head = Node(500, 260)
# snake_middle = Node(460, 260)
# snake_body.head.next = snake_middle
# snake_tail = Node(420,260)
# snake_middle.next = snake_tail




class Snake():
    def __init__(self, ):
        self.direction = None

    def display(self,):
        ''' This method contains all the functionality for displaying the snake on screen'''
        current = snake_body.head 
        while current:
            body_rect = pygame.Rect(int(current.x), int(current.y), CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(WINDOW, (20,89,200), body_rect)
            current = current.next

    def change_direction(self, direction):
        ''' This is the method that contains the functionality for the snake's movement'''
        if direction == 'up':
            self.direction = 'up'
        elif direction == 'down':
            self.direction = 'down'
        elif direction == 'left':
            self.direction = 'left'
        elif direction == 'right':
            self.direction = 'right'
        else:
            pass
    
    def move(self,):
        ''' This method moves the snake continously until the game stops'''
        if self.direction == 'up':
            snake_body.head.y -= 40
        elif self.direction == 'down':
            snake_body.head.y += 40
        elif self.direction == 'left':
            snake_body.head.x -= 40
        elif self.direction == 'right':
            snake_body.head.x += 40
        else:
            pass

        
            




            
food = Food()
snake = Snake()


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
            if event.type == UPDATE_TIMER:
                snake.move()
        WINDOW.fill((195, 229, 84))
        food.display()
        snake.display()
        if event.type == KEYDOWN:
                if event.key == K_UP:
                    if snake.direction == 'down':
                        pass
                    else:
                        snake.change_direction('up')
                if event.key == K_DOWN:
                    if snake.direction == 'up':
                        pass
                    else:
                        snake.change_direction('down')
                if event.key == K_LEFT:
                    if snake.direction == 'right':
                        pass
                    else:
                        snake.change_direction('left')
                if event.key == K_RIGHT:
                    if snake.direction == 'left':
                        pass
                    else:
                        snake.change_direction('right')
        
        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()




if __name__ =="__main__":
    main()