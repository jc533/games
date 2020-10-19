import pygame,random

class SpriteModel(pygame.sprite.Sprite):
    
    def __init__(self, x, y, size, color):
        super().__init__()
        self.pos = [x, y]
        self.speed = [0, 0]
        self.size = size
        self.color = color
        # self.img = pygame.image.load(image)
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.center = self.pos

    def update(self):
        #draw player
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.rect.center = self.pos
        screen.blit(self.surface, self.rect)

class Snake(SpriteModel):

    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)
        self.direction = None

    def touch_wall(self):
        if self.pos[0] < self.size/2 or self.pos[0] > width-(self.size/2):
            return True
        elif self.pos[1] < self.size/2 or self.pos[1] > height-(self.size/2):
            return True
        return False

class SnakeBody(SpriteModel):

    def __init__(self, x, y, size, color):
        super().__init__(x, y, size, color)


class Apple(SpriteModel):

    def __init__(self, size, color):
        super().__init__(0, 0, size, color)
        self.set_pos()

    def set_pos(self):
        randx, randy = random.randint(1, 39), random.randint(1, 19)
        randx = 10 + (randx-1)*20
        randy = 10 + (randy-1)*20
        self.pos = [randx, randy]

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


class Text(pygame.sprite.Sprite):

    def __init__(self, center_x, center_y, font, font_size):
        self.font = pygame.font.Font(font, font_size)
        self.image = self.font.render(str(0), 1, (255, 255, 255))
        self.pos = [center_x, center_y]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self,text):
        self.image = self.font.render(text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)

def touch_something(thing1,things2):
    collide_list = pygame.sprite.spritecollide(thing1, things2, False)
    if collide_list != []:
        return True
    return False

    
pygame.init()
size = width,height = 800,400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game")
done = False
over = False
fps = 10
clock = pygame.time.Clock()


score = 0
score_text = Score(30, 30, 'freesansbold.ttf', 30)
over_text = Text(width/2, height/2, 'freesansbold.ttf', 30)


group = pygame.sprite.Group()
player = Snake(410, 210, 20, (255, 255, 255))


apple = Apple(20, (255, 0, 0))
snake_bodyies = []


group.add(player)
group.add(apple)




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if player.direction != 270:
            player.speed = [0,-20]
            player.direction = 90
    if pressed[pygame.K_LEFT]:
        if player.direction != 180:
            player.speed = [-20, 0]
            player.direction = 0
    if pressed[pygame.K_DOWN]:
        if player.direction != 90:
            player.speed = [0, 20]
            player.direction = 270
    if pressed[pygame.K_RIGHT]:
        if player.direction != 0:
            player.speed = [20, 0]
            player.direction = 180

    screen.fill((0,0,0))

    if not over:
        score_text.update()
        for index in range(len(snake_bodyies)-1,-1,-1):
            if index == 0:
                next_pos = player.pos
            else:
                next_pos = snake_bodyies[index-1].pos
            snake_bodyies[index].pos[0] = next_pos[0]
            snake_bodyies[index].pos[1] = next_pos[1]
            snake_bodyies[index].update()

        for sprite in group:
            sprite.update()
        
        if touch_something(player,[apple]):
            apple.set_pos()
            score += 1
            if len(snake_bodyies) == 0:
                body_posx, body_posy = player.pos
            else:
                body_posx, body_posy = snake_bodyies[-1].pos

            for i in range(3):
                if player.direction == 90:
                    body_posy += 20
                if player.direction == 270:
                    body_posy -= 20
                if player.direction == 0:
                    body_posx += 20
                if player.direction == 180:
                    body_posx -= 20
                sb = SnakeBody(body_posx, body_posy, 20, (255,255,255))
                snake_bodyies.append(sb)
        if touch_something(player,snake_bodyies) or player.touch_wall():
            over = True
    if over:
        length = len(snake_bodyies)
        over_text.update("score: %d length: %d" %(score,length))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
