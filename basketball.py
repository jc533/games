import pygame,sys,math,random,datetime
from pygame.locals import *

class Basketball():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    def rest(self):
        self.addsize = -1
        self.fire = False
        self.size = 100
        self.pos = [200,490]
        self.v = [0,0]
    
    def move(self):
        global basket,gravity,basketballs,fireballs  
        self.v[1] += gravity
        self.pos[1] += self.v[1] 
        self.pos[0] += self.v[0] 
        if self.fire:
            self.ball_fire(basketballs,fireballs) 

        if self.pos[1] >= 600 - self.size:
            self.pos[1] = 600 - self.size
        
        if self.pos[0] >= 600 - self.size:
            self.pos[0] = 600 - self.size 

        if self.pos[0] <= self.size / 10:
            self.pos[0] = self.size / 10    
    
    def ball_fire(self,basketballs,fireballs):
        global score,score_text,fire_lock
        if self.pos[1] >= basket.pos[1] + self.size / 0.6:  
                # print(self.pos[0],self.pos[0] + self.size / 2)
                self.size += self.addsize
        
        elif self.pos[1] > basket.pos[1] + self.size:
            fire_lock = True
            self.v[1] = 8
            self.v[0] *= 0
            self.addsize = 0   
            if is_get_point(fireballs[0],basket,screen):
                score += 1
                score_text = font.render(str(score), 1, (0, 0, 0))
            basketballs.insert(0,fireballs[0])
            del(fireballs[0])
            
        if self.addsize == 0 and self.pos[1] > basket.pos[1] + basket.size:
            # print('hi')
            self.addsize = 2
            self.v[0] = -1
            self.size += 15
            self.pos[0] += -6.5

        if self.pos[1] >= 600 - self.size:
            self.pos[1] = 490
            self.v[1] = 0
            self.v[0] = 0
            self.fire = False
            self.addsize *= -1
            self.size = 100
            self.pos[0] += -0.5
class Basket():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    def step(self):
        self.pos[1] += self.v[1] 
        self.pos[0] += self.v[0]
        if self.pos[0] >= 600 - self.size or self.pos[0] <= 10: 
            self.v[0] *= -1

    def rest(self):
        self.move = False
        self.size = 200
        self.v = [0,0]
        self.pos = [200,0]

def is_get_point(basketball,basket,screen):
    if basketball.fire:
        get_point_pos = [0,0]
        get_point_pos[0] = basket.pos[0] + basket.size / 1.4 - basket.size / 2
        get_point_pos[1] = basket.pos[1] + basket.size
        if basketball.v[1] > 0:
            if basketball.pos[0] - basketball.v[0] > get_point_pos[0] and basketball.pos[0] - basketball.v[0] < basket.size + basket.pos[0] - basketball.size / 0.4:            
                if basketball.pos[1] - basketball.v[1] < get_point_pos[1]:
                    return True

def terminate():
    pygame.quit()
    sys.exit()

def drawbasket(screen,basket):
    basket_surface = pygame.transform.scale(basket.image, (basket.size, basket.size))
    basketRect = pygame.Rect((basket.pos[0], basket.pos[1], basket.size, basket.size))
    screen.blit(basket_surface, basketRect)

def drawball(screen,ball):
    basketball_surface = pygame.transform.scale(ball.image, (ball.size, ball.size))
    basketballRect = pygame.Rect((ball.pos[0], ball.pos[1], ball.size, ball.size))
    screen.blit(basketball_surface, basketballRect)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('basketball')
font = pygame.font.Font(None, 50) 
bgcolor = (229, 240, 140)
basketballs = []
fireballs = [] 
basket = Basket("basket.png")
score = 0
score_text = font.render(str(score), 1, (0, 0, 0))
textpos = [10, 10]
fire_lock = True
gravity = 0.1
over = False

for ball in range(0,5):
    basketballs.append(Basketball("basketball.png"))

start = datetime.datetime.now()

while True:
    if not over:
        screen.fill(bgcolor) 
        drawbasket(screen,basket)
        if fireballs:
            for ball in fireballs:
                drawball(screen,ball)
                ball.move()

        for ball in basketballs:
            drawball(screen,ball)
            ball.move()

        now = datetime.datetime.now()
        screen.blit(score_text, textpos)
        basket.step()
        if now.minute - start.minute == 3:
            over = True
        if not basket.move and score >= 10:
            basket.v[0] = random.randint(3,6)
            basket.move = True
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            terminate()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
            
            if event.key == K_RIGHT:
                if not basketballs[-1].fire:
                    for ball in basketballs:
                        if not ball.fire:
                            ball.v[0] = 5
            
            if event.key == K_LEFT:
                if not basketballs[-1].fire:
                    for ball in basketballs:
                        if not ball.fire:
                            ball.v[0] = -5

            if event.key == K_SPACE:
                if not basketballs[-1].fire and fire_lock:
                    # print("fire")
                    fire_lock = False
                    basketballs[-1].fire = True 
                    basketballs[-1].v[1] = -10
                    basketballs[-1].addsize = -1
                    basketballs[-1].v[0] = 0.5
                    fireballs.append(basketballs.pop())
            if event.key == K_s:
                while fireballs:
                    basketballs.append(fireballs.pop())
                
                for ball in basketballs:
                    ball.rest()
                basket.rest()
                score = 0
                score_text = font.render(str(score), 1, (0, 0, 0))
                fire_lock = True
                over = False
                start = datetime.datetime.now()
        else:
            if not basketballs[-1].fire:
                for ball in basketballs:
                    if not ball.fire:
                        ball.v[0] = 0

    pygame.display.update()