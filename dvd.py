import pygame, sys
from pygame.locals import *
pygame.init()

fpsClock = pygame.time.Clock()
FPS = 60

SCREEN_W = 640
SCREEN_H = 480

DVD_X = 50
DVD_Y = 50
DVD_XDirection = 2
DVD_YDirection = 2
     
#set up and display the window
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('DVD Display')

# load DVD Logo
DVD = pygame.image.load('images/DVD.webp').convert_alpha(screen)
DVD = pygame.transform.scale(DVD,(DVD.get_width() * 0.2,DVD.get_height() * 0.2))

while True:
    
    # check for user quitting
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
                   
    # draw background and DVD
    screen.fill((255,255,255))
    screen.blit(DVD, (DVD_X, DVD_Y))

    if DVD_X > SCREEN_W -DVD.get_width():
        DVD_XDirection *= -1
        
    if DVD_X < 0:
        DVD_XDirection *= -1
        
    DVD_X += DVD_XDirection

    if DVD_Y > SCREEN_H -DVD.get_height():
        DVD_YDirection *= -1
        
    if DVD_Y < 0:
        DVD_YDirection *= -1
        
    DVD_Y += DVD_YDirection
 
    # tick the clock and refresh the screen
    fpsClock.tick(FPS)
    pygame.display.update()

    

    


    
