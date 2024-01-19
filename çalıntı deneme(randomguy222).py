
# Modification date: Thu Dec  3 21:48:40 2020

# Production date: Sun Sep  3 15:42:51 2023

import pygame
from time import sleep
from random import choices
pygame.init()

side = 500
gameDisplay = pygame.display.set_mode((side, side))
c = 0
s = 0

gameDisplay.fill((255,255,0))
pygame.draw.circle(gameDisplay, (0,122,255), (side/2, side/2), side/2)

while True:
  point = choices(list(range(side)), k=2)
  color = gameDisplay.get_at(point)

  gameDisplay.set_at(point, (0,255,0))
  pygame.display.update()

  if color == (255,255,0):
    s += 1
  elif color == (0,122,255):
    c += 1
  
  print(c/(s+c)*4)
  sleep(0.001)
