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
    events = pygame.event.get()

    if not game_started:
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BUTTON.collidepoint(event.pos):
                    print(f"Iniciando jogo com 2 jogadores!")
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
