import pygame
import random
import math

##Initialization window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fight The Plane")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
bgImg = pygame.image.load("bg.png")


##Score
score = 0
pygame.init()
font = pygame.font.Font("freesansbold.ttf", 32)

def show_score():
    text = f"Score:{score}"
    score_render = font.render(text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))


##Game over
is_over = False
over_font = pygame.font.Font("freesansbold.ttf", 82)
def check_is_over():
    if is_over:
        text = "Game Over"
        render = font.render(text, True, (255, 0, 0))
        screen.blit(render, (200, 250))


##Player
playerImg = pygame.image.load("player.png")
playerX = 350
playerY = 500
playerStep = 0 ##Player speed

##Enemy
number_of_enemies = 6

class Enemy(object):
    def __init__(self):
        self.img = pygame.image.load("enemy.png")
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(2, 6)

    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)


enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())

enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(200, 600)
enemyY = random.randint(50, 250)
enemyStep = 2 ##Enemy speed
def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if e.x > 736 or e.x < 0:
            e.step *= -1
            e.y += 40
            if e.y > 450:
                is_over = True
                print("Game over")
                enemies.clear()

##Distance
def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)


##Bullet
class Bullet(object):
    def __init__(self):
        self.img = pygame.image.load("bullet.png")
        self.x = playerX + 16
        self.y = playerY + 10
        self.step = 10

    def hit(self):
        global score
        for e in enemies:
            if distance(self.x, self.y, e.x, e.y) < 30:
                bullets.remove(self)
                e.reset()
                score += 1
                print(score)


bullets = []

def show_bullets():
    for b in bullets:
        screen.blit(b.img, (b.x, b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)



##Main loop body
def move_player():
    global playerX
    playerX += playerStep
    if playerX > 736:
        playerX = 736

    if playerX < 0:
        playerX = 0

running = True
while running:
    screen.blit(bgImg, (0, 0))
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##Keyboard press and lift judgment
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 5
            elif event.key == pygame.K_LEFT:
                playerStep = -5
            elif event.key == pygame.K_SPACE:
                print("Fire a bullet......")
                bullets.append(Bullet())

        if event.type == pygame.KEYUP:
            playerStep = 0

    screen.blit(playerImg, (playerX, playerY))
    move_player()
    show_enemy()
    show_bullets()
    check_is_over()
    pygame.display.update()