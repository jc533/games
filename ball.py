import pygame,sys,random
from pygame.locals import *


class Ball():

    def __init__(self, image_file):
        self.px = random.randint(200, 400)
        self.py = random.randint(200, 400)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
        self.size = 100
        self.image = pygame.image.load(image_file)

    def step(self):
        self.px += self.vx
        self.py += self.vy

        if self.py >= 390 or self.py <= 15:
            # print(self.py)
            self.vy *= -0.9

        if self.px >= 490 or self.px <= 15:
            # print(self.px)
            self.vx *= -0.9


def terminate():
    pygame.quit()
    sys.exit()


def speed():
    global balls
    for ball in balls:
        ball.vx *= 1.1
        ball.vy *= 1.1

def speed_random():
    global balls
    for ball in balls:
        ball.vx = random.randint(-10, 10)
        ball.vy = random.randint(-10, 10)


def pos_random():
    global balls
    for ball in balls:
        ball.px = random.randint(200, 400)
        ball.py = random.randint(200, 400)

WHITE = (255, 255, 255)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 500))
pygame.display.set_caption('game')
balls = []
while True:
    DISPLAYSURF.fill(WHITE)
    for ball in balls:
        ball.step()
        ball_surface = pygame.transform.scale(ball.image, (ball.size, ball.size))
        ballRect = pygame.Rect((ball.px, ball.py, ball.size, ball.size))
        # print(ballRect)
        DISPLAYSURF.blit(ball_surface, ballRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()

        if event.type == KEYDOWN:
            # print("l:",KEYDOWN)
            if event.key == K_ESCAPE:
                terminate()

            if event.key == K_SPACE:
                for i in range(1,1):
                    img = random.randint(2, 4)
                    balls.append(Ball("ball" + str(img) + ".png"))    
            if event.key == K_UP:
                speed()

            if event.key == K_w:
                pos_random()

            if event.key == K_r:
                speed_random()
        if event.type == 5:
            img = random.randint(2, 4)
            balls.append(Ball("ball" + str(img) + ".png"))
    pygame.display.update()
