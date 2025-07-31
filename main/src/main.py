import sys
import pygame
from constants import *
from graph import Graph
from shapes import POSSIBLE_SHAPES
from game import play
from menu import draw_menu

# Reinicialização
pygame.init()

# Janela [1]
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("COL")

# Loop de jogo [2]
running = True
game_started = False

# Constroi o grafo a partir das shapes
shapes = POSSIBLE_SHAPES
graph: Graph = None

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
                game_started = True
                graph = Graph(shapes, area_minima_face=100)

    if not game_started:
        draw_menu(SCREEN)
        pygame.display.update()                 # Atualizar tela a cada frame
    else:
        play(SCREEN, num_players, graph)

# Encerrar pygame
pygame.quit()
sys.exit()
