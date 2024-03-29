import sys

import pygame

pygame.init()

size = width, height = 600,400
speed = [1,1]
BLACK = 0,0,0

fps = 300
fclock = pygame.time.Clock()

screen = pygame.display.set_mode(size,pygame.RESIZABLE)
pygame.display.set_caption("My first game design programme")

ball = pygame.image.load("imgs/ball.png")

pygame.display.set_icon(ball)

ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)*int(speed[0]/abs(speed[0]))
            if event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] >= 0 else speed[0] - 1
            if event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] >= 0 else speed[1] - 1
            if event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1)*int(speed[1]/abs(speed[1]))
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width,height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size,pygame.RESIZABLE)
    print(speed)
    if pygame.display.get_active():
        ballrect = ballrect.move(speed[0], speed[1])

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    screen.fill((BLACK))
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)