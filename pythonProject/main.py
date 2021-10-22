import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

screen_width = 700
screen_height = 500
pygame.display.set_caption("Pong")
#   Colors:
black = (0, 0, 1)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 00, 00)

background = black
color_list = [white, green, blue, red]

current_color = white

screen = pygame.display.set_mode((screen_width, screen_height))

#   Paddles
paddleA = Paddle(current_color, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(current_color, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
ball.delay(1.5, ball.accelerate, 1)

clock = pygame.time.Clock()
scoreA = 0
scoreB = 0

running = True
n = 0
x = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            while True:
                font = pygame.font.Font(None, 170)
                text = font.render("PAUSED", True, current_color)
                screen.blit(text, (125, 194))
                font = pygame.font.Font(None, 30)
                text = font.render("PRESS SPACE TO UNPAUSE", True, current_color)
                screen.blit(text, (210, 294))
                pygame.display.flip()
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break
                elif event.type == pygame.QUIT:
                    running = False
                    break

        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            if n < 3:
                n += 1
                current_color = color_list[n]
                ball.changeColor(current_color)
                paddleA.changeColor(current_color)
                paddleB.changeColor(current_color)
            else:
                n = 0
                current_color = color_list[n]
                ball.changeColor(current_color)
                paddleA.changeColor(current_color)
                paddleB.changeColor(current_color)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if x < 1:
                x += 1
            else:
                x = 0
            if x == 0:
                background = black
                color_list[0] = white
                current_color = color_list[0]
                ball.changeColor(current_color)
                paddleA.changeColor(current_color)
                paddleB.changeColor(current_color)

            if x == 1:
                background = white
                color_list[0] = black
                current_color = color_list[0]
                ball.changeColor(current_color)
                paddleA.changeColor(current_color)
                paddleB.changeColor(current_color)


        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if scoreA >= 11 or scoreB >= 11:
                scoreA = 0
                scoreB = 0
                ball.rect.x = 345
                ball.rect.y = 195
                ball.velocity = [0, 0]
                ball.delay(1, ball.accelerate, 1)
                paddleA.rect.y = 200
                paddleB.rect.y = 200

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        if scoreA < 11:
            scoreA += 1
            ball.resetPos(current_color)
            ball.velocity = [0, 0]
            ball.delay(1, ball.accelerate, 1)

    if ball.rect.x <= 0:
        if scoreB < 11:
            scoreB += 1
            ball.resetPos(current_color)
            ball.velocity = [0, 0]
            ball.delay(1, ball.accelerate, -1)

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(background)

    pygame.draw.line(screen, current_color, [349, 0], [349, 500])

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), True, current_color)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), True, current_color)
    screen.blit(text, (420, 10))

    if scoreA >= 11:
        ball.velocity = [0, 0]
        font = pygame.font.Font(None, 110)
        text = font.render("PlayerA Won!", True, current_color)
        screen.blit(text, (110, 194))
        font = pygame.font.Font(None, 80)
        text = font.render("Press r to restart", True, current_color)
        screen.blit(text, (135, 284))

    if scoreB >= 11:
        ball.velocity = [0, 0]
        font = pygame.font.Font(None, 110)
        text = font.render("PlayerB Won!", True, current_color)
        screen.blit(text, (110, 194))
        font = pygame.font.Font(None, 80)
        text = font.render("Press r to restart", True, current_color)
        screen.blit(text, (135, 284))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
