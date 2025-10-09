import pygame, constants
from textures import gradient_surface, stripe_texture


def create_player_textures(size=(100, 100)):
    """
    Cria texturas procedurais para cada jogador baseadas em suas cores.
    Retorna um dicionário {player_index: Surface}.
    """
    textures = {}

    # Jogador 0 (Vermelho) - Listras diagonais
    base_red = constants.PLAYER_COLORS[0]
    dark_red = pygame.Color(
        max(0, base_red.r - 40),
        max(0, base_red.g - 20),
        max(0, base_red.b - 20)
    )
    textures[0] = stripe_texture(
        size,
        base_red,
        dark_red,
        stripe_width=8,
        spacing=8,
        angle=45
    )

    # Jogador 1 (Verde) - Gradiente vertical
    base_green = constants.PLAYER_COLORS[1]
    light_green = pygame.Color(
        min(255, base_green.r + 30),
        min(255, base_green.g + 30),
        min(255, base_green.b + 30)
    )
    textures[1] = gradient_surface(
        size,
        base_green,
        light_green,
        vertical=True
    )

    # Jogador 2 (Azul) - Listras horizontais
    base_blue = constants.PLAYER_COLORS[2]
    dark_blue = pygame.Color(
        max(0, base_blue.r - 30),
        max(0, base_blue.g - 30),
        max(0, base_blue.b - 30)
    )
    textures[2] = stripe_texture(
        size,
        base_blue,
        dark_blue,
        stripe_width=6,
        spacing=6,
        angle=0
    )

    # Jogador 3 (Roxo) - Listras diagonais invertidas
    base_purple = constants.PLAYER_COLORS[3]
    light_purple = pygame.Color(
        min(255, base_purple.r + 25),
        min(255, base_purple.g + 25),
        min(255, base_purple.b + 25)
    )
    textures[3] = stripe_texture(
        size,
        base_purple,
        light_purple,
        stripe_width=7,
        spacing=7,
        angle=-45
    )

    # Jogador 4 (Amarelo) - Listras diagonais claras/escuras
    base_yellow = constants.PLAYER_COLORS[4]
    dark_yellow = pygame.Color(
        max(0, base_yellow.r - 50),
        max(0, base_yellow.g - 50),
        max(0, base_yellow.b - 50)
    )
    textures[4] = stripe_texture(
        size,
        base_yellow,
        dark_yellow,
        stripe_width=10,
        spacing=8,
        angle=45
    )

    return textures


# Cache global de texturas
_texture_cache = None


def get_player_texture(player_index, size=(100, 100)):
    """Retorna a textura do jogador, usando cache."""
    global _texture_cache
    if _texture_cache is None or _texture_cache[0] != size:
        _texture_cache = (size, create_player_textures(size))
    return _texture_cache[1].get(player_index)