import pygame
from constants import *

# Logo
try:
    logo_img = pygame.image.load(r'C:\Users\conta\Documents\Programacao\Outros\TCC\main\assets\col-logo.png').convert_alpha()
    logo_img = pygame.transform.smoothscale(logo_img, (1600, 900))     # Redimensionar a imagem
except pygame.error:
    logo_img = None  # se falhar ao carregar, seguimos sem imagem

# Menu inicial
def draw_menu(screen: pygame.Surface):
    screen.fill(BG_COLOR)

    # Desenhar logo, se carregado
    if logo_img:
        logo_rect = logo_img.get_rect(center=(SCREEN_WIDTH // 2, 140))
        screen.blit(logo_img, logo_rect)

    # Título
    title_surf = FONT_MEDIUM.render("Número de jogadores", True, TEXT_COLOR)  # Posicionamento vertical do texto "nº de jogadores"
    title_pos = title_surf.get_rect(center=(SCREEN_WIDTH//2, 105))
    screen.blit(title_surf, title_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    # Setas e número atual
    arrows_y = title_pos.bottom + 210
    LEFT_ARROW.topleft = (SCREEN_WIDTH // 2 - 100, arrows_y)
    RIGHT_ARROW.topleft = (SCREEN_WIDTH // 2 + 60, arrows_y)

    # Seta para esquerda
    left_color = BUTTON_HOVER if LEFT_ARROW.collidepoint(pygame.mouse.get_pos()) else TEXT_COLOR
    pygame.draw.polygon(screen, left_color, [
        (LEFT_ARROW.right, LEFT_ARROW.top),
        (LEFT_ARROW.left, LEFT_ARROW.centery),
        (LEFT_ARROW.right, LEFT_ARROW.bottom),
    ])
    # Seta para direita
    right_color = BUTTON_HOVER if RIGHT_ARROW.collidepoint(pygame.mouse.get_pos()) else TEXT_COLOR
    pygame.draw.polygon(screen, right_color, [
        (RIGHT_ARROW.left, RIGHT_ARROW.top),
        (RIGHT_ARROW.right, RIGHT_ARROW.centery),
        (RIGHT_ARROW.left, RIGHT_ARROW.bottom),
    ])

    # Número (centro entre as setas)
    num_surf = FONT_MEDIUM.render(str(temporary_number_of_players), True, TEXT_COLOR)
    num_pos = num_surf.get_rect(center=(SCREEN_WIDTH // 2, arrows_y + LEFT_ARROW.height // 2))
    screen.blit(num_surf, num_pos)

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
        screen.blit(name_surf, name_surf.get_rect(center=(x, y_text)))

        # Quadrado de cor ao lado
        square = pygame.Rect(x + name_surf.get_width()//2 + 10, y_text - 15, 30, 30)
        pygame.draw.rect(screen, PLAYER_COLORS[i], square)
        pygame.draw.rect(screen, TEXT_COLOR, square, 2)

    # Botão “JOGAR”
    mouse = pygame.mouse.get_pos()
    btn_color = BUTTON_HOVER if PLAY_BUTTON.collidepoint(mouse) else BUTTON_COLOR
    pygame.draw.rect(screen, btn_color, PLAY_BUTTON, border_radius=8)
    play_surf = FONT_MEDIUM.render("JOGAR", True, TEXT_COLOR)
    screen.blit(play_surf, play_surf.get_rect(center=PLAY_BUTTON.center))
