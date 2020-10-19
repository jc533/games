import pygame,random,math

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.r = 7
        self.show = True
        self.start = False
        self.pos = [x,y]
        self.speed = [0,0]
        self.rect = pygame.draw.circle(screen,WHITE,self.pos,self.r)
        self.rect.center = self.pos

    def update(self):

        if self.show:
            self.key()
        else:
            self.move_to()
        self.touch_wall()
        self.rect = pygame.draw.circle(screen,WHITE,self.pos,self.r)
        self.speed[0] *= 0.9
        self.speed[1] *= 0.9
        self.pos[0] += int(self.speed[0])
        self.pos[1] += int(self.speed[1])

    def move_to(self):
        mouse_pos = pygame.mouse.get_pos()
        self.speed[0] = int((mouse_pos[0] - self.pos[0])/5)
        self.speed[1] = int((mouse_pos[1] - self.pos[1])/5)

    def key(self):

        if key["up"]:
            self.speed[1] = -12

        if key["down"]:
            self.speed[1] = 12

        if key["left"]:
            self.speed[0] = -12

        if key["right"]:
            self.speed[0] = 12

    def kill(self):
        for i in enemies:
            if i.show:
                collide_list = pygame.sprite.spritecollide(self, [i] , False)
                if collide_list != []:
                    return True
            

    def touch_wall(self):
        if self.pos[0]+self.r >= 799:
            self.pos[0] = 799 - self.r

        if self.pos[0]-self.r <= 0:
            self.pos[0] = self.r

        if self.pos[1]+self.r >= 599: 
            self.pos[1] = 599 - self.r

        if self.pos[1]-self.r <= 0:
            self.pos[1] = self.r


class enemy(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.show = False
        self.start = False
        self.next_time = pygame.time.get_ticks() + random.randint(30,600)*100
        self.r = 10
        self.pos = [x,y]
        self.move_to_pos = [random.randint(0,800),random.randint(0,600)]
        if get_distance(self.move_to_pos,self.pos) < 30:
            self.__init__(random.randint(0,800),random.randint(0,600))
        self.speed = [0,0]
        self.rect = pygame.draw.circle(screen,RED,self.pos,self.r)
        self.rect.center = self.pos
        self.move_to()


    def update(self):
        self.kill()
        if self.show:
            self.rect = pygame.draw.circle(screen,RED,self.pos,self.r)
            self.pos[0] += self.speed[0]
            self.pos[1] += self.speed[1]

        elif pygame.time.get_ticks() >= self.next_time:
            self.show = True


    def move_to(self):
        # global ball
        self.speed[0] = int((self.move_to_pos[0] - self.pos[0])/30)
        self.speed[1] = int((self.move_to_pos[1] - self.pos[1])/30)

    def kill(self):
        kill = False
        if self.pos[0]+self.r >= 800 + 2 * self.r:
            # self.pos[0] = 799 - self.r
            kill = True

        if self.pos[0]-self.r <= -0 - 2 * self.r:
            # self.pos[0] = self.r
            kill = True

        if self.pos[1]+self.r >= 600 + 2 * self.r: 
            # self.pos[1] = 599 - self.r
            kill = True

        if self.pos[1]-self.r <= -0 - 2 * self.r: 
            # self.pos[1] =  self.r
            kill = True
        
        if kill and self.show:
            global score
            self.__init__(self.pos[0],self.pos[1])
            score += 1

class Score(pygame.sprite.Sprite):
    global score
    def __init__(self, center_x, center_y, font, font_size):
        self.font = pygame.font.Font(font, font_size)
        self.image = self.font.render(str(0), 1, (255, 255, 255))
        self.pos = [center_x, center_y]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.image = self.font.render(str(score), 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)

def get_distance(pos1,pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def darw_mouse():
    mouse_pos = pygame.mouse.get_pos()
    mouse_surface = pygame.transform.scale(mouse_img, (32, 32))
    mouse_rect = mouse_surface.get_rect()
    mouse_rect.center = mouse_pos
    screen.blit(mouse_surface,mouse_rect)

def restart():
    ball.show = True

WHITE = (255,255,255)
RED = (200,50,50)
GREEN = (0,70,0)
BLUE = (0,0,90)
BLACK = (0,0,0)

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
group = pygame.sprite.Group()

fps = 30
pygame.display.set_caption("tank","pgame")
done = False
next_time = 0
clock = pygame.time.Clock()
group = pygame.sprite.Group()

score = 0
hp = 10
key = {"up":False,"down":False,"left":False,"right":False}
mouse_img = pygame.image.load('mouse.jpg')
enemies = []
ball = Ball(400,300)
score_image = Score(30,30, 'freesansbold.ttf', 30)


for i in range(10):
    enemies.append(enemy(random.randint(0,800),random.randint(0,600)))
    group.add(enemies[i])


# enemy = enemy(400,300)
group.add(ball)
pygame.mouse.set_visible(False)



while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                key["left"] = True
            
            if event.key == pygame.K_RIGHT:
                key["right"] = True
            
            if event.key == pygame.K_UP:
                key["up"] = True
            
            if event.key == pygame.K_DOWN:
                key["down"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key["left"] = False
            
            if event.key == pygame.K_RIGHT:
                key["right"] = False
            
            if event.key == pygame.K_UP:
                key["up"] = False
            
            if event.key == pygame.K_DOWN:
                key["down"] = False
        if event.type == 1:
            restart()

    # print(pygame.time.get_ticks(),next_time)
    if pygame.time.get_ticks() >= next_time and len(enemies)<=50:
        enemies.append(enemy(random.randint(0,800),random.randint(0,600)))
        group.add(enemies[-1])


    screen.fill(BLACK)
    darw_mouse()
    for sprite in group:
        sprite.update()
    score_image.update()
    
    if not ball.show:
        screen.fill(BLACK)

    if ball.kill():
        # pass
        hp -= 1
        print(hp)
    if hp <= 0:
        ball.show = False


    pygame.display.flip()
    clock.tick(fps)
pygame.quit()   