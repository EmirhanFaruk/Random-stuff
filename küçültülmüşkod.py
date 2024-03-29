
# Modification date: Mon Oct 11 22:13:24 2021

# Production date: Sun Sep  3 15:42:51 2023

# importing pygame etc
import pygame

# initialize the pygame
pygame.init()

# create the screen(width, height)
screen = pygame.display.set_mode((500, 400))#(y, x)

# Background
background = pygame.image.load("background.png")

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 280
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))#(pic, (x, y))


# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((5, 18, 94))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 --> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # Checking for boundaries of spaceship so it doesn't go out of bounds

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 400:
        playerX = 400


    player(playerX, playerY)
    pygame.display.update()
