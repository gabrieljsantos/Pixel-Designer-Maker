import pygame
import sys
import os
import random
from Setup_Screen import setup_screen, get_colors

# Configurações iniciais
screen, screen_width, screen_height = setup_screen()
test_color, background_color,background_color_boxes = get_colors()

# Diretório para salvar objetos
os.makedirs('PDM Objects', exist_ok=True)

# Inicializar matrizes
### Cores
colors_1bit = [("null"),(230,211,135)]
colors_2bit = [(0,0,0),(230,111,235),(130,211,135),(130,211,35)]
colors_RGB = [[0] * 10 for _ in range(10)]
TypeData = "2bit"
palette = []
### 
current_status = "main"
empty_design = [[0] * 13 for _ in range(13)]
created_design = [[0] * 13 for _ in range(13)]
created_design_text = [['0'] * 13 for _ in range(13)]
last_button_pressed_state = False


def write_design(screen, test_color, created_design, created_design_text, last_button_pressed_state):
    pos_text_x = 810
    pos_text_y = 20
    font = pygame.font.Font(None, 40)
    write_design_text = font.render("Write_Design", True, test_color)
    screen.blit(write_design_text, (pos_text_x, pos_text_y))

    if pygame.mouse.get_pressed()[0] == False:
        last_button_pressed_state = False
    position_mouse = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0] and not last_button_pressed_state:
        if pos_text_x <= position_mouse[0] <= pos_text_x + write_design_text.get_width() and pos_text_y <= position_mouse[1] <= pos_text_y + write_design_text.get_height():
            id_file = str(random.randint(1000, 10000))
            filepath = os.path.join('PDM Objects', f'object_{id_file}.pdm')
            for i in range(len(created_design[0])):
                for j in range(len(created_design)):
                    created_design_text[j][i] = str(int(created_design[i][j]))  # Converte para '0' ou '1'
            with open(filepath, 'w') as f:  # Abre o arquivo em modo texto ('w')
                for row in created_design_text:
                    f.write('(' + ', '.join(row) + '),\n')
            last_button_pressed_state = True
    return last_button_pressed_state

def color_management_button(screen,TypeData,last_button_pressed_state):
    global colors_1bit, colors_2bit, colors_RGB, background_color_boxes, current_status
    pos_text_x = 810
    pos_text_y = 60
    color_text = (200,200,200)
    size_font = 20
    spacing = 5
    font = pygame.font.Font(None, size_font)
    size_background_boxes_x = 150
    size_background_boxes_y = 105
    if TypeData == "2bit":
        size_color_box_x = (size_background_boxes_x - (5*spacing)) / len(colors_2bit)
        size_color_box_y = (size_background_boxes_y - (2*spacing) - size_font) / 1
        pygame.draw.rect(screen, background_color_boxes, (pos_text_x, pos_text_y, size_background_boxes_x, size_background_boxes_y))
        color_n = 0  # Inicializa o deslocamento horizontal
        for color in colors_2bit:
            pygame.draw.rect(screen, color, (pos_text_x + ((color_n+1) * spacing) + (color_n * size_color_box_x), pos_text_y + size_font + (spacing), size_color_box_x, size_color_box_y))
            color_n += 1  # Ajuste de espaço entre os quadrados (30px de largura + 5px de espaço)
    Color_Management_text = font.render("Color Management", True, color_text)
    screen.blit(Color_Management_text, (pos_text_x+ spacing, pos_text_y+ spacing))

    if pygame.mouse.get_pressed()[0] == False:
        last_button_pressed_state = False
    position_mouse = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0] and not last_button_pressed_state:
        if pos_text_x <= position_mouse[0] <= pos_text_x + Color_Management_text.get_width() and pos_text_y <= position_mouse[1] <= pos_text_y + Color_Management_text.get_height():
            last_button_pressed_state = True
            current_status = "color_management"
    return last_button_pressed_state

def draw_color_management(screen,TypeData,palette,last_button_pressed_state):
    global colors_1bit, colors_2bit, colors_RGB, background_color_boxes
    if TypeData == "2bit":
        pygame.draw.rect(screen, background_color_boxes, (23, 32, 123, 22))


def grid_pdm(screen, test_color):
    size_pixel = screen.get_height() // 13
    for i in range(13):
        for j in range(13):
            posx = i * size_pixel
            posy = j * size_pixel
            pygame.draw.rect(screen, test_color, (posx, posy, size_pixel, size_pixel), 1)

def selecionar(screen, test_color, created_design):
    size_pixel = screen.get_height() // 13
    position = pygame.mouse.get_pos()
    selecion_x = position[0] // size_pixel
    selecion_y = position[1] // size_pixel
    
    if selecion_x <= 12 and pygame.mouse.get_focused() and position[0] <= screen.get_height():
        pygame.draw.rect(screen, test_color, (selecion_x * size_pixel, selecion_y * size_pixel, size_pixel, size_pixel))
        return selecion_x, selecion_y
    return None, None

def paint(created_design):
    size_pixel = screen.get_height() // 13
    position = pygame.mouse.get_pos()
    alvo_x = position[0] // size_pixel
    alvo_y = position[1] // size_pixel

    if pygame.mouse.get_pressed()[0] and 0 <= alvo_y < len(created_design) and 0 <= alvo_x < len(created_design[0]):
        created_design[alvo_x][alvo_y] = True
    elif pygame.mouse.get_pressed()[2] and 0 <= alvo_y < len(created_design) and 0 <= alvo_x < len(created_design[0]):
        created_design[alvo_x][alvo_y] = False

def draw_paint(screen, test_color, created_design):
    size_pixel = screen.get_height() // 13
    for i in range(len(created_design[0])):
        for j in range(len(created_design)):
            if created_design[i][j]:
                pygame.draw.rect(screen, test_color, (i * size_pixel, j * size_pixel, size_pixel, size_pixel))

def main():
    global last_button_pressed_state
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(background_color)
        if current_status == "main":
            grid_pdm(screen, test_color)
            selecionar(screen, test_color, created_design)
            paint(created_design)
            draw_paint(screen, test_color, created_design)
            
            last_button_pressed_state = write_design(screen, test_color, created_design, created_design_text, last_button_pressed_state)
            last_button_pressed_state = color_management_button(screen,TypeData,last_button_pressed_state)
        if current_status == "color_management":
            last_button_pressed_state = draw_color_management(screen,TypeData,palette,last_button_pressed_state)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
main()
