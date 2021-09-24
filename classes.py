import pygame
import pygame.locals

pygame.init()

vec = pygame.math.Vector2
friction = 0.93
ACC = 0.5
player2 = pygame.sprite.Group()
player1 = pygame.sprite.Group()
buttons = pygame.sprite.Group()
players = pygame.sprite.Group()
walls = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
goals = pygame.sprite.Group()


class xplayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect()
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)
        self.pos = vec(0, 25)
        player1.add(self)
        players.add(self)
        allSprites.add(self)
        self.rect.center = self.pos
        self.oldPos = [self.pos, self.pos, self.pos, self.pos, self.pos]

    def update(self):
        self.oldPos.append(self.pos)
        self.oldPos = self.oldPos[1:6]
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT]:
            self.acc.x = ACC
        elif keys[pygame.locals.K_LEFT]:
            self.acc.x = ACC * -1
        else:
            self.acc.x = 0
        self.vel = self.acc + self.vel * friction
        self.pos = self.pos + self.vel
        if pygame.sprite.spritecollide(self, player2, False):
            for entity in player2:
                entity.vel.x = self.vel.x * 1.5
                self.pos = self.oldPos[2]
                self.vel = vec(0, 0)
        if pygame.sprite.spritecollide(self, walls, False):
            self.pos = self.oldPos[3]
            self.vel = vec(0, 0)
        self.rect.center = self.pos


class yplayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
        player2.add(self)
        players.add(self)
        allSprites.add(self)
        self.acc = vec()
        self.vel = vec(0, 0)
        self.pos = vec(25, 0)
        self.rect.center = self.pos
        self.oldPos = [self.pos, self.pos, self.pos, self.pos, self.pos]

    def update(self):
        self.oldPos.append(self.pos)
        self.oldPos = self.oldPos[1:6]
        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_DOWN]:
            self.acc.y = ACC
        elif keys[pygame.locals.K_UP]:
            self.acc.y = ACC * -1
        else:
            self.acc.y = 0
        self.vel = self.acc + self.vel * friction
        self.pos = self.pos + self.vel
        if pygame.sprite.spritecollide(self, player1, False):
            for entity in player1:
                entity.vel.y = self.vel.y * 1.5
                self.pos = self.oldPos[2]
                self.vel = vec(0, 0)
        if pygame.sprite.spritecollide(self, walls, False):
            self.pos = self.oldPos[3]
            self.vel = vec(0, 0)
        self.rect.center = self.pos


class wall(pygame.sprite.Sprite):
    def __init__(self, topleft, botright, color=(0, 0, 0), frict=0.93):
        super().__init__()
        self.surf = pygame.Surface((botright - topleft))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.rect.topleft = topleft
        allSprites.add(self)
        walls.add(self)

    def collide(self):
        pass


        #trying to create more stable hitboxes and god
        # if pygame.sprite.spritecollide(self, players, False) :
        #   for entity in players:
        #     if entity.rect.left < self.rect.right and entity.rect.left > self.rect.left and entity.rect.bottom > self.rect.top and entity.rect.top < self.rect.bottom:
        #       print("colliding")
        #       if entity.rect.left > self.rect.center :
        #         entity.rect.left = self.rect.right + 1
        # if entity.rect.right > self.rect.left and entity.rect.right < self.rect.right:
        #   entity.rect.right = self.rect.left - 1
        # if entity.rect.top < self.rect.bottom and entity.rect.top > self.rect.top:
        #   entity.rect.top = self.rect.bottom + 1
        # if entity.rect.bottom > self.rect.top and entity.rect.bottom < self.rect.bottom:
        #   entity.rect.bottom = self.rect.top
class goal(pygame.sprite.Sprite):
    def __init__(self, winFunct, Pos=(vec(75, 425))):
        super().__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=Pos)
        self.winFunct = winFunct
        goals.add(self)

    def update(self):
        if pygame.sprite.spritecollide(self, players, False):
            self.winFunct()
class button(pygame.sprite.Sprite):
  def __init__(self, buttonfunct, pos = (0, 0)):
    super().__init__()
    self.surf = pygame.Surface((10,10))
    self.rect = self.surf.get_rect()
    self.rect.center = pos
    self.pos = self.rect.center
    self.funct = buttonfunct
    buttons.add(self)
  def update(self):
    if pygame.sprite.spritecollide(self, players, False):
      self.funct()
    




    self.rect.center = self.pos