#This is my first computer game created: Turtle vs Bees.
#Please note: all images were taken from OpenGameArt.org

#importing the modules
import pygame
import random

#Initializing Pygame
pygame.init()

#Creating the window for the game.
width = 500
height = 500
window = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption('Turtle vs Bees')

#Creating background colour for the game.
black = (0,0,0)
window_background = window.fill(black)


#Updating the game with the new additions created. 
pygame.display.update()

#Creating the characters of our game.

turtle = pygame.image.load('turtle_64x72.png')
bee1 = pygame.image.load('1.png')
bee2 = pygame.image.load('1.png')
bee3 = pygame.image.load('1.png')
trophy = pygame.image.load('golden_trophy.png')

#Setting the boundaries of our players
turtle_height = turtle.get_height()
turtle_width = turtle.get_width()
bee1_height = bee1.get_height()
bee1_width = bee1.get_width()
bee2_height = bee2.get_height()
bee2_width = bee2.get_width()
bee3_height = bee3.get_height()
bee3_width = bee3.get_width()
trophy_height = trophy.get_height()
trophy_width = trophy.get_width()


#Starting positions of the characters
turtle_x_position = 150
turtle_y_position = 150
bee1_x_position = 400
bee1_y_position = 150
bee2_x_position = 300
bee2_y_position = 100
bee3_x_position = 300
bee3_y_position = 225
trophy_x_position = 400 
trophy_y_position = 50

#Creating a main loop in order to exit the window.
run = True

#Creating boolean values for key up and key down.
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
      # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    if keyUp == True:
        if turtle_y_position > 0 : # This makes sure that the user does not move the player above the window.
            turtle_y_position -= 1
    if keyDown == True:
        if turtle_y_position < height - turtle_height:# This makes sure that the user does not move the player below the window.
            turtle_y_position += 1
    if keyLeft == True:
        if turtle_x_position > 0:
            turtle_x_position -= 1 
    if keyRight == True:
        if turtle_x_position < width - turtle_width:
            turtle_x_position += 1

    #Window updating the background with black once the character is moving.
    window.fill(black)
    
    #Displaying the characters on the screen

    tutrtle_display = window.blit(turtle,(turtle_x_position,turtle_y_position))
    bee1_display = window.blit(bee1,(bee1_x_position,bee1_y_position))
    bee2_display = window.blit(bee2,(bee2_x_position,bee2_y_position))
    bee3_display = window.blit(bee3,(bee3_x_position,bee3_y_position))
    trophy_display = window.blit(trophy,(trophy_x_position,trophy_y_position))
    pygame.display.flip()


#Creating boxes around the Turtle to see if there is a collision.

    turtleBox = pygame.Rect(turtle.get_rect())

#Making the box stay around the player image.
    turtleBox.top = turtle_y_position
    turtleBox.left = turtle_x_position

#Creating the box for the bees:
    bee1Box = pygame.Rect(bee1.get_rect())
    bee1Box.top = bee1_y_position
    bee1Box.left = bee1_x_position

    bee2Box = pygame.Rect(bee2.get_rect())
    bee2Box.top = bee2_y_position
    bee2Box.left = bee2_x_position

    bee3Box = pygame.Rect(bee3.get_rect())
    bee3Box.top = bee3_x_position
    bee3Box.left = bee3_x_position

#Creating the box for the trophy:
    trophyBox = pygame.Rect(trophy.get_rect())
    trophyBox.top = trophy_y_position
    trophyBox.left = trophy_x_position

    if turtleBox.colliderect(bee1Box):
        print("You Lose!")

        pygame.quit()
        exit(0)

    if turtleBox.colliderect(bee2Box):
        print("You Lose!")

        pygame.quit()
        exit(0)

    if turtleBox.colliderect(bee3Box):
        print("You Lose!")
        
        pygame.quit()
        exit(0)

    if turtleBox.colliderect(trophyBox):
        print("You Win!")

        pygame.quit()
        exit(0)


    
#Making the bees approach the player
    bee1_x_position -= 0.15
    bee2_x_position -= 0.15
    bee3_x_position -= 0.15
