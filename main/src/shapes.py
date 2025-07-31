import random
from constants import *

# Parâmetros mínimos
MIN_SIZE = 90
MAX_SIZE_W = SCREEN_WIDTH // 3
MAX_SIZE_H = SCREEN_HEIGHT // 3

# Geradores de formas aleatórias dentro dos limites da tela

def random_rect():
    w = random.randint(MIN_SIZE, MAX_SIZE_W)
    h = random.randint(MIN_SIZE, MAX_SIZE_H)
    x = random.randint(0, SCREEN_WIDTH - w)
    y = random.randint(0, SCREEN_HEIGHT - h)
    return 'rect', pygame.Rect(x, y, w, h)


def random_circle():
    radius = random.randint(MIN_SIZE // 2, min(MIN_SIZE, MAX_SIZE_W, MAX_SIZE_H))
    x = random.randint(radius, SCREEN_WIDTH - radius)
    y = random.randint(radius, SCREEN_HEIGHT - radius)
    return 'circle', (x, y, radius)  # center_x, center_y, radius


def random_ellipse():
    w = random.randint(MIN_SIZE, MAX_SIZE_W)
    h = random.randint(MIN_SIZE, MAX_SIZE_H)
    x = random.randint(0, SCREEN_WIDTH - w)
    y = random.randint(0, SCREEN_HEIGHT - h)
    return 'ellipse', pygame.Rect(x, y, w, h)


def random_triangle():
    # Triângulo gerado dentro de um retângulo de delimitação
    w = random.randint(MIN_SIZE, MAX_SIZE_W)
    h = random.randint(MIN_SIZE, MAX_SIZE_H)
    x0 = random.randint(0, SCREEN_WIDTH - w)
    y0 = random.randint(0, SCREEN_HEIGHT - h)
    # vértices relativos
    p1 = (x0, y0 + h)
    p2 = (x0 + w // 2, y0)
    p3 = (x0 + w, y0 + h)
    return 'polygon', [p1, p2, p3]


def random_polygon(sides=5):
    # Polígono convexo regular aproximado
    import math
    cx = random.randint(MAX_SIZE_W, SCREEN_WIDTH - MAX_SIZE_W)
    cy = random.randint(MAX_SIZE_H, SCREEN_HEIGHT - MAX_SIZE_H)
    radius = random.randint(MIN_SIZE, min(MAX_SIZE_W, MAX_SIZE_H))
    verts = []
    for i in range(sides):
        theta = 2 * math.pi * i / sides
        x = int(cx + radius * math.cos(theta))
        y = int(cy + radius * math.sin(theta))
        verts.append((x, y))
    return 'polygon', verts

# Lista de possíveis formas para usar no jogo
POSSIBLE_SHAPES = [
    random_rect(),
    random_circle(),
    random_ellipse(),
    random_triangle(),
    random_polygon(sides=5),
    random_polygon(sides=6),
    random_polygon(sides=7),
    random_polygon(sides=4),
    random_polygon(sides=6)
]

