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
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_rect(x,y)
    
    x += 1
    # if pygame.key.get_pressed()[pygame.K_DOWN] :
    #     y += 1
    

    pygame.display.update()
    clock.tick(60)
   
    