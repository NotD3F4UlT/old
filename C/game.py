import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Rectangle")

# Define colors
black = (0, 0, 0)
green = (30, 244, 67)

# Rectangle properties
rect_x, rect_y = width // 2, height // 2
rect_width, rect_height = 50, 50
rect_speed = 5
rect_speed1 = 4
rect_speed2 = 3
vx=rect_speed-rect_speed1
#if vx>=0:

    


# Clock object to manage frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rect_x -= rect_speed1
    if keys[pygame.K_d]:
        rect_x += rect_speed
    if keys[pygame.K_w]:
        rect_y -= rect_speed2
    if keys[pygame.K_s]:
        rect_y += rect_speed2

    # Keep the rectangle within the screen bounds
    rect_x = max(0, min(width - rect_width, rect_x))
    rect_y = max(0, min(height - rect_height, rect_y))

    # Fill the screen with black
    screen.fill(black)

    # Draw the rectangle
    pygame.draw.rect(screen, green, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick()
