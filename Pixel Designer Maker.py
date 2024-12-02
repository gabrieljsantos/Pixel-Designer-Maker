import pygame
import sys
import os
import random
from Setup_Screen import setup_screen, get_colors

# Configurações iniciais
screen, screen_width, screen_height = setup_screen()
test_color, background_color,background_color_boxes, subtitle_color = get_colors()

# Diretório para salvar objetos
os.makedirs('PDM Objects', exist_ok=True)

# Inicializar matrizes
### Cores
colors_1bit = [(0,0,0),(230,211,135)]
colors_2bit = [(0,0,0),(230,111,235),(130,211,135),(130,211,35)]
colors_RGB = [[0] * 10 for _ in range(10)]
TypeData = "1bit"
palette = [(0,0,0),(230,111,135)]
for _ in range(len(palette), 10):
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    palette.append(random_color)

chosen_color = 1
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

def color_management_button(screen,x0,y0):

    global subtitle_color, colors_1bit, colors_2bit, colors_RGB, background_color_boxes, TypeData
    
    size_font = 20
    spacing = 5
    font = pygame.font.Font(None, size_font)
    size_background_boxes_x = 150
    size_background_boxes_y = 105

    pygame.draw.rect(screen, background_color_boxes, (x0, y0, size_background_boxes_x, size_background_boxes_y))
    Color_Management_text = font.render("Color Management", True, subtitle_color)
    screen.blit(Color_Management_text, (x0 + spacing, y0 + spacing))

    if TypeData == "1bit":
        size_color_box_x = (size_background_boxes_x - (3*spacing)) / len(colors_1bit)
        size_color_box_y = (size_background_boxes_y - (2*spacing) - size_font) / 1
        button(x0, y0, size_background_boxes_x, size_background_boxes_y,"color_management")
        color_n = 0  # Inicializa o deslocamento horizontal
        for color in colors_1bit:
            pygame.draw.rect(screen, color, (x0 + ((color_n+1) * spacing) + (color_n * size_color_box_x), y0 + size_font + (spacing), size_color_box_x, size_color_box_y))
            color_n += 1  # Ajuste de espaço entre os quadrados (30px de largura + 5px de espaço)
   
    if TypeData == "2bit":
        size_color_box_x = (size_background_boxes_x - (5*spacing)) / len(colors_2bit)
        size_color_box_y = (size_background_boxes_y - (2*spacing) - size_font) / 1
        button(x0, y0, size_background_boxes_x, size_background_boxes_y,"color_management")
        color_n = 0  # Inicializa o deslocamento horizontal
        for color in colors_2bit:
            pygame.draw.rect(screen, color, (x0 + ((color_n+1) * spacing) + (color_n * size_color_box_x), y0 + size_font + (spacing), size_color_box_x, size_color_box_y))
            color_n += 1  # Ajuste de espaço entre os quadrados (30px de largura + 5px de espaço)
    


def button(x0,y0,x1,y1,invocation):
    global last_button_pressed_state, current_status
    if pygame.mouse.get_pressed()[0] == False:
        last_button_pressed_state = False
    position_mouse = pygame.mouse.get_pos()
    
    if pygame.mouse.get_pressed()[0] and not last_button_pressed_state:
        if x0 <= position_mouse[0] <= x0 + x1 and y0 <= position_mouse[1] <= y0 + y1:
            last_button_pressed_state = True
            current_status = invocation

def draw_color_management(screen):
    global current_status, TypeData, colors_1bit, colors_2bit, colors_RGB, palette, chosen_color 
    
    # Definindo a largura e altura do gradiente
    gradient_width = 255 * 5  # 255 para R, rosa, G, B
    gradient_height = 100  # Altura fixa para o gradiente
    start_x = 100  # Posição inicial do gradiente no eixo X
    start_y = 100  # Posição inicial do gradiente no eixo Y

    # Variáveis de cor (R, G, B)
    R, G, B = 0, 0, 0

    # Desenha o gradiente RGB com transições entre vermelho, rosa, verde e azul
    for x in range(gradient_width):
        if x <= 255:  # Gradiente de vermelho para rosa
            R = 255  # Vermelho fixo
            G = x    # Verde aumenta de 0 até 255
            B = 0    # Azul permanece 0
        elif 255 < x <= 255 * 2:  # Gradiente de rosa (mistura de vermelho e azul)
            R = 255 - (x - 255)  # O vermelho diminui, criando o rosa
            G = 255              # Verde fixo em 255
            B = x - 255          # Azul aumenta de 0 até 255
        elif 255 * 2 < x <= 255 * 3:  # Gradiente de verde
            R = 0                # Vermelho é 0
            G = 255 - (x - 255 * 2)  # Verde diminui de 255 até 0
            B = 255              # Azul fixo em 255
        elif 255 * 3 < x <= 255 * 4:  # Gradiente de verde
            R = 0 + (x - 255 * 3)                # Vermelho é 0
            G = 0 #
            B = 255           # Azul fixo em 255
        else:  # Gradiente de azul
            R = 255                # Vermelho continua 0
            G = 0 #              # Verde continua 0
            B = 255 - (x - 255 * 4)  # Azul diminui de 255 até 0

        # Desenha o pixel do gradiente
        pygame.draw.rect(screen, (R, G, B), (start_x + (int(0 + x/2.5)), start_y, 1, gradient_height))
    
    color_tmtg = palette[chosen_color] #color_to_make_the_gradient
    #print(color_tmtg)
    for pixel_color_x in range(500):
        for pixel_color_y in range(500):
            R_pixel = int(color_tmtg[0] + ((255 - color_tmtg[0]) * (pixel_color_x/500)) - ((color_tmtg[0]) * (pixel_color_y/500))) 
            G_pixel = int(color_tmtg[1] + ((255 - color_tmtg[1]) * (pixel_color_x/500)) - ((color_tmtg[1]) * (pixel_color_y/500))) 
            B_pixel = int(color_tmtg[2] + ((255 - color_tmtg[2]) * (pixel_color_x/500)) - ((color_tmtg[2]) * (pixel_color_y/500))) 
            pixel_color = ( R_pixel , G_pixel , B_pixel )

            screen.set_at((100 + pixel_color_x, 250 + pixel_color_y), pixel_color)

    color_n = 0
    for color in palette:
        x_position = 800 + (color_n % 2) * (50 + 5)
        y_position = 100 + ((color_n - (color_n % 2)) / 2) * (50 + 5)
        pygame.draw.rect(screen, color, (x_position, y_position, 50, 50))
        color_n += 1





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
            
            write_design(screen, test_color, created_design, created_design_text, last_button_pressed_state)
            color_management_button(screen, 810, 60)
        if current_status == "color_management":
            draw_color_management(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
main()
