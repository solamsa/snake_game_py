import pygame
import sys
import random
def draw_rect(x,y):
    rectangle = pygame.Rect(x,y,10,10)
    pygame.draw.rect(display_window, green, rectangle)
    pygame.display.flip()

pygame.init()
green = (0,255,0)
display_window = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
# print(pygame.K_UP)
x = 0
y = 0
direction = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_rect(x,y)
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] :
        direction = 1
    elif pressed[pygame.K_LEFT] :
        direction = 2
    elif pressed[pygame.K_UP] :
        direction = 3
    elif pressed[pygame.K_RIGHT] :
        direction = 0

    if direction == 0:
        x += 1
    elif direction == 1 :
        y += 1
    elif direction == 2 :
        x -= 1
    elif direction == 3:
        y -= 1
 
    if x > 800 :
        x = 0 
    if x < 0 :
        x = 800
    if y > 400 :
        y = 0
    if y < 0 :
        y = 400

    pygame.display.update()
    clock.tick(60)

   
    