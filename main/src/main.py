import sys
import pygame
from constants import *
from graph import Graph
import shapes as shapes_module
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

shapes = None  # receberá lista de shapes da partida
graph: Graph = None

while running:
    events = pygame.event.get()

    if not game_started:
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BUTTON.collidepoint(event.pos):
                    print(f"Iniciando jogo com 2 jogadores!")
                    # gera novas shapes aleatórias a cada partida
                    shapes = shapes_module.generate_shapes()
                    graph = Graph(shapes, area_minima_face=100)
                    game_started = True
        draw_menu(SCREEN)
        pygame.display.update()
    else:
        cont = play(SCREEN, graph, events)
        if not cont:
            game_started = False

# Encerrar pygame
pygame.quit()
sys.exit()
