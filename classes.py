import pygame

WHITE = (255, 255, 255)

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, (x,y, 50, 50))
        pygame.draw.polygon(self.image, color, [(x,y), (x+25, y-50), (x+50, y)])
        pygame.draw.polygon(self.image, color, [(x,y), (x-25, y+100), (x+25, y+50)])
        pygame.draw.polygon(self.image, color, [(x+50,y), (x+75, y+100), (x+25, y+50)])        
        self.rect = self.image.get_rect()