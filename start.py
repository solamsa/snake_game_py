import pygame
import sys
import random
def draw_rect(x,y):
    rectangle = pygame.Rect(0,0,10,10)
    pygame.draw.rect(display_window, green, rectangle)
    pygame.display.flip()

pygame.init()
green = (0,255,0)
display_window = pygame.display.set_mode((800,400))
# print(pygame.K_UP)
x = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw_rect()
    