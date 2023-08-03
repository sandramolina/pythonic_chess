import pygame
import game_variables
import helpers

pygame.init()

pygame.display.set_caption('🐍🐍 Welcome to the Pythonic Chess 🐍🐍')


# Main game loop
run = True
while run:
    game_variables.timer.tick(game_variables.fps)
    game_variables.screen.fill('violet')
    helpers.draw_board()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
