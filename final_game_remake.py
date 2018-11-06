import pygame, random, time

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
pygame.display.set_caption('Final Game')

done = False
clock = pygame.time.Clock()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        
        super().__init__()
        
        self.image = pygame.Surface([x, y])
        self.image.set_colorkey(WHITE)
        
        pygame.draw.rect(self.image, color, (x,y, 50, 50))
        pygame.draw.polygon(self.image, color, [(x,y), (x+25, y-50), (x+50, y)])
        pygame.draw.polygon(self.image, color, [(x,y), (x-25, y+100), (x+25, y+50)])
        pygame.draw.polygon(self.image, color, [(x+50,y), (x+75, y+100), (x+25, y+50)])
        
        self.rect = self.image.get_rect()
        
class GreenAlien(pygame.sprite.Sprite):
    def __init__(self, alien_x, alien_y, color):
        super().__init__()
        
        self.image = pygame.Surface([alien_x, alien_y])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)        

player_list = pygame.sprite.Group()
alien_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

spaceship = Spaceship(100, 100, BLUE)
all_sprites_list.add(spaceship)