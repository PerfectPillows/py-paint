import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
LIGHT_GREY = (211, 211, 211)
FPS = 240

WIDTH, HEIGHT =  600,700

ROWS = COLS = 80

TOOLBAR_HEIGHT =  HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS 

DRAW_GRID_LINES = False
BG_COLOR = WHITE

def get_font(size):
    return pygame.font.SysFont('comicsans',size)