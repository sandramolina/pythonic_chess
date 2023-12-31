import pygame
from settings import Settings

# Create an instance of the Settings class
settings = Settings()
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
            pygame.draw.rect(settings.screen, 'light pink', [
                             600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(settings.screen, 'light pink', [
                             700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(settings.screen, 'violet', [
                         0, 800, settings.WIDTH, 100])
        pygame.draw.rect(settings.screen, 'white', [
                         0, 800, settings.WIDTH, 100], 5)
        pygame.draw.rect(settings.screen, 'white', [
                         800, 0, 200, settings.HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        settings.screen.blit(medium_font.render(
            status_text[settings.turn_step], True, 'black'), (20, 820))

        # Adds horizontal and vertical lines to the board
        for i in range(9):
            pygame.draw.line(settings.screen, 'white',
                             (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(settings.screen, 'white',
                             (100 * i, 0), (100 * i, 800), 2)
        settings.screen.blit(medium_font.render(
            'Forfeit', True, 'white'), (810, 830))

#  draw pieces into the board


def draw_pieces():
    for i in range(len(settings.white_pieces)):
        index = settings.piece_list.index(settings.white_pieces[i])
