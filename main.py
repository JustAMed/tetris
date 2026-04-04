import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 900), pygame.RESIZABLE)


clock = pygame.time.Clock()

w,h = pygame.display.get_surface().get_size()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.VIDEORESIZE:
            w,h = pygame.display.get_surface().get_size()
            print(w, h)

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60) 
