import sys
import pygame
from constants import *
from graph import Graph
from shapes import POSSIBLE_SHAPES

# Tela de jogo
def play(screen, number_of_players, graph: Graph):
    # Limpa o menu
    screen.fill(BG_COLOR)

    # Desenha arestas
    for v1, v2 in graph.arestas:
        pygame.draw.line(screen, SHAPES_COLOR, v1, v2, 2)

    # Alterar cor da face por clique
    graph.desenhar(screen, cor_arestas=SHAPES_COLOR, largura_arestas=1)

    # Detectar clique em face, alterar cor da face de acordo com a vez de cada jogador


    # Atualiza a tela
    pygame.display.update()


