import pygame
import sys
import random
def draw_rect():
    rectangle = pygame.Rect(10,10,10,10)
    pygame.draw.rect(display_window, green, rectangle)


pygame.init()
display_window = pygame.display.set_mode((800,400))
green = (0,255,0)
rectangle = pygame.Rect(10,10,10,10)
pygame.draw.rect(display_window, green, rectangle)