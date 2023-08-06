import pygame
from settings import Settings
import helpers

pygame.init()

pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')

# Create an instance of the Settings class
settings = Settings()

# Main game loop
run = True
while run:
    settings.timer.tick(settings.fps)
    settings.screen.fill('violet')
    helpers.draw_board()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
