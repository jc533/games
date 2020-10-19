import pygame,random
def creat_map(blocks,block_size):
    map_y = {}
    mapx = [[1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20],[1,20],[],[1,4,5,8,11,12,15,15,16,17,20],[1,4,8,12,15,20],[1,4,8,11,12,20],[1,2,3,4,7,8,17],[15,16,17],[12,17,20],[1,3,4,8,9,12,17,20],[1,4,15,16,17,20],[1,4,7,10,12,17,20],[1,20],[1,20],[1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,18,19,20]]
    for c in range(0,len(mapx)):
        map_y[c] = {}
        y = 0+(c)*block_size
        for a in mapx[c]:
            x = 0+(a-1)*block_size
            block = Block(x,y,blocks[0])
            map_y[c][a] = block
    return map_y
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.size = block_size
        self.surface = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = pygame.Rect((x,y,block_size, block_size))
    def update(self):
        screen.blit(self.surface, self.rect)

class Tank(pygame.sprite.Sprite):
    def __init__(self,center_x,center_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank1.png")
        self.size = [45,50] 
        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.rect = self.surface.get_rect()
        self.angle = 0 
        self.speed = [0,0]
        self.rect.center = [center_x, center_y]
    def update(self):
        global group,keys,size
        self.speed = [0,0]
        self.keydown()
        # print(keys)
        if self.touch_wall():
            self.speed = [0,0]
            if keys["w"]:
                self.speed[1 ] = 20
            if keys["s"]:
                self.speed[1] = -20
            if keys["d"]:
                self.speed[0] = -20
            if keys["a"]:
                self.speed[0] = 20
            # if self.speed[0] != 0:
            #     self.speed[0] = self.speed[0] * -3
            # if self.speed[1] != 0:
            #     self.speed[1] = self.speed[1] * -3

        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.surface = pygame.transform.rotate(self.surface,self.angle)
        self.rect.center = [self.rect.center[0]+self.speed[0], self.rect.center[1]+self.speed[1]]
        screen.blit(self.surface, self.rect)
    def touch_wall(self):
        if self.rect.center[0] >= size[0] - self.size[1]/2:
            self.speed[0] = -1
        if self.rect.center[0] <= self.size[0]/2:
            self.speed[0] = 1
        if self.rect.center[1]-self.speed[1] >= size[1] - self.size[1]/2:
            self.speed[1] = -1
        if self.rect.center[1] <= self.size[1]/2:
            self.speed[1] = 1
        for i in game_map:
            for b in game_map[i]:
                collide_list = pygame.sprite.spritecollide(self, [game_map[i][b]], False)
                if collide_list != []:
                    print(collide_list)
                    return True
        return False
    def keydown(self):
        # print(keys)
        if keys["w"]:
            self.speed[1] = -5
            self.angle = 0
        if keys["s"]:
            self.speed[1] = 5
            self.angle = 180
        if keys["d"]:
            self.speed[0] = 5
            self.angle = 270
        if keys["a"]:
            self.speed[0] = -5
            self.angle = 90
class Enemy(Tank):
    def __init__(self,center_x,center_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank1.png")
        self.size = [45,50] 
        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.rect = self.surface.get_rect()
        self.angle = 0 
        self.speed = [0,0]
        self.rect.center = [center_x, center_y]
    def update(self):
        global group,keys,size
        self.speed = [0,0]

        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.surface = pygame.transform.rotate(self.surface,self.angle)
        self.rect.center = [self.rect.center[0]+self.speed[0], self.rect.center[1]+self.speed[1]]
        screen.blit(self.surface, self.rect)
    def touch_wall(self):
        if self.rect.center[0] >= size[0] - self.size[1]/2:
            self.speed[0] = -1
        if self.rect.center[0] <= self.size[0]/2:
            self.speed[0] = 1
        if self.rect.center[1]-self.speed[1] >= size[1] - self.size[1]/2:
            self.speed[1] = -1
        if self.rect.center[1] <= self.size[1]/2:
            self.speed[1] = 1
        for i in game_map:
            for b in game_map[i]:
                collide_list = pygame.sprite.spritecollide(self, [game_map[i][b]], False)
                if collide_list != []:
                    return True
        return False
    def keydown(self):
        # print(keys)
        if keys["w"]:
            self.speed[1] = -5
            self.angle = 0
        if keys["s"]:
            self.speed[1] = 5
            self.angle = 180
        if keys["d"]:
            self.speed[0] = 5
            self.angle = 270
        if keys["a"]:
            self.speed[0] = -5
            self.angle = 90
    # def __init__(self,center_x,center_y):
    #     pygame.sprite.Sprite.__init__(self)
    #     self.image = pygame.image.load("tank1.png")
    #     self.size = [45,50] 
    #     self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
    #     self.rect = self.surface.get_rect()
    #     self.angle = 0 
    #     self.speed = [0,0]
    #     self.rect.center = [center_x, center_y]
    # def update():
    #     self.speed = [0,0]
    #     self.keydown()
    #     if self.touch_wall():
    #         pass
    #         # if self.move["w"]:
    #         #     self.speed[1] *= 1
    #         # if self.move["s"]:
    #         #     self.speed[1] *= -1
    #         # if self.move["d"]:
    #         #     self.speed[0] *= -1
    #         # if self.move["a"]:
    #         #     self.speed[0] *= 1

    #     self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
    #     self.surface = pygame.transform.rotate(self.surface,self.angle)
    #     self.rect.center = [self.rect.center[0]+self.speed[0], self.rect.center[1]+self.speed[1]]
    #     screen.blit(self.surface, self.rect)
    # def touch_wall(self):
    #     if self.rect.center[0] >= size[0] - self.size[1]/2:
    #         self.speed[0] = -1
    #     if self.rect.center[0] <= self.size[0]/2:
    #         self.speed[0] = 1
    #     if self.rect.center[1]-self.speed[1] >= size[1] - self.size[1]/2:
    #         self.speed[1] = -1
    #     if self.rect.center[1] <= self.size[1]/2:
    #         self.speed[1] = 1
    #     for i in game_map:
    #         for b in game_map[i]:
    #             collide_list = pygame.sprite.spritecollide(self, [game_map[i][b]], False)
    #             if collide_list != []:
    #                 return True

class Bullet(pygame.sprite.Sprite):
    def __init__(self, center_x, center_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank_bullet2.png")
        self.speed = [0,0]
        self.fire = False
        self.size = [10,10]
        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.rect = self.surface.get_rect()
        self.rect.center = [center_x, center_y]
    def attack(self):
        global tank
        self.speed = [0,0]
        self.rect.center = tank.rect.center
        # print(self.image.get_width(),self.image.get_height())
        if tank.angle == 0:
            self.speed[1] = -10
        if tank.angle == 180:
            self.speed[1] = 10
        if tank.angle == 270:
            self.speed[0] = 10
        if tank.angle == 90:
            self.speed[0] = -10
    def touch_wall(self):
        for i in game_map:
            for b in game_map[i]:
                collide = pygame.sprite.spritecollide(self, [game_map[i][b]], False)
                if collide != []:
                    return True
        if self.rect.center[0] >= size[0] - self.size[1]/2 or self.rect.center[0] <= self.size[0]/2:
            return True
        elif self.rect.center[1] - self.speed[1] >= size[1] - self.size[1]/2 or self.rect.center[1] <= self.size[1]/2:
            return True
        else:
            return False
    def update(self):
        if self.touch_wall():
            self.speed = [0,0]
            self.rect.center = tank.rect.center
            self.fire = False
        self.surface = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.surface = pygame.transform.rotate(self.surface,0)
        self.rect.center = [self.rect.center[0]+self.speed[0], self.rect.center[1]+self.speed[1]]
        if self.fire:
            screen.blit(self.surface, self.rect)

WHITE = (255,255,255)
RED = (100,0,0)
GREEN = (0,70,0)
BLUE = (0,0,90)
BLACK = (0,0,0)

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
group = pygame.sprite.Group()
keys = {"w":False,"a":False,"s":False,"d":False,"space":False} 
fps = 30
pygame.display.set_caption("tank","pgame")
done = False
next_time = 0
clock = pygame.time.Clock()
tank = Tank(size[0]//2,size[1]//2)
enemy = Enemy(size[0]//2,size[1]//2)
group.add(tank)
group.add(enemy)
bullets = []
for i in range(0,5):
    bullets.append(Bullet(0,0))
    group.add(bullets[i])
block_size = 40
game_map = creat_map(["gamemap.png"],block_size) 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            keys["w"] = False
            keys["a"] = False
            keys["s"] = False
            keys["d"] = False 
            if event.key == 119:
                keys["w"] = True
            elif event.key == 115:
                keys["s"] = True
            if event.key == 97:
                keys["a"] = True
            elif event.key == 100:
                keys["d"] = True
            if event.key == 32:
                keys["space"] = True
        if event.type == pygame.KEYUP:
            if event.key == 119:
                keys["w"] = False
            if event.key == 115:
                keys["s"] = False
            if event.key == 97:
                keys["a"] = False
            if event.key == 100:
                keys["d"] = False
            if event.key == 32:
                keys["space"] = False
    screen.fill(BLACK)
    for i in game_map:
        for a in game_map[i]:
            game_map[i][a].update()
            
    for sprite in group:
        sprite.update()
    if keys["space"]:
        if pygame.time.get_ticks() >= next_time:
            idx = bullets.pop()
            bullets.insert(0,idx)
        if not bullets[-1].fire:
            bullets[-1].attack()
            bullets[-1].fire = True
            next_time = pygame.time.get_ticks()+500
    # print(bullets[-1].fire)
    # print(pygame.time.get_ticks())
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()   