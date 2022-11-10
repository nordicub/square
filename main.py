# libraries
import pygame
import random

# setting up pygame
pygame.init()
# icon, caption, screen, and start ticks
screen = pygame.display.set_mode((800, 680))
pygame.display.set_caption("square")
icon = pygame.image.load('square.png')
pygame.display.set_icon(icon)
# variables
tesla = 0
clock = pygame.time.Clock()
# player X, Y
playerX = 370
playerY = 303
playerX_change = 0
playerY_change = 0
# enemy X, Y
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 600)
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_UP:
                playerY_change = -0.4
            if event.key == pygame.K_DOWN:
                playerY_change = 0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
        # fill + boundaries
    playerX += playerX_change
    playerY += playerY_change
    screen.fill((0, 0, 0))
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 648:
        playerY = 648
    if enemyX <= 0:
        enemyX = 0
    elif enemyX >= 768:
        enemyX = 768
    elif enemyY <= 0:
        enemyY = 0
    elif enemyY >= 648:
        enemyY = 648
    # images
    playerImg = pygame.draw.rect(screen, "white", pygame.Rect(playerX, playerY, 32, 32))
    enemyImg = pygame.draw.rect(screen, "red", pygame.Rect(enemyX, enemyY, 32, 32))
    # enemy controls
    col = pygame.Rect.colliderect(enemyImg, playerImg)
    if col:
        running = False
    evx = random.randint(0, 1)
    evy = random.randint(0, 1)
    if evx == 1:
        enemyX += 2
    else:
        enemyX = enemyX - 2
    if evy == 1:
        enemyY += 2
    else:
        enemyY = enemyY - 2
    # enemy timer
    ct = clock.tick()
    tesla += ct
    if tesla > 5000:
        tesla = 0
    # update
    pygame.display.update()
