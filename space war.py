import pygame,random,math

class Tank(pygame.sprite.Sprite):
    # player
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [x,y]
        self.speed = 0
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        #draw player
        self.pos[0] += self.speed
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)

    def touch_wall(self):
        global size
        if self.pos[0] <= 0:
            return -1
        if self.pos[0] >= size[0]:
            return 1
        else:
            return 0
       


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,x,y,imgs,index):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.wait_time = 200
        self.move_time = pygame.time.get_ticks() + 200
        for image in imgs:
            self.images.append(pygame.image.load(image))
        self.speed = [5,0]
        self.rect = self.images[0].get_rect()
        self.rect.left = x
        self.rect.top = y
        self.pos = [self.rect.centerx,self.rect.centery]
        self.id = index
        self.image_id = 0


    def update(self):
        if pygame.time.get_ticks() >= self.move_time:
            if self.rect.right > size[0] or self.rect.left < 0:
                self.speed[0] *= -1
                # self.wait_time -= 10

            # print(self.pos,self.speed)
            self.pos[0] += self.speed[0]
            # print(self.rect.right,self.rect.left)
            self.move_time = pygame.time.get_ticks() + self.wait_time
            
            self.image_id += 1
            self.image_id %= 2
        self.rect.center = self.pos
        screen.blit(self.images[self.image_id], self.rect)


class Bullet(pygame.sprite.Sprite):

    def __init__(self,x,y,img,index):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.pos = [x,y]
        self.speed = -10
        self.rect  = self.image.get_rect()
        self.rect.center = self.pos
        self.id = index
    
    def update(self):
        self.pos[1] += self.speed
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
        if self.touch_something():
            group.remove(self)
            bullets.remove(self)
            # print("hello there are somethig strange")
            # print(len(bullets))
            # print(group)

    def touch_something(self):
        if self.pos[1] <= 0:
            return 1
        # now
        # collide_list = pygame.sprite.spritecollide(self, [net], False)
        # if collide_list != []:
        #     pass
        # touch enemy            
        

WHITE = (255,255,255)
RED = (200,50,50)
GREEN = (0,70,0)
BLUE = (0,0,90)
BLACK = (0,0,0)

#init pygame
#set window
pygame.init() 
size = (1000,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("space war","space")


fps = 30
done = False
group = pygame.sprite.Group()
clock = pygame.time.Clock()
#set all sprite
tank = Tank(250,550,"space_Tank.png")
enemies = []
enemies.append(Enemy(0,0,["Jellyfish1.png","Jellyfish2.png"],0))
width = enemies[0].rect.w
group.add(enemies[0])
for i in range(1,10):
    enemy = Enemy(enemies[i-1].rect.right+width,0,["Jellyfish1.png","Jellyfish2.png"],i)
    enemies.append(enemy)
    group.add(enemies[i])

bullets = []
next_time = pygame.time.get_ticks()
group.add(tank)









while not done:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            pass
    tank.speed = 0
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if tank.touch_wall() != -1:
            tank.pos[0] -= 7.5

    if pressed[pygame.K_RIGHT]:
        if tank.touch_wall() != 1:
            tank.pos[0] += 7.5

    if pressed[pygame.K_SPACE]:
        if pygame.time.get_ticks() >= next_time: 
            bullets.append(Bullet(tank.pos[0],tank.pos[1],"Shell.png",0))
            group.add(bullets[-1])
            # group.remove(bullets.pop())
            next_time = pygame.time.get_ticks() + 500
    # print(pygame.time.get_ticks())  check time clock
    
    screen.fill(BLACK)
    for sprite in group:
        sprite.update()


    pygame.display.flip()
    clock.tick(fps)
pygame.quit()