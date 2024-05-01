#!/usr/bin/env python3

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load("Graphics/Sky.png")
ground_surface = pygame.image.load("Graphics/Ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Drawing all our elements
    # Updating everything
    pygame.display.update()
    clock.tick(60)
