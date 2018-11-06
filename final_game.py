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



#DRAWING FUNCTIONS

###------------------------------###   TO Do   ###-----------------------------------------------###
###----------------------------------------------------------------------------------------------###
#Make each drawing a sprite -- own surface. Blit onto screen, check if sprites(surfaces) overlap for collision detection.
#Look at -- https://gamedev.stackexchange.com/questions/63411/collision-detection-without-classes-in-pygame
#Also - Look up more ways to make sprites
#Look at -- http://programarcadegames.com/index.php?chapter=introduction_to_sprites
#Look at -- http://www.101computing.net/creating-sprites-using-pygame/
###----------------------------------------------------------------------------------------------###
###----------------------------------------------------------------------------------------------###





def drawSpaceship(x, y, color):
    pygame.draw.rect(screen, color, (x,y, 50, 50))
    pygame.draw.polygon(screen, color, [(x,y), (x+25, y-50), (x+50, y)])
    pygame.draw.polygon(screen, color, [(x,y), (x-25, y+100), (x+25, y+50)])
    pygame.draw.polygon(screen, color, [(x+50,y), (x+75, y+100), (x+25, y+50)])
    
    
def drawAliens(alien_x, alien_y, pickAlien):
    if pickAlien == 0:
        pygame.draw.circle(screen, GREEN, (alien_x, alien_y), 15)
        pygame.draw.circle(screen, GREEN, (alien_x, alien_y+15), 20)
        pygame.draw.circle(screen, BLACK, (alien_x-5, alien_y-3), 3)
        pygame.draw.circle(screen, BLACK, (alien_x+5, alien_y-3), 3)
    elif pickAlien == 1:
        pygame.draw.rect(screen, BLUE, (alien_x-10, alien_y-5, 20, 40))
        pygame.draw.ellipse(screen, BLUE, (alien_x-25,alien_y-10, 50, 10))
        pygame.draw.circle(screen, BLUE, (alien_x-10, alien_y-10), 5)
        pygame.draw.circle(screen, BLUE, (alien_x+10, alien_y-10), 5)        
        pygame.draw.circle(screen, BLACK, (alien_x-10, alien_y-10), 3)
        pygame.draw.circle(screen, BLACK, (alien_x+10, alien_y-10), 3)        
    elif pickAlien == 2:
        pygame.draw.circle(screen, D_ORANGE, (alien_x, alien_y+10), 15)
        pygame.draw.rect(screen, D_ORANGE, (alien_x-20, alien_y+6, 40, 8))
        pygame.draw.circle(screen, D_ORANGE, (alien_x-20, alien_y+10), 5)
        pygame.draw.circle(screen, D_ORANGE, (alien_x+20, alien_y+10), 5)        
        pygame.draw.circle(screen, BLACK, (alien_x-20, alien_y+10), 3)
        pygame.draw.circle(screen, BLACK, (alien_x+20, alien_y+10), 3)        
    elif pickAlien == 3:
        pygame.draw.ellipse(screen, RED, (alien_x-12, alien_y, 25, 40))
        pygame.draw.ellipse(screen, RED, (alien_x-12, alien_y, 25, 40))
        pygame.draw.ellipse(screen, RED, (alien_x-13, alien_y-10, 10, 35))
        pygame.draw.ellipse(screen, RED, (alien_x+3, alien_y-10, 10, 35))
        pygame.draw.circle(screen, RED, (alien_x-8, alien_y-4), 5)
        pygame.draw.circle(screen, RED, (alien_x+8, alien_y-4), 5)        
        pygame.draw.circle(screen, BLACK, (alien_x-8, alien_y-4), 3)
        pygame.draw.circle(screen, BLACK, (alien_x+8, alien_y-4), 3)
    elif  pickAlien == 4:
        pygame.draw.polygon(screen, PURPLE, [(alien_x, alien_y), (alien_x-20, alien_y+30), (alien_x+20, alien_y+30)])
        pygame.draw.circle(screen, PURPLE, (alien_x, alien_y), 10)
        pygame.draw.circle(screen, BLACK, (alien_x, alien_y), 5)


def main():
    global wave
    
    for aliens in range (len(alien_y)):
        alien_y[aliens] = alien_y[aliens] + alien_v[aliens]    
    for aliens in range (len(alien_y)):
            alien_y[aliens] = alien_y[aliens] + alien_v[aliens]
            
    text = basicfont.render('Score = ' + getTime(), True, WHITE, BLACK)
    textrect = text.get_rect()
    textrect.centerx = WIDTH - 150
    textrect.centery = 25
    text2 = basicfont.render('Wave: ' + str(wave), True, WHITE, BLACK)
    text2rect = text2.get_rect()
    text2rect.centerx = WIDTH - 150
    text2rect.centery = 65
    
    screen.fill(BLACK)
    
    if y < min(alien_y):
        #screen.blit(text2, text2rect)
        wave += 1
    screen.blit(text2, text2rect)
    screen.blit(text, textrect)
    
    drawSpaceship(x, y, WHITE)
    for aliens in range (100):
        drawAliens(alien_x[aliens], alien_y[aliens], pickAlien[aliens])        
    
            
            
wave = 1
time1 = 0
i = 0
alien_v = []
alien_x = []
alien_y = []
alien_pos = [alien_x, alien_y]
pickAlien = []
for alienNum in range(2000):
    alien_v.append(random.randint(3, 8))
for alienNum in range(2000):
    alien_y.append((random.randint(1000, 3000)*-1))
for alienNum in range (2000):
    alien_x.append(random.randint(0, WIDTH))
for aleinNum in range(2000):
    pickAlien.append(random.randint(0,5))
t0 = time.clock()
basicfont = pygame.font.SysFont(None, 48)


def getTime():
    global t0
    global time1
    time1 = time.clock() - t0
    return str(round(time1, 0))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #GAME LOGIC
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    pygame.mouse.set_visible(False)
    i = i + 1
    i_test = i % 4
    
    #for aliens in range (len(alien_y)):
    #    alien_y[aliens] = alien_y[aliens] + alien_v[aliens]    
    #text = basicfont.render('Score = ' + getTime(), True, WHITE, BLACK)
    #textrect = text.get_rect()
    #textrect.centerx = WIDTH - 150
    #textrect.centery = 25
    #if y < min(alien_y):
    #    print("End of Wave: " + str(wave))
    #    wave += 1
    
    
    if y > min(alien_y):
        main()
    elif y < min(alien_y):
        #pygame.time.delay(1000)
        alien_v = []
        alien_x = []
        alien_y = []
        pickAlien = []
        for alienNum in range(2000):
            alien_v.append(random.randint(3, 8))
        for alienNum in range(2000):
            alien_y.append((random.randint(1000, 3000)*-1))
        for alienNum in range (2000):
            alien_x.append(random.randint(0, WIDTH))
        for aleinNum in range(2000):
            pickAlien.append(random.randint(0,5))
        
    
    #SCREEN CLEARING
    #screen.fill(BLACK)
    
    #DRAWING
    #screen.blit(text, textrect)
    #drawSpaceship(x, y, WHITE)
    #for aliens in range (100):
        #drawAliens(alien_x[aliens], alien_y[aliens], pickAlien[aliens])
    ###ON COLLISIONS/EXPLODING
    #if (i_test == 0):
    #    drawSpaceship(x, y, WHITE)
    #elif (i_test != 0):
    #    drawSpaceship(x, y, GREEN)
            
    #FLIPPING
    pygame.display.flip()
    clock.tick(60)
pygame.quit()    