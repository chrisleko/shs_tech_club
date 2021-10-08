#---------------------------------File Imports---------------------------------#
import classes
import pygame
import pygame.locals
import time
from sys import exit
#---------------------------------Pygame Initiation---------------------------------#
pygame.init()
#---------------------------------Pygame Settings---------------------------------#
width = 500
height = 500
Frames = pygame.time.Clock()
FPS = 60
fontLarge = pygame.font.SysFont('comicsans', 30)
displaySurf = pygame.display.set_mode((width, height))
displaySurf.fill((255,255,255))
pygame.display.set_caption("Project L3k0")
vec = pygame.math.Vector2
#---Players---#
p1 = classes.xplayer()
p2 = classes.yplayer()
p3 = classes.xplayer()
#---Conditions---#
win = False
def lvl1win():
  global win 
  win = True
#---------------------------------Game Objects/Physicals---------------------------------#
w1 = classes.wall(vec(0, 450), vec(500, 500), (0, 0, 0))
w2 = classes.wall(vec(0, 0), vec(500, 50))
w3 = classes.wall(vec(0, 0), vec(50, 500))
w4 = classes.wall(vec(450, 0), vec(500, 500))
G1 = classes.goal(lvl1win)
w5 = classes.wall(vec(120, 20), vec(145, 145))
w6 = classes.wall(vec(0, 120), vec(145, 145))
p3.pos = vec(70, 70)
layer0 = pygame.sprite.Group()
for goal in classes.goals:
  layer0.add(goal)
layer1 = pygame.sprite.Group()
for barrier in classes.walls:
  layer1.add(barrier)
layer2 = pygame.sprite.Group()
for entity in classes.players:
  layer2.add(entity)
b1 = classes.button(lvl1win, (200, 90))
layer2.add(b1)
#---------------------------------Reset Function---------------------------------#
def reset():
  p1.pos = (width/2, height/2 + 25)
  p2.pos = (width/2, height/2)
reset()
#---------------------------------Main Function---------------------------------#
def main():
  
  pygame.display.set_caption('Project L3k0')
  while True:
    if pygame.key.get_pressed()[pygame.locals.K_r]:
      time.sleep(0.5)
      reset()
#---Conditionals---#
    for event in pygame.event.get():
      if event.type == pygame.QUIT: exit()
    for entity in classes.players:
      entity.update()
    for goal in classes.goals:
      goal.update()
#---Update Feature---#
    b1.update()
    pygame.display.update()
#---Display Conditionals---#
    displaySurf.fill((255, 255, 255))
    for entity in layer0:
      displaySurf.blit(entity.surf, entity.rect)
    for entity in layer1:
      displaySurf.blit(entity.surf, entity.rect)
    for entity in layer2:
      displaySurf.blit(entity.surf, entity.rect)
    if win:
      displaySurf.blit(fontLarge.render("YOU WIN!", True, (255, 100, 0)), (width/2, height/2))
    Frames.tick(FPS)
main()
