import pygame, constants
from textures import gradient_surface, stripe_texture, pixel_texture, wave_texture


def create_player_textures(size=(100, 100)):
    """
    Cria texturas procedurais para cada jogador baseadas em suas cores.
    Retorna um dicionário {player_index: Surface}.
    Se adapta automaticamente ao número de jogadores definido em constants.MAX_PLAYERS.
    """
    textures = {}

    # Padrões de textura que se repetem ciclicamente
    texture_patterns = [
        'wave',                # 0
        'stripe_diagonal',     # 1
        'pixel',               # 2
        'solid',               # 3
        'wave',                # 4
        'stripe_horizontal',   # 5
        'wave',                # 6
        'solid',               # 7
        'stripe_diagonal',     # 8
        'pixel'                # 9
    ]

    for i in range(len(constants.PLAYER_COLORS)):
        base_color = constants.PLAYER_COLORS[i]
        pattern = texture_patterns[i % len(texture_patterns)]

        if pattern == 'wave':
            textures[i] = wave_texture(size, base_color)

        elif pattern == 'gradient_vertical':
            dark_color = pygame.Color(
                max(0, base_color.r - 40),
                max(0, base_color.g - 20),
                max(0, base_color.b - 20)
            )
            textures[i] = gradient_surface(size, base_color, dark_color, vertical=True)

        elif pattern == 'stripe_diagonal':
            dark_color = pygame.Color(
                max(0, base_color.r - 30),
                max(0, base_color.g - 30),
                max(0, base_color.b - 30)
            )
            textures[i] = stripe_texture(size, base_color, dark_color, stripe_width=8, spacing=8, angle=45)

        elif pattern == 'pixel':
            textures[i] = pixel_texture(size, base_color, tile_size=5, pattern='checker')

        elif pattern == 'stripe_horizontal':
            light_color = pygame.Color(
                min(255, base_color.r + 25),
                min(255, base_color.g + 25),
                min(255, base_color.b + 25)
            )
            textures[i] = stripe_texture(size, base_color, light_color, stripe_width=6, spacing=6, angle=0)

        elif pattern == 'solid':
            textures[i] = pygame.Surface(size, pygame.SRCALPHA)
            textures[i].fill(base_color)

        elif pattern == 'gradient_horizontal':
            light_color = pygame.Color(
                min(255, base_color.r + 40),
                min(255, base_color.g + 40),
                min(255, base_color.b + 40)
            )
            textures[i] = gradient_surface(size, base_color, light_color, vertical=False)

    return textures


# Cache global de texturas
_texture_cache = None


def get_player_texture(player_index, size=(100, 100)):
    """Retorna a textura do jogador, usando cache."""
    global _texture_cache
    if _texture_cache is None or _texture_cache[0] != size:
        _texture_cache = (size, create_player_textures(size))
    return _texture_cache[1].get(player_index)