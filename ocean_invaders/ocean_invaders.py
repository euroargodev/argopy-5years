#!/usr/bin/env python
# coding: utf-8
# Source code:
#
# Adapted from:
# https://www.codingal.com/coding-for-kids/blog/space-invaders-game-using-python/
# https://github.com/attreyabhatt/Space-Invaders-Pygame


import math
import random
import pygame
from pathlib import Path
from pygame import mixer

#
ASSETS = Path("assets")
display_width, display_height = 600, 800  # Should fit background image size

game_speed = 1.5  # Adjust game play speed here
num_of_enemies = 6

if __name__ == "__main__":

    # Intialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((display_width, display_height))

    # Background
    background = pygame.image.load(ASSETS.joinpath('background.jpeg'))

    # Sound
    mixer.music.load(ASSETS.joinpath("background.wav"))
    mixer.music.play(-1)

    # Caption and Icon
    pygame.display.set_caption("Ocean Invaders")
    icon = pygame.image.load(ASSETS.joinpath('argopy_logo_square_64.png'))
    pygame.display.set_icon(icon)

    # Player
    playerImg = pygame.image.load(ASSETS.joinpath('boat.png'))  # 64x64
    playerX = display_width/2 - 64/2
    playerY = 30
    playerX_change = 0

    # Enemy
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load(ASSETS.joinpath('enemy.png')))  # 64x64
        enemyX.append(random.randint(0, display_width - 64))
        enemyY.append(random.randint(display_height - 64 - 100, display_height - 64))
        enemyX_change.append(game_speed*3)
        enemyY_change.append(-game_speed*40)

    # Bullet
    # Ready - You can't see the bullet on the screen
    # Fire - The bullet is currently moving

    bulletImg = pygame.image.load(ASSETS.joinpath('float.png'))  # 32x32
    bulletX = 0
    bulletY0 = playerY+32
    bulletY = bulletY0
    bulletX_change = 0
    bulletY_change = -game_speed*10
    bullet_state = "ready"

    # Score
    score_value = 0
    font = pygame.font.Font(ASSETS.joinpath('FreeSansBold.ttf'), 24)
    textX = 10
    testY = 5

    # Game Over
    over_font = pygame.font.Font(ASSETS.joinpath('FreeSansBold.ttf'), 64)

    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (display_width/2 - 200, display_height/2))

    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False

    # Game Loop
    running = True
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))

        # Background Image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = game_speed*-5
                if event.key == pygame.K_RIGHT:
                    playerX_change = game_speed*5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound(ASSETS.joinpath("splash.wav"))
                        bulletSound.set_volume(0.2)
                        bulletSound.play()
                        bulletSound.fadeout(500)
                        # Get the current x cordinate of the spaceship
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= display_width-64:
            playerX = display_width-64

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] < 64:
                for j in range(num_of_enemies):
                    enemyY[j] = -2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = game_speed*3
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= display_width-64:
                enemyX_change[i] = game_speed*-3
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound(ASSETS.joinpath("explosion.wav"))
                explosionSound.play()
                bulletY = playerY
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, display_width-64)
                enemyY[i] = random.randint(display_height - 64 - 100, display_height - 64)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY > display_height - 32:
            bulletY = playerY
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
