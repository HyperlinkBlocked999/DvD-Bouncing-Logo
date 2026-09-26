import pygame, sys
from pygame.locals import *
pygame.init()

fpsClock = pygame.time.Clock()
FPS = 60

SCREEN_W = 640
SCREEN_H = 480

ballX = 50
ballY = 50
ballXDirection = 2
ballYDirection = 2
     
#set up and display the window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Start')

# load DVD Logo
ball = pygame.image.load('images/DVD.webp').convert_alpha(screen)
ball = pygame.transform.scale(ball,(ball.get_width() * 0.2,ball.get_height() * 0.2))

while True:
    
    # check for user quitting
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
                   
    # draw background and ball
    screen.fill((255,255,255))
    screen.blit(ball, (ballX, ballY))

    if ballX > SCREEN_W -ball.get_width():
        ballXDirection *= -1
        
    if ballX < 0:
        ballXDirection *= -1
        
    ballX += ballXDirection

    if ballY > SCREEN_H -ball.get_height():
        ballYDirection *= -1
        
    if ballY < 0:
        ballYDirection *= -1
        
    ballY += ballYDirection
 
    # tick the clock and refresh the screen
    fpsClock.tick(FPS)
    pygame.display.update()

    

    


    
