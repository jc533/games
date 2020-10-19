import pygame,sys,random,math,datetime
from pygame.locals import *


class Ball():
 
    def __init__(self, image_file):   
        self.image = pygame.image.load(image_file)
        self.rest()
    
    def rest(self):
        global score
        self.pos = [random.randint(150,400),random.randint(-100,0)]
        self.v = [random.randint(1,1),random.randint(0,2)]
        if score < 51:
            self.size = random.randint(30,30)
        elif score < 71:
            self.v = [random.randint(1,1),random.randint(0,1)]
            self.size = random.randint(30,60)
        else:
            self.size = random.randint(30,90)
    def step(self):
        global score,score_text,G
        self.v[1] += G
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        
        if self.pos[1] >= 500 - self.size:
            self.v[1] *= -0.95
            self.pos[1] = 500 - self.size
            score += int(self.size / 30)
            score_text = font.render(str(score), 1, (0, 0, 0))
        if self.pos[0] >= 600 - self.size or self.pos[0] <= 15:
            self.v[0] *= -1
        if self.pos[1] > 390 and  abs(self.v[1]) < 4:
                self.rest()          

class Player():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    def rest(self):
        self.pos = [300,480]
        self.size = 20
        self.v = [0,0]
    def move(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        if self.pos[0] >= 600 - self.size:
            self.pos[0] = 600 - self.size
            self.v[0] *= -1

        if self.pos[0] <= self.size / 2:
            self.pos[0] = self.size / 2
            self.v[0] *= -1   
class Bullet():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    
    def rest(self):
        global start
        self.bullet_number = 5
        self.move = False 
        self.count = True
        self.show = False
        self.size = 30
        self.v = [random.randint(-1,1),random.randint(-10,-5)]
        self.pos = [random.randint(100,500),470]
        self.time = random.randint(5,10)
        start = datetime.datetime.now()
    
    def attack(self):
        
        self.v[1] += G
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        if self.bullet_number == 0:
            self.rest()
        if self.pos[1] >= 500 - self.size / 2:
            self.show = False
            self.bullet_number -= 1 


def terminate():
    pygame.quit()
    sys.exit()

def hit(ball1,ball2):
    # distance = math.sqrt((ball1.pos[0] + ball1.size / 2 - ball2.pos[0] + ball2.size / 2)**2 + (ball1.pos[1] + ball1.size / 2 - ball2.pos[1] + ball2.size / 2)**2)
    distance = math.sqrt((ball1.pos[0] - ball2.pos[0])**2 + (ball1.pos[1] - ball2.pos[1])**2)
    # (ball2.size - (math.sqrt(ball2.size**2+ball2.size**2) - ball2.size) + ball1.size - (math.sqrt(ball1.size**2+ball1.size**2) - ball1.size)) / 2
    if distance < (ball1.size + ball2.size) / 1.8:
        return True
G = 0.1
bgcolor = (5, 255, 178)
BLUE = (28, 103, 243)
score = 0
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 500))
pygame.display.set_caption('game')
balls = []
player = Player("ball2.png")
player_surface = pygame.transform.scale(player.image, (player.size, player.size))
over = False
font = pygame.font.Font(None, 50) 
score_text = font.render(str(score), 1, (0, 0, 0))
textpos = [10, 10]
start = datetime.datetime.now()
bullet = Bullet("ball3.png")


for i in range(0,10):
    balls.append(Ball("ball.png"))

while True:
    DISPLAYSURF.fill(bgcolor)
    playerRect = pygame.Rect((player.pos[0], player.pos[1], player.size, player.size))
    DISPLAYSURF.blit(player_surface, playerRect)
    DISPLAYSURF.blit(score_text, textpos) 
    
    if bullet.show:
        bullet_surface = pygame.transform.scale(bullet.image, (bullet.size, bullet.size))
        bulletRect = pygame.Rect((bullet.pos[0], bullet.pos[1], bullet.size, bullet.size))
        DISPLAYSURF.blit(bullet_surface, bulletRect)
        # pygame.draw.circle(DISPLAYSURF, BLUE, (int(bullet.pos[0]), int(bullet.pos[1])), bullet.size, 0)
        
        if bullet.move and not over:
            bullet.attack()
    
    if bullet.count and not over:
        now = datetime.datetime.now()
        now = now.second
        if abs(now - start.second) == bullet.time and now - start.second >= 0:
            bullet.show = True
            bullet.count = False
        elif 60 - start.second + now == bullet.time:
            bullet.show = True
            bullet.count = False

    
    if not over:
        player.move()
    
    for ball in balls:
        ball_surface = pygame.transform.scale(ball.image, (ball.size, ball.size))
        ballRect = pygame.Rect((ball.pos[0], ball.pos[1], ball.size, ball.size))
        DISPLAYSURF.blit(ball_surface, ballRect)
        if not over:
            ball.step() 
        if hit(ball,player):
            over = True

        if hit(bullet,ball) and bullet.move:
            ball.rest()

        if bullet.show:
            if hit(bullet,player):
                if not bullet.move:
                    bullet.show = False
                else:
                    over = True

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player.v[0] = 3
            
            if event.key == K_LEFT:
                player.v[0] = -3
            
            if event.key == K_ESCAPE:
                terminate()
            
            if event.key == K_SPACE:
                if not bullet.count and not bullet.show:
                    if not over:
                        bullet.move = True
                        bullet.show = True
                        bullet.v = [random.randint(-1,1),random.randint(-10,-5)]
                        bullet.pos = [random.randint(100,500),460]    
                
            if event.key == K_s:
                score = 0
                score_text = font.render(str(score), 1, (0, 0, 0))
                player.rest()
                bullet.rest()
                for ball in balls:
                    ball.rest()
                over = False

    pygame.display.update()
