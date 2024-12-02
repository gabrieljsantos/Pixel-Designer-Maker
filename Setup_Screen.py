import pygame

def setup_screen():
    # Inicialize o Pygame
    pygame.init()

    # Defina as dimensões da tela
    screen_width = 1000
    screen_height = 800

    # Crie a tela
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pixel Designer Maker by Gabriel J Santos")

    return screen, screen_width, screen_height

def get_colors():
    # Defina a cor do quadrado (R, G, B)
    test_color = (200, 200, 200)  # Cinza
    background_color = (0, 0, 0)  # Preto
    background_color_boxes = (150, 150, 150)  
    subtitle_color = (200,200,200)

    return test_color, background_color, background_color_boxes, subtitle_color
