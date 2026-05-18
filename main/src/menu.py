import pygame
import constants

# Logo
try:
    logo_img = pygame.image.load(r'C:/Users/conta/Documents/Programacao/Outros/TCC/main/asset/col-logo.png')
    logo_img = pygame.transform.smoothscale(logo_img, (600, 370))     # Redimensionar a imagem
except pygame.error:
    logo_img = None  # se falhar ao carregar, seguimos sem imagem

# Menu inicial
def draw_menu(screen: pygame.Surface, events: list[pygame.event.Event]):
    # no local temp, use constants.temporary_number_of_players

    # Processar eventos
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clique esquerdo
                mouse_pos = event.pos

                # Verificar clique na seta esquerda
                if constants.LEFT_ARROW.collidepoint(mouse_pos):
                    if constants.temporary_number_of_players > constants.min_players:
                        constants.temporary_number_of_players -= 1
                    print(f"número de jogadores: {constants.temporary_number_of_players}")

                # Verificar clique na seta direita
                elif constants.RIGHT_ARROW.collidepoint(mouse_pos):
                    if constants.temporary_number_of_players < constants.max_players:
                        constants.temporary_number_of_players += 1
                    print(f"número de jogadores: {constants.temporary_number_of_players}")

                # Verificar clique no botão JOGAR
                elif constants.PLAY_BUTTON.collidepoint(mouse_pos):
                    print(f"Iniciando jogo com {constants.temporary_number_of_players} jogadores!")
                    return "start_game"  # Retorna sinal para iniciar o jogo

    screen.fill(constants.BG_COLOR)

    # Desenhar logo, se carregado
    if logo_img:
        logo_rect = logo_img.get_rect(center=(constants.SCREEN_WIDTH // 2, 140))
        screen.blit(logo_img, logo_rect)

    # Título
    title_surf = constants.FONT_MEDIUM.render("Número de jogadores", True, constants.TEXT_COLOR)  # Posicionamento vertical do texto "nº de jogadores"
    title_pos = title_surf.get_rect(center=(constants.SCREEN_WIDTH//2, 115))
    screen.blit(title_surf, title_surf.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)))

    # Setas e número atual
    arrows_y = title_pos.bottom + 230
    constants.LEFT_ARROW.topleft = (constants.SCREEN_WIDTH // 2 - 100, arrows_y)
    constants.RIGHT_ARROW.topleft = (constants.SCREEN_WIDTH // 2 + 60, arrows_y)

    # Seta para esquerda
    left_color = constants.BUTTON_HOVER if constants.LEFT_ARROW.collidepoint(pygame.mouse.get_pos()) else constants.TEXT_COLOR
    pygame.draw.polygon(screen, left_color, [
        (constants.LEFT_ARROW.right, constants.LEFT_ARROW.top),
        (constants.LEFT_ARROW.left, constants.LEFT_ARROW.centery),
        (constants.LEFT_ARROW.right, constants.LEFT_ARROW.bottom),
    ])
    # Seta para direita
    right_color = constants.BUTTON_HOVER if constants.RIGHT_ARROW.collidepoint(pygame.mouse.get_pos()) else constants.TEXT_COLOR
    pygame.draw.polygon(screen, right_color, [
        (constants.RIGHT_ARROW.left, constants.RIGHT_ARROW.top),
        (constants.RIGHT_ARROW.right, constants.RIGHT_ARROW.centery),
        (constants.RIGHT_ARROW.left, constants.RIGHT_ARROW.bottom),
    ])

    # Número (centro entre as setas)
    num_surf = constants.FONT_MEDIUM.render(str(constants.temporary_number_of_players), True, constants.TEXT_COLOR)
    num_pos = num_surf.get_rect(center=(constants.SCREEN_WIDTH // 2, arrows_y + constants.LEFT_ARROW.height // 2))
    screen.blit(num_surf, num_pos)

    # Lista de jogadores em linha
    count = constants.temporary_number_of_players
    spacing = 75
    total_width = (count - 1) * spacing
    start_x = constants.SCREEN_WIDTH//2 - total_width//2
    y_text = 420  # Posicionamento vertical da lista de jogadores

    for i in range(constants.temporary_number_of_players):
        dimension_square = 30
        x = start_x + i * spacing

        # Nomes
        name_surf = constants.FONT_SMALL.render(constants.player_names[i], True, constants.TEXT_COLOR)
        screen.blit(name_surf, name_surf.get_rect(center=(x, y_text)))

        # Quadrado de cor ao lado
        square = pygame.Rect(x + name_surf.get_width()//2 - name_surf.get_width() + 15, y_text + dimension_square//2, dimension_square, dimension_square)
        pygame.draw.rect(screen, constants.PLAYER_COLORS[i], square)
        pygame.draw.rect(screen, constants.TEXT_COLOR, square, 2)

    # Botão "JOGAR"
    mouse = pygame.mouse.get_pos()
    btn_color = constants.BUTTON_HOVER if constants.PLAY_BUTTON.collidepoint(mouse) else constants.BUTTON_COLOR
    pygame.draw.rect(screen, btn_color, constants.PLAY_BUTTON, border_radius=8)
    play_surf = constants.FONT_MEDIUM.render("JOGAR", True, constants.TEXT_COLOR)
    screen.blit(play_surf, play_surf.get_rect(center=constants.PLAY_BUTTON.center))

    return None  # Retorna None quando não há ação especial
