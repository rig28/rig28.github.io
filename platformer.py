import pygame
import os

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer Game")

# Player properties
player_size = 30
player_x = 50
player_y = screen_height - player_size - 50
player_speed = 3
player_y_velocity = 5
gravity = 0.4
jump_strength = -12
is_jumping = False

# Platform properties
platform_width = 100
platform_height = 20
platforms = [(200, screen_height - 150, platform_width, platform_height),
             (500, screen_height - 250, platform_width, platform_height)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_y_velocity = jump_strength
                is_jumping = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Apply gravity
    player_y_velocity += gravity
    player_y += player_y_velocity

    # Keep player within screen bounds
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_size:
        player_x = screen_width - player_size
    if player_y > screen_height - player_size:
        player_y = screen_height - player_size
        player_y_velocity = 100
        is_jumping = False

    # Platform collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        platform_rect = pygame.Rect(platform[0], platform[1], platform[2], platform[3])
        if player_rect.colliderect(platform_rect):
            if player_y_velocity > 0 and player_rect.bottom <= platform_rect.bottom:
                player_y = platform[1] - player_size
                player_y_velocity = 10
                is_jumping = False

    # Clear screen
    screen.fill((135, 206, 235))

    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 0), (platform[0], platform[1], platform[2], platform[3]))

    # Update display
    pygame.display.update()

pygame.quit()

# add double jump
#make player img 
player_image = pygame.image.load(os.path.join('images', 'epic pixel dude.png')).convert_alpha()
player_rect = player_image.get_rect()