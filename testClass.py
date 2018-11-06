import pygame
from classes import Spaceship
pygame.init()

BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
GREEN   = (  0, 255,   0)
RED     = (255,   0,   0)
BLUE    = (0,     0, 255)
YELLOW  = (255, 255,   0)
SKYBLUE = (135, 206, 250)
BROWN   = (139,  69,  19)
D_ORANGE= (205, 102,   0)
PURPLE =  (138,  43, 226)

WIDTH = 1000
HEIGHT = 900
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('testClass')

done = False
clock = pygame.time.Clock()

spaceship = Spaceship(100, 100, WHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    
    screen.blit(screen, spaceship)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()     