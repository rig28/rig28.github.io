import pygame
import os

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

player_image = pygame.image.load(os.path.join('images', 'player')).convert_alpha()

player_rect = player_image.get_rect()

player_rect.center = (screen_width // 2, screen_height - 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    # Draw the player image
    screen.blit(player_image, player_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()