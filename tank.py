import pygame,random,math,time,datetime,sys
from pygame.locals import*
class Tank():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    def rest(self):
        self.pos = [400,322]
        self.size = [45,50]
        self.v = [0,0]
        self.angle = 0
    def step(self):
        self.pos[0] += self.v[0]/2
        self.pos[1] += self.v[1]/2
        if self.pos[0] > 800 - self.size[0]/2:
            self.pos[0] = 800 - self.size[0]/2 
        if self.pos[0] < 15:
            self.pos[0] = 15
        if self.pos[1] > 600 - self.size[1]/2:
            self.pos[1] = 600 - self.size[1]/2
        if self.pos[1] < 15:
            self.pos[1] = 15

class Ememy():
    def __init__(self,image_file):
        self.image = pygame.image.load(image_file)
        self.rest()
    def rest(self):
        self.pos = [random.randint(0,600),random.randint(0,400)]
        self.size = [45,50]
        self.time = random.randint(5,7)
        self.show = False
        self.direction = ""
        self.start = datetime.datetime.now() 
        self.id = 0
        self.attack = True
        self.angle = 0
        self.v = [0,0]
    def fire(self,ememy_bullets,ememy_bulletid):
        # print("hi")
        for i in range(len(ememy_bulletid)-1,0,-1):
            if ememy_bulletid[i] == self.id or ememy_bulletid[i] == -1:
                print(ememy_bullets[i],'\n')
                distance = get_distance(self,ememy_bullets[i])
                if distance >= 200:
                    idx = ememy_bullets[i]
                    del(ememy_bullets[i])
                    # length = len(ememy_bullets)
                    ememy_bullets.insert(0,idx)
                    del(ememy_bulletid[i])
                    # length = len(ememy_bulletid)
                    ememy_bulletid.insert(0,self.id)
                    print(ememy_bullets[-1].pos, '\n')
        #     print("abcd")
        # z=0 
        # for i in range(0,len(ememy_bullets)):
        #     if ememy_bullets[i].fire:
        #         z+=1
        #         print(z)
        # print(ememy_bullets[0])
        if not ememy_bullets[-1].fire:
            bullet_fire(self,ememy_bullets[-1],self.direction)
    def step(self):
        global tank,ememy_bullets,ememies,ememy_bulletid
        for e in ememies:
            if self.pos[0] == e.pos[0] and self.pos[1] == e.pos[1] or not e.show:
                continue
            if hit(self,e):
                self.attack = False
                self.v[0] *= -1
                e.v[1] *= -1
                break
            elif get_distance(self,e) <= 40: 
                if abs(self.pos[0] - e.pos[0]) < 40:
                    self.v[0] *= -1
                if abs(self.pos[1] - e.pos[1]) < 40 :
                    self.v[1] *= -1
                break
            else:
                self.attack = True
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        if self.attack:
            if abs(self.pos[0] - tank.pos[0]) < abs(self.pos[1] - tank.pos[1]):
                if self.pos[0] > tank.pos[0] + tank.size[0] / 2 or self.pos[0] < tank.pos[0] - tank.size[0] /  2:
                    if self.pos[0] - tank.pos[0] < 0:
                        self.direction = "right"
                        tank_move("ememy",self,270,0,"right",2)
                    else:
                        self.direction = "left"
                        tank_move("ememy",self,90,0,"left",2)
                else:
                    if self.pos[1] - tank.pos[1] < 0:
                        self.v = [0,0]
                        self.direction = "down"
                        self.angle = 180
                        self.fire(ememy_bullets,ememy_bulletid)
                    else:
                        self.v = [0,0]
                        self.direction = "up"
                        self.angle = 360
                        self.fire(ememy_bullets,ememy_bulletid)
            if abs(self.pos[0] - tank.pos[0]) >= abs(self.pos[1] - tank.pos[1]):    
                if self.pos[1] > tank.pos[1] + tank.size[1] / 2 or self.pos[1] < tank.pos[1] - tank.size[1] / 2:
                    if self.pos[1] - tank.pos[1] < 0:
                        tank_move("ememy",self,180,1,"down",2)
                    else:
                        tank_move("ememy",self,360,1,"up",2)
                else:
                    if self.pos[0] - tank.pos[0] < 0:
                        self.v = [0,0]
                        self.direction = "right"
                        self.angle = 270
                        self.fire(ememy_bullets,ememy_bulletid)
                    else:
                        self.v = [0,0]
                        self.direction = "left"
                        self.angle = 90
                        self.fire(ememy_bullets,ememy_bulletid)
class Bullet():
    def __init__(self,image_file):
        self.fire = False
        self.pos = [100,100]
        self.size = [10,10]
        self.v = [0,0]
        self.angle = 360
        self.image = pygame.image.load(image_file)
    
    def step(self):
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]

        if self.pos[0] >= 800 - self.size[0] or self.pos[0] <= 15:
            self.fire = False

        if self.pos[1] > 600 - self.size[1] or self.pos[1] <= 15:
            self.fire = False

def terminate():
    pygame.quit()
    sys.exit()

def get_distance(sprite1,sprite2):
    return math.sqrt((sprite1.pos[0] - sprite2.pos[0])**2 + (sprite1.pos[1] - sprite2.pos[1])**2)

def drawsprite(screen,sprite,degree):
    sprite_surface = pygame.transform.scale(sprite.image, (sprite.size[0], sprite.size[1]))
    sprite_surface = pygame.transform.rotate(sprite_surface,degree)        
    spriteRect = sprite_surface.get_rect()
    spriteRect.center = (sprite.pos[0], sprite.pos[1])
    screen.blit(sprite_surface, spriteRect)

def hit(sprite1,sprite2):
    distance = get_distance(sprite1,sprite2)
    if distance < (sprite1.size[0] + sprite2.size[0]) / 2:
        return True
def tank_move(species,tank,degree,speed_idx,direction,speed):
    tank.v = [0,0]
    tank.angle = degree
    if direction == "up" or direction == "left":
        tank.v[speed_idx] = -speed
    else:
        tank.v[speed_idx] = speed       
def bullet_fire(tank,bullet,direction):
    bullet.fire = True
    bullet.angle = tank.angle
    bullet.v = [0,0]
    bullet.pos[0],bullet.pos[1] = tank.pos
    if direction == "down":
        bullet.v[1] = 10
    elif direction == "left": 
        bullet.v[0] = -10
    elif direction == "right":
        bullet.v[0] = 10
    else:
        bullet.v[1] = -10

pygame.init()
screen = pygame.display.set_mode((800, 600),16)
pygame.display.set_caption('tank')
font = pygame.font.Font(None, 50) 
bgcolor = (0, 0, 0)
over = False
hp = 15
score = 0
hp_text = font.render("hp:"+str(hp), 1, (255,255,255))
score_text = font.render("score:"+str(score), 1, (255,255,255))
point_pos = [10,40]
textpos = [10,10]
bullets = []
ememy_bullets = []
ememy_bulletid = [-1,-1,-1,-1,-1]
tank = Tank("tank1.png")
ememies = []
tank_direction = "up"
keys = {"up": False,"down": False,"right": False,"left": False,"space": False}
move = {"up": True,"down": True,"right": True,"left": True}
start = datetime.datetime.now()
now = datetime.datetime.now()
clock = pygame.time.Clock()

for i in range(0,5):
    bullets.append(Bullet("tank_bullet2.png"))
    ememy_bullets.append(Bullet("tank_bullet2.png"))
for i in range(0,5):
    ememies.append(Ememy("tank1.png"))
    ememies[i].id = i
    for i in range(0,len(ememies)):
        if get_distance(ememies[i-1],ememies[i]) <= 300:
            ememies[i].rest()
while True:
    if not over:
        screen.fill(bgcolor)
        now = datetime.datetime.now()
        for e in ememies:
            if not e.show:
                continue
            if abs(tank.pos[0] + abs(tank.v[0]) - e.pos[0]) <= 50:
                if abs(tank.pos[1] + abs(tank.v[1]) - e.pos[1]) <= 50:
                    if tank.pos[0] - e.pos[0] >= 0:
                        if (tank.pos[0] - tank.size[0] / 2) - (e.pos[0] + e.size[0] / 2) <= 50:
                            move["left"] = False
                            tank.v[0] *= -1
                    if tank.pos[0] - e.pos[0] <= 0:
                        if abs((tank.pos[0] + tank.size[0] / 2) - (e.pos[0] - e.size[0] / 2)) <= 50: 
                            move["right"] = False
                            tank.v[0] *= -1
                    if tank.pos[1] - e.pos[1] >= 0:
                        if abs((tank.pos[1] - tank.size[1] / 2) - (e.pos[1] + e.size[1] / 2)) <= 50: 
                            move["up"] = False
                            tank.v[1] *= -1
                    if tank.pos[1] - e.pos[1] <= 0:
                        if abs((tank.pos[1] + tank.size[1] / 2) - (e.pos[1] - e.size[1] / 2)) <= 50: 
                            move["down"] = False
                            tank.v[1] *= -1
                    break
            move = {"up": True,"down": True,"right": True,"left": True}
        drawsprite(screen,tank,tank.angle)
        tank.step()
        screen.blit(hp_text, textpos)
        screen.blit(score_text, point_pos)
        for ememy in ememies:
            if get_distance(ememy,tank) <= 100 and not ememy.show:
                ememy.rest()
                for i in range(0,len(ememies)):
                    if get_distance(ememy,ememies[i]) <= 350:
                        ememy.rest()
            if ememy.show:
                drawsprite(screen,ememy,ememy.angle)
            if abs(now.second - ememy.start.second) == ememy.time and now.second - e.start.second >= 0:
                ememy.show = True
            elif 60 - e.start.second + now.second == ememy.time:
                ememy.show = True
            if not hit(ememy,tank) and ememy.show:
                ememy.step()
            for b in bullets:
                if not ememy.show:
                    continue
                if b.fire and hit(ememy,b):
                    ememy.show = False
                    ememy.rest()
                    b.fire = False
                    score += 5
                    score_text = font.render("score:"+str(score), 1, (255,255,255)) 
        for bullet in bullets:
            if bullet.fire:
                bullet.angle = tank.angle
                drawsprite(screen,bullet,bullet.angle)
                bullet.step()
                for e in ememy_bullets:
                    if e.fire and hit(e,bullet):
                        bullet.fire = False
                        e.fire = False
                        break
        for bullet in ememy_bullets:
            # print(ememy_bulletid,ememy_bullets)
            if bullet.fire and hit(tank,bullet):
                bullet.fire = False
                ememy_bulletid[ememy_bullets.index(bullet)] = -1 
                hp -= 1 
                hp_text = font.render("hp:" + str(hp), 1, (255,255,255))
                if hp == 0:
                    over = True
            if bullet.fire:
                drawsprite(screen,bullet,bullet.angle)
                bullet.step()
        if keys["up"] and move["up"]:
            tank_direction = "up"
            tank_move("tank",tank,360,1,tank_direction,20)
        elif keys["down"] and move["down"]:
            tank_direction = "down"
            tank_move("tank",tank,180,1,tank_direction,20)
        if keys["right"] and move["right"]:
            tank_direction = "right"
            tank_move("tank",tank,270,0,tank_direction,20)
        elif keys["left"] and move["left"]:
            tank_direction = "left"
            tank_move("tank",tank,90,0,tank_direction,20)
        if keys["space"]:
            distance =  get_distance(bullets[-1],tank)
            if distance > 200:
                bullets.insert(0,bullets.pop())
            if not bullets[-1].fire:
                bullet_fire(tank,bullets[-1],tank_direction)
    for event in pygame.event.get():    
        if event.type == KEYDOWN:
            if event.key == K_e:
                over = True
            if event.key == K_w:
                keys["up"] = True
            if event.key == K_s:
                keys["down"] = True
            if event.key == K_d:
                keys["right"] = True
            if event.key == K_a:
                keys["left"] = True               
            if event.key == K_SPACE:
                keys["space"] = True
            if event.key == K_r:
                tank.rest()
                for bullet in bullets:
                    bullet.fire = False
                for bullet in ememy_bullets:
                    bullet.fire = False
                ememies = []
                for i in range(0,10):
                    ememies.append(Ememy("tank1.png"))
                hp = 15
                score = 0
                hp_text = font.render("hp:" + str(hp), 1, (255,255,255))
                score_text = font.render("score:"+str(score), 1, (255,255,255))
                over = False
            if event.key == K_ESCAPE:
                terminate()
        if event.type == KEYUP:
            if event.key == K_e:
                over = False
            if event.key == K_SPACE:
                keys["space"] = False
            else:
                tank.v[0],tank.v[1] = 0,0
            if event.key == K_w:
                keys["up"] = False
            if event.key == K_s:
                keys["down"] = False
            if event.key == K_d:
                keys["right"] = False
            if event.key == K_a:
                keys["left"] = False
        if event.type == QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(60)
    # pygame.display.update()
