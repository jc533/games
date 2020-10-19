 import pygame,random

class Ball():
    def __init__(self, image_file):
        self.pos = [random.randint(200, 400),random.randint(100, 100)]       
        self.v = [random.randint(1,10),0]
        self.speed = random.randint(0,0)
        self.size = [100,100]
        self.m = 10
        self.image = pygame.image.load(image_file)
    def step(self):
        self.v[1] += (G * (self.m/self.pos[1]**2))
        self.pos[0] += self.v[0]//fps
        self.pos[1] += self.speed+self.v[1]//fps
        print(self.pos,self.v[1])
        if self.pos[1] >= size[1] - self.size[1]/2 or self.pos[1] <=  self.size[1]/2:
            self.speed *= -1

        if self.pos[0] >= size[0] - self.size[0]/2 or self.pos[0] <=  self.size[0]/2:
            self.v[0] *= -0.9

def drawsprite(screen,sprite,degree):
    sprite_surface = pygame.transform.scale(sprite.image, (sprite.size[0], sprite.size[1]))
    sprite_surface = pygame.transform.rotate(sprite_surface,degree)        
    spriteRect = sprite_surface.get_rect()
    spriteRect.center = (sprite.pos[0], sprite.pos[1])
    screen.blit(sprite_surface, spriteRect)


WHITE = (255,255,255)
RED = (100,0,0)
GREEN = (0,70,0)
BLUE = (0,0,90)
BLACK = (0,0,0)
color1 = (20,40,89)
G = 9800

pygame.init()
size = (800,600)
Screen = pygame.display.set_mode(size)
pygame.display.set_caption("game","pgame")
done = False
clock = pygame.time.Clock()
ball = Ball("ball3.png")
fps = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    Screen.fill(BLACK)
    drawsprite(Screen,ball,0)
    ball.step()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()	