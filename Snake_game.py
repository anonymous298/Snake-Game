import pygame

pygame.init()

width = 800
height = 500

gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#game specific variables
gameloop = True

while gameloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameloop == False