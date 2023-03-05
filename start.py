import pygame
import sys
import random

def draw_rect(x,y,colour):
    rectangle = pygame.Rect(x,y,10,10)
    pygame.draw.rect(display_window, colour, rectangle)
    pygame.display.flip()

def wall_pass(x,y):
    if x > 800 :
        x = 0 
    if x < 0 :
        x = 800
    if y > 400 :
        y = 0
    if y < 0 :
        y = 400
    return x,y

pygame.init()
green = (0,255,0)
black = (0,0,0)
red = (0,0,255)
display_window = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
# print(pygame.K_UP)
x = 0
y = 0
direction = 0
colour = None
# obstacle = (400,200)
draw_rect(400,200,red)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    x,y = wall_pass(x,y)
    draw_rect(x,y,green)
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
        draw_rect(x-10,y,black )
    elif direction == 1 :
        y += 1
        draw_rect(x,y-10,black )
    elif direction == 2 :
        x -= 1
        draw_rect(x+10,y,black)
    elif direction == 3:
        y -= 1
        draw_rect(x,y+10,black)
  
    pygame.display.update()
    clock.tick(50.5)

   
    