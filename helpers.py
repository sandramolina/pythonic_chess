import pygame
import game_variables

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

#  Function that will create the titles of the board (8x8) there are 64 squares, we can draw the half


def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(game_variables.screen, 'light pink', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(game_variables.screen, 'light pink', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(game_variables.screen, 'violet', [
                         0, 800, game_variables.WIDTH, 100])
        pygame.draw.rect(game_variables.screen, 'white', [
                         0, 800, game_variables.WIDTH, 100], 5)
        pygame.draw.rect(game_variables.screen, 'white', [
                         800, 0, 200, game_variables.HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        game_variables.screen.blit(medium_font.render(
            status_text[game_variables.turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(game_variables.screen, 'white',
                             (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(game_variables.screen, 'white',
                             (100 * i, 0), (100 * i, 800), 2)
        game_variables.screen.blit(medium_font.render(
            'Forfeit', True, 'white'), (810, 830))
