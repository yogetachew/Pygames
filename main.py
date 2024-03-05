import pygame
import os
import time 
import random

WIDTH, HEIGHT = 650, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# lod the images
# this line of code is saying from the pygame menu use the image 
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# load the player ship image
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# load the leasers image
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# load the backgound 
BG = pygame.image.load(os.path.join("assets", "background-black.png"))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()