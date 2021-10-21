import pygame
from paddle import Paddle
from ball import Ball
pygame.init()

screen_width = 700
screen_height = 500
pygame.display.set_caption("Pong")
#   Colors:
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 00, 00)


screen = pygame.display.set_mode((screen_width, screen_height))

#   Paddles
paddleA = Paddle(white, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(white, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
ball.accelerate(1)

clock = pygame.time.Clock()
scoreA = 0
scoreB = 0


def Game():
    global scoreA
    global scoreB
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
        scoreA += 1
        ball.resetPos(white)
        ball.velocity = [0, 0]
        ball.delay(1, 1)

    if ball.rect.x <= 0:
        scoreB += 1
        ball.resetPos(white)
        ball.velocity = [0, 0]
        ball.delay(1, -1)

    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(black)

    pygame.draw.line(screen, white, [349, 0], [349, 500])

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), True, white)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), True, white)
    screen.blit(text, (420, 10))

    pygame.display.flip()
    clock.tick(60)


running = True
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
                text = font.render("PAUSED", True, white)
                screen.blit(text, (125, 194))
                font = pygame.font.Font(None, 30)
                text = font.render("PRESS SPACE TO UNPAUSE", True, white)
                screen.blit(text, (210, 294))
                pygame.display.flip()
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    break
                elif event.type == pygame.QUIT:
                    running = False
                    break
    Game()
pygame.quit()
