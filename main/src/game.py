import sys
import pygame
from constants import *
from graph import Graph
from shapes import POSSIBLE_SHAPES

# Reinicialização
pygame.init()

# Janela [1]
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("COL")

# Logo
try:
    logo_img = pygame.image.load(r'C:\Users\conta\Documents\Programacao\Outros\TCC\main\assets\col-logo.png').convert_alpha()
    logo_img = pygame.transform.smoothscale(logo_img, (1600, 900))     # Redimensionar a imagem
except pygame.error:
    logo_img = None  # se falhar ao carregar, seguimos sem imagem

# Estado do menu
temporary_number_of_players = 2     # valor temporário antes de confirmar no botão
num_players = 2
max_players = 3
min_players = 2

# Nomes personalizáveis (pode ser alterado antes de iniciar)
player_names = ['Jogador 1', 'Jogador 2', 'Jogador 3']

# Retângulos das setas
LEFT_ARROW  = pygame.Rect(SCREEN_WIDTH // 2 - 50, 200, 30, 30)
RIGHT_ARROW = pygame.Rect(SCREEN_WIDTH // 2 + 50, 200, 30, 30)
PLAY_BUTTON = pygame.Rect((SCREEN_WIDTH // 2 - 100, 450), (200, 60))

# Menu inicial
def draw_menu():
    SCREEN.fill(BG_COLOR)

    # Desenhar logo, se carregado
    if logo_img:
        logo_rect = logo_img.get_rect(center=(SCREEN_WIDTH // 2, 140))
        SCREEN.blit(logo_img, logo_rect)

    # Título
    title_surf = FONT_MEDIUM.render("Número de jogadores", True, TEXT_COLOR)  # Posicionamento vertical do texto "nº de jogadores"
    title_pos = title_surf.get_rect(center=(SCREEN_WIDTH//2, 105))
    SCREEN.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    # Setas e número atual
    arrows_y = title_pos.bottom + 210
    LEFT_ARROW.topleft = (SCREEN_WIDTH // 2 - 100, arrows_y)
    RIGHT_ARROW.topleft = (SCREEN_WIDTH // 2 + 60, arrows_y)

    # Seta para esquerda
    left_color = BUTTON_HOVER if LEFT_ARROW.collidepoint(pygame.mouse.get_pos()) else TEXT_COLOR
    pygame.draw.polygon(SCREEN, left_color, [
        (LEFT_ARROW.right, LEFT_ARROW.top),
        (LEFT_ARROW.left, LEFT_ARROW.centery),
        (LEFT_ARROW.right, LEFT_ARROW.bottom),
    ])
    # Seta para direita
    right_color = BUTTON_HOVER if RIGHT_ARROW.collidepoint(pygame.mouse.get_pos()) else TEXT_COLOR
    pygame.draw.polygon(SCREEN, right_color, [
        (RIGHT_ARROW.left, RIGHT_ARROW.top),
        (RIGHT_ARROW.right, RIGHT_ARROW.centery),
        (RIGHT_ARROW.left, RIGHT_ARROW.bottom),
    ])

    # Número (centro entre as setas)
    num_surf = FONT_MEDIUM.render(str(temporary_number_of_players), True, TEXT_COLOR)
    num_pos = num_surf.get_rect(center=(SCREEN_WIDTH // 2, arrows_y + LEFT_ARROW.height // 2))
    SCREEN.blit(num_surf, num_pos)

    # Lista de jogadores em linha
    count = temporary_number_of_players
    spacing = 220
    total_width = (count - 1) * spacing
    start_x = SCREEN_WIDTH//2 - total_width//2
    y_text = 400  # Posicionamento vertical da lista de jogadores

    for i in range(count):
        x = start_x + i * spacing

        # Nome editável
        name_surf = FONT_MEDIUM.render(player_names[i], True, TEXT_COLOR)
        SCREEN.blit(name_surf, name_surf.get_rect(center=(x, y_text)))

        # Quadrado de cor ao lado
        square = pygame.Rect(x + name_surf.get_width()//2 + 10, y_text - 15, 30, 30)
        pygame.draw.rect(SCREEN, PLAYER_COLORS[i], square)
        pygame.draw.rect(SCREEN, TEXT_COLOR, square, 2)

    # Botão “JOGAR”
    mouse = pygame.mouse.get_pos()
    btn_color = BUTTON_HOVER if PLAY_BUTTON.collidepoint(mouse) else BUTTON_COLOR
    pygame.draw.rect(SCREEN, btn_color, PLAY_BUTTON, border_radius=8)
    play_surf = FONT_MEDIUM.render("JOGAR", True, TEXT_COLOR)
    SCREEN.blit(play_surf, play_surf.get_rect(center=PLAY_BUTTON.center))


# Tela de jogo
def play():
    # Limpa o menu
    SCREEN.fill(BG_COLOR)

    # Constroi o grafo a partir das shapes
    shapes = POSSIBLE_SHAPES
    graph  = Graph(shapes, min_face_area=100)

    # Desenha arestas
    for v1, v2 in graph.edges:
        # Se graph.edges armazenar pares de índices em vez de tuplas de coordenadas,
        # você deve buscar as coords em graph.vertices:
        #   p1 = graph.vertices[v1]; p2 = graph.vertices[v2]
        pygame.draw.line(SCREEN, SHAPES_COLOR, v1, v2, 2)

    # (Opcional) Desenha faces por cima, se quiser pintar as faces:
    # for face in graph.faces:
    #     pygame.draw.polygon(screen, face_color, face)

    # Atualiza a tela
    pygame.display.update()

# Loop de jogo [2]
running = True
gameWasStarted = False

while running:

    # Manipulador de eventos [3]
    for event in pygame.event.get():

        # Sair do jogo
        if event.type == pygame.QUIT:
            running = False

        # Clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if LEFT_ARROW.collidepoint(event.pos):
                temporary_number_of_players = max(min_players, temporary_number_of_players - 1)
            if RIGHT_ARROW.collidepoint(event.pos):
                temporary_number_of_players = min(max_players, temporary_number_of_players + 1)
            if PLAY_BUTTON.collidepoint(event.pos):
                num_players = temporary_number_of_players  # confirma seleção
                print(f"Iniciando jogo com {num_players} jogadores!")
                gameWasStarted = True

    if not gameWasStarted: draw_menu()
    else: play()

    # Atualizar tela a cada frame
    pygame.display.update()

# Encerrar pygame
pygame.quit()
sys.exit()
