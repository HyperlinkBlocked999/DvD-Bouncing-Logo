import pygame, sys
from pygame.locals import *
pygame.init()

fpsClock = pygame.time.Clock()
FPS = 60

SCREEN_W = 640
SCREEN_H = 480

ballX = 50
ballY = 50
ballXDirection = 10
ballYDirection = 10

starfishX = 100
starfishY = 150

starfishXDirection = 2
starfishYDirection = 2

# load background and ball image (note double backslash)
ball = pygame.image.load('assets\\ball.png')
starfish = pygame.image.load('assets\\starfish.png')
bg = pygame.image.load('assets\\bg.jpg')
        
#set up and display the window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Start')

while True:
    
    # check for user quitting
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
                   
    # draw background and ball
    screen.blit(bg, (0,0))
    screen.blit(ball, (ballX, ballY))

    if ballX > SCREEN_W -75:
        ballXDirection *= -1
        
    if ballX < 0:
        ballXDirection *= -1
        
    ballX += ballXDirection

    if ballY > SCREEN_H -75:
        ballYDirection *= -1
        
    if ballY < 0:
        ballYDirection *= -1
        
    ballY += ballYDirection

    screen.blit(starfish, (starfishX, starfishY))

    if starfishX > SCREEN_W -144:
        starfishXDirection *= -1
        
    if starfishX < 0:
        starfishXDirection *= -1
        
    starfishX += starfishXDirection

    if starfishY > SCREEN_H -144:
        starfishYDirection *= -1
        
    if starfishY < 0:
        starfishYDirection *= -1
        
    starfishY += starfishYDirection

        
    # tick the clock and refresh the screen
    fpsClock.tick(FPS)
    pygame.display.update()

    

    


    
