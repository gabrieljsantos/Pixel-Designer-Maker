import pygame
import sys
import os
import random

from Setup_Screen import setup_screen, get_colors

# Configurações iniciais
screen, screen_width, screen_height = setup_screen()
test_color, background_color, background_color_2 ,background_color_boxes, subtitle_color = get_colors()

# Diretório para salvar objetos
os.makedirs('PDM Objects', exist_ok=True)

# Inicializar matrizes
### Cores
s_RGB_g = []
TypeData = "1bit"
palette = [(0,0,0)]
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
pos_slider_rgb = (0,0,255,100)
pos_slider_white = (0,0,255,100)
pos_slider_black = (0,0,255,100)

def generate_segmented_RGB_gradient():
    global s_RGB_g
    # Variáveis de cor (R, G, B)
    R, G, B = 0, 0, 0
    for x in range(255*5):
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
        s_RGB_g.append((R,G,B))
    return s_RGB_g


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

def back_button(screen, x0, y0, x1, y1,size_font, page_to_return):
    spacing = 5
    pygame.draw.rect(screen, background_color_boxes, (x0, y0, x1, y1))
    font = pygame.font.Font(None, size_font)
    Back_text = font.render("Back", True, subtitle_color)
    screen.blit(Back_text, (x0 + spacing, y0 + spacing))
    button(x0, y0, x1, y1, page_to_return)
def generate_HSB_color(pos_slider_rgb_x,pos_slider_lumin_y,gradient_xy_chosen):
    global s_RGB_g
    return s_RGB_g[pos_slider_rgb_x]

def HSB_gradient(color_of_s_RGB_s, black , white):
    gradient_to_white = []
    total_gradient= [[] for _ in range(50)]

    difference_to_white = (
        white*255/100 - color_of_s_RGB_s[0],
        white*255/100 - color_of_s_RGB_s[1],
        white*255/100 - color_of_s_RGB_s[2]
    )
    # Cria o gradiente HSB
    for n in range(50):
        gradient_to_white.append((
            color_of_s_RGB_s[0] + int(n * difference_to_white[0] / 50),
            color_of_s_RGB_s[1] + int(n * difference_to_white[1] / 50),
            color_of_s_RGB_s[2] + int(n * difference_to_white[2] / 50)
        ))
        for z in range(50):
            total_gradient[n].append((
                gradient_to_white[n][0] - int( (z * gradient_to_white[n][0] / 50) / (100/black) ),
                gradient_to_white[n][1] - int( (z * gradient_to_white[n][1] / 50) / (100/black) ),
                gradient_to_white[n][2] - int( (z * gradient_to_white[n][2] / 50) / (100/black) )
            ))
    return total_gradient

def draw_HSB_gradient(color_of_s_RGB_s, black , white ,screen):

    total_gradient = HSB_gradient(color_of_s_RGB_s, black , white)

    
    for m in range(50):
        for l in range(50):
            try:
                pygame.draw.rect(
                    screen, total_gradient[m][l],
                    (10 + 10 * m, 10 + 10 * l, 10, 10)
                    )
            except :
                x=1
                #print("error color:")
                #print(total_gradient[m][l])


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
        size_color_box_x = (size_background_boxes_x - (3*spacing)) / 2
        size_color_box_y = (size_background_boxes_y - (2*spacing) - size_font) / 1
        button(x0, y0, size_background_boxes_x, size_background_boxes_y,"color_management")
        color_n = 0  # Inicializa o deslocamento horizontal
        for x in range(2):
            pygame.draw.rect(screen, palette[x], (x0 + ((color_n+1) * spacing) + (color_n * size_color_box_x), y0 + size_font + (spacing), size_color_box_x, size_color_box_y))
            color_n += 1  # Ajuste de espaço entre os quadrados (30px de largura + 5px de espaço)
   
    if TypeData == "2bit":
        size_color_box_x = (size_background_boxes_x - (5*spacing)) / 4
        size_color_box_y = (size_background_boxes_y - (2*spacing) - size_font) / 1
        button(x0, y0, size_background_boxes_x, size_background_boxes_y,"color_management")
        color_n = 0  # Inicializa o deslocamento horizontal
        for x in range(4):
            pygame.draw.rect(screen, palette[x], (x0 + ((color_n+1) * spacing) + (color_n * size_color_box_x), y0 + size_font + (spacing), size_color_box_x, size_color_box_y))
            color_n += 1  # Ajuste de espaço entre os quadrados (30px de largura + 5px de espaço)
    
def Click_Slider(x0,y0,x1,y1,scale,default):
    position_mouse = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if x0 <= position_mouse[0] <= x0 + x1 and y0 <= position_mouse[1] <= y0 + y1:
            return int((position_mouse[0] - x0) * scale / x1), int ((position_mouse[1] - y0) * scale / y1) , position_mouse[0] - x0, position_mouse[1] - y0
    return default

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
    global current_status, TypeData, colors_1bit, colors_2bit, colors_RGB, palette, chosen_color, Seg_RGB_gradt, pos_slider_rgb, s_RGB_g,pos_slider_white,pos_slider_black
    
    # Definindo a largura e altura do gradiente
    gradient_width = 500
    gradient_height = 50  # Altura fixa para o gradiente
    start_x = 10  # Posição inicial do gradiente no eixo X
    start_y = 520  # Posição inicial do gradiente no eixo Y
    color_n = 0
    for color in Seg_RGB_gradt:
        pygame.draw.rect(
            screen,
            color,
            (
                int(start_x + color_n * (gradient_width / len(Seg_RGB_gradt))),  # Posição X
                start_y,                                              # Posição Y
                1,                                                   # Largura do retângulo
                gradient_height                                      # Altura do retângulo
            )
        )
        color_n += 1
    
    pos_slider_rgb = Click_Slider(start_x,start_y,gradient_width,gradient_height,len(Seg_RGB_gradt),pos_slider_rgb)
    pos_slider_rgb_x = pos_slider_rgb[0]

    pos_slider_black = Click_Slider(520,10,50,500,100,pos_slider_black)
    black = 100 - pos_slider_black[1]
    pos_slider_white = Click_Slider(580,10,50,500,100,pos_slider_white)
    white = 100 - pos_slider_white[1]

    pos_slider_lumin_y = 500
    gradient_xy_chosen = (0,0)
    color_of_s_RGB_s = s_RGB_g[pos_slider_rgb_x]

    palette[chosen_color] = generate_HSB_color(pos_slider_rgb[0] ,pos_slider_lumin_y,gradient_xy_chosen)


 
    pygame.draw.rect(screen, (0,0,0), ( 520 , 10,gradient_height,gradient_width))
    pygame.draw.rect(screen, (255,255,255), ( 580 , 10,gradient_height,gradient_width))
    
    pygame.draw.rect(screen, color, (pos_slider_rgb[2] , start_y,4,gradient_height))
    pygame.draw.rect(screen, color, ( 520 , pos_slider_black[3],gradient_height,4))
    pygame.draw.rect(screen, color, ( 580 , pos_slider_white[3],gradient_height,4))
    

    draw_HSB_gradient(color_of_s_RGB_s, black , white ,screen)
    color_n = 0
    for color in palette:
        x_position = 640 + (color_n % 2) * (50 + 5)
        y_position = 10 + ((color_n - (color_n % 2)) / 2) * (50 + 5)
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
    global TypeData, palette
    size_pixel = screen.get_height() // 13
    if TypeData == "1bit":
        for i in range(len(created_design[0])):
            for j in range(len(created_design)):
                if created_design[i][j]:
                    pygame.draw.rect(screen, palette[1], (i * size_pixel, j * size_pixel, size_pixel, size_pixel))
    if TypeData == "2bit":
        for i in range(len(created_design[0])):
            for j in range(len(created_design)):
                pygame.draw.rect(screen, palette[int(created_design[i][j], 2)], (i * size_pixel, j * size_pixel, size_pixel, size_pixel))


Seg_RGB_gradt = generate_segmented_RGB_gradient()

def main():
    global last_button_pressed_state
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        if current_status == "main":
            screen.fill(background_color)
            selecionar(screen, test_color, created_design)
            paint(created_design)
            draw_paint(screen, test_color, created_design)
            grid_pdm(screen, test_color)
            
            write_design(screen, test_color, created_design, created_design_text, last_button_pressed_state)
            color_management_button(screen, 810, 60)
            
        if current_status == "color_management":
            screen.fill(background_color_2)
            draw_color_management(screen)
            back_button(screen, 10, 600, 95, 40, 50, "main")

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
main()
