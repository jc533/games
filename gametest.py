import pygame,random
WHITE = (255,255,255)
RED = (100,0,0)
GREEN = (0,70,0)
BLUE = (0,0,90)
BLACK = (0,0,0)
color1 = (20,40,89)

pygame.init()
size = (1440,900)
# screen = pygame.display.set_mode(size,pygame.RESIZABLE)
print(pygame.RESIZABLE)
screen = pygame.display.set_mode(size,20,32)
pygame.display.set_caption("game","pgame")
done = False
circle_pos = (size[0]//2,size[1]//2)
clock = pygame.time.Clock()
a = pygame.image.load("ball.png")
ball_surface = pygame.transform.scale(a, (1000, 1000))
ballRect = pygame.Rect((250, 250, 1000, 1000))

def draw():
    a = size[1]//2
    for i in range(0,a//17):
        pygame.draw.circle(screen,color1,circle_pos,a)
        a -= 5
        pygame.draw.circle(screen,BLUE,circle_pos,a)
        a -= 5
        pygame.draw.circle(screen,RED,circle_pos,a)
        a -= 3
        pygame.draw.circle(screen,WHITE,circle_pos,a)
        a -= 4
        pygame.draw.circle(screen,GREEN,circle_pos,a)
def draw2(color):
    squre_pos = circle_pos
    b = 10
    d = 1
    for a in range(1,20):
        for i in range(0,1):
            pygame.draw.line(screen,color,squre_pos,(squre_pos[0]+(d-1)*b,squre_pos[1]),5)
            squre_pos = (squre_pos[0]+(d-1)*b,squre_pos[1])
            d += 1
            pygame.draw.line(screen,color,squre_pos,(squre_pos[0],squre_pos[1]+(d-1)*b),5)
            squre_pos = (squre_pos[0],squre_pos[1]+(d-1)*b)
            d += 1
            pygame.draw.line(screen,color,squre_pos,(squre_pos[0]-(d-1)*b,squre_pos[1]),5)
            squre_pos = (squre_pos[0]-(d-1)*b,squre_pos[1])
            d += 1
            pygame.draw.line(screen,color,squre_pos,(squre_pos[0],squre_pos[1]-(d-1)*b),5)
            squre_pos = (squre_pos[0],squre_pos[1]-(d-1)*b)
            d += 1

while not done:
    screen.blit(ball_surface, ballRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == 3:
            draw2((60,70,90))
            print(event.key)
        if event.type == 2:
            draw() 
        if event.type == 5:
            rand = random.randint(0,100)
            # screen.fill((rand+random.randint(0,125),rand+random.randint(0,125),rand+random.randint(0,125)))
            screen.blit(ball_surface, ballRect)
            print(a)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()	
