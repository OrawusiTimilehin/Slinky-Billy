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
pygame.time.set_timer(UPDATE_TIMER,110)
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
        # Test 
        # print("Food created and displayed")
        food_rect = Rect(int(self.coor.x) * 60, int(self.coor.y) *60, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(WINDOW, (200, 0, 0), food_rect)


# SNAKE SECTION
#CONSTANTS
class Node():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.next = None
        self.previous = None

class DoublyLinkedList():
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
snake_body = DoublyLinkedList()
snake_body.head = Node(300, 300)
snake_middle = Node(270, 300)
snake_tail = Node(240,300)
snake_body.head.next = snake_middle
snake_middle.next = snake_tail
snake_middle.previous = snake_body.head
snake_tail.previous = snake_middle




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
        return self.direction
    
    def move(self,):
        ''' This method moves the snake continously until the game stops'''
        current = snake_body.head
        while current.next:                     # This loops through the linked list inorder to get
            current = current.next
        while current.previous:
            current.x, current.y = current.previous.x, current.previous.y
            current = current.previous
        if self.direction == 'up':
            snake_body.head.y -= 30
            # print("going up")
        elif self.direction == 'down':
            snake_body.head.y += 30
            # print("going down")
        elif self.direction == 'left':
            snake_body.head.x -= 30
            # print("going left")
        elif self.direction == 'right':
            snake_body.head.x += 30
            # print("going right")
        else:
            pass
        return "Moving"

    def grow(self,):
        ''' This is the method that adds the functionality for the snake to increase in size when it eats the fruit.
         It loops through the Doubly linked List until it finds the tail ( The block with no next attribute ) 
         Then it sets that block's next attribute to the new block that was created and adds it into the link. '''
        current = snake_body.head
        while current.next:
            current = current.next
        if self.direction == 'right':
            new_body = Node(current.x-30, current.y) #This creates the new block and sets the position of the block based on the tail's block and the direction of the snake
            new_body.previous = current
        elif self.direction == 'left':
            new_body = Node(current.x + 30, current.y) #This creates the new block and sets the position of the block based on the tail's block and the direction of the snake
            new_body.previous = current
        elif self.direction == 'down':
            new_body = Node(current.x, current.y-30) #This creates the new block and sets the position of the block based on the tail's block and the direction of the snake
            new_body.previous = current
        elif self.direction == 'up':
            new_body = Node(current.x, current.y+30) #This creates the new block and sets the position of the block based on the tail's block and the direction of the snake
            new_body.previous = current
        current.next = new_body
        # Test
        #print("Added New Body")   
        return "New body block created"
           

        
    def munch(self,):
        ''' This method holds the functionality for the snake's eating abilities.
         It checks constantly if the position of the snake's head and the food are the same then it calls the grow method of the snake'''
        global food
        if snake_body.head.x == food.x *60 and snake_body.head.y == food.y *60:
            food = Food()       #Calls the creates a new food object from the food class
            self.grow()         #Calls the grow method of the snake
            # print("Eating")
        

    def collision(self,):
        if snake_body.head.x >= 600 or snake_body.head.x <= 0:
            pass
        

        
            
    




            
food = Food()
snake = Snake()

game_is_running = True
def main():
    global game_is_running
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
        snake.munch()
        snake.collision()
        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()
    sys.exit()




if __name__ =="__main__":
    main()