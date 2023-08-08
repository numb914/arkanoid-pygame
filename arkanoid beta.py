import pygame as p
import random as r
import time as t

mode = input('Choose the difficulty level from 1 to 3')

print('Click the game icon and wait 5 sec')
if mode == ' 1' or mode == '1':
    speed = 40
    ballSpeed = 0.3
elif mode == ' 2' or mode == '2':
    speed = 60
    ballSpeed = 0.5
elif mode == '3' or mode == ' 3':
    speed = 80
    ballSpeed = 0.7



WIDTH = 1920
HEIGHT = 1080

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


FPS = 60
posx = 700
posy = 1000
posxBall = r.randint(920, 1000)
posyBall = r.randint(1, 780)

dy = 1
dx = r.randint(-1, 1)
while dx == 0:
    dx = r.randint(-1, 1)

block_list = [p.Rect(100 + 180 * i, 11 + 120 * j, 110, 50) for i in range(10) for j in range(4)]
color_list = [(r.randrange(50, 256), r.randrange(50, 256), r.randrange(50, 256)) for i in range(10) for j in range(4)]


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy

    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


p.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('')
clock = p.time.Clock()
clock.tick(FPS)

p.display.flip()
p.display.update()
running = True
t.sleep(5)
while running:
    screen.fill(BLACK)
    paddle = p.draw.rect(screen, PURPLE, (posx, posy, 350, 40))
    ball = p.draw.circle(screen, WHITE, (posxBall, posyBall), 10)

    [p.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    p.display.update()
    p.display.flip()
    if ball.colliderect(paddle) and dy > 0:
        dy *= -1
        ballSpeed += 0.005
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        elif event.type == p.KEYDOWN:
            if event.key == p.K_LEFT and posx > 0:
                posx -= speed
            elif event.key == p.K_RIGHT and (posx + 350) < WIDTH:
                posx += speed

    posxBall += dx * ballSpeed
    posyBall += dy * ballSpeed
    if posxBall <= 0 or posxBall >= WIDTH:
        dx *= -1
        ballSpeed += 0.005
    if posyBall <= 0:
        dy *= -1
        ballSpeed += 0.005
    if posyBall >= HEIGHT:
        screen.fill(WHITE)
        p.display.set_caption('GAME OVER')
        p.font.init()
        font = p.font.SysFont('Arial', 50)
        text = font.render('GAME OVER.', 1, RED, WHITE)
        screen.blit(text, (900, 540))
        p.display.update()
        p.display.flip()
        for i in range(5000):
            p.display.update()
        running = False
    if block_list == []:
        screen.fill(WHITE)
        p.display.set_caption('YOU WON!')
        p.font.init()
        font = p.font.SysFont('Arial', 50)
        text1 = font.render('YOU WON!', 1, GREEN, WHITE)
        screen.blit(text1, (900, 540))
        for i in range(5000):
            p.display.update()
        running = False

p.quit()
