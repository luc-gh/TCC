import pygame
import math

def _clamp(v, a=0, b=255):
    """Limita um valor entre a e b."""
    return max(a, min(b, int(v)))


def _shade_color(color, factor):
    """Retorna uma cor (r,g,b) clareada (factor>1) ou escurecida (factor<1)."""
    r, g, b = color[:3]
    return (_clamp(r * factor), _clamp(g * factor), _clamp(b * factor))


def gradient_surface(size, start_color, end_color, vertical=True):
    """Cria um Surface com um gradiente linear.
    start_color/end_color = (r,g,b) ou (r,g,b,a). size = (w,h).
    vertical=True para top->bottom, False para left->right.
    """
    w, h = size
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    r1,g1,b1 = start_color[:3]
    r2,g2,b2 = end_color[:3]
    for i in range(h if vertical else w):
        t = i / (h-1) if vertical else i / (w-1)
        r = int(r1 + (r2-r1)*t)
        g = int(g1 + (g2-g1)*t)
        b = int(b1 + (b2-b1)*t)
        if vertical:
            pygame.draw.line(surf, (r,g,b), (0,i), (w-1,i))
        else:
            pygame.draw.line(surf, (r,g,b), (i,0), (i,h-1))
    return surf.convert_alpha()

def stripe_texture(size, base_color, stripe_color, stripe_width=6, spacing=6, angle=0):
    """Cria uma textura listrada. angle em graus (0 = horizontais).
    size = (w,h). stripe_width e spacing em pixels.
    """
    w, h = size
    base = pygame.Surface((w, h), pygame.SRCALPHA)
    base.fill(base_color)
    # criar uma pequena superfície repetível maior que a diagonal para rotação segura
    pattern = pygame.Surface((w, h), pygame.SRCALPHA)
    # Desenhar listras horizontais no pattern (serão rotacionadas depois se angle != 0)
    y = -spacing
    while y < h + stripe_width:
        pygame.draw.rect(pattern, stripe_color, pygame.Rect(0, int(y), w, stripe_width))
        y += stripe_width + spacing
    if angle != 0:
        # rotacionar pattern e centralizar
        rot = pygame.transform.rotate(pattern, angle)
        # cortar/regenerar na área original (toma o centro)
        rect = rot.get_rect(center=(w//2, h//2))
        final = pygame.Surface((w, h), pygame.SRCALPHA)
        final.blit(rot, rect)
    else:
        final = pattern
    base.blit(final, (0,0), special_flags=pygame.BLEND_RGBA_ADD)
    return base.convert_alpha()


def pixel_texture(size, base_color, tile_size=4, pattern='checker'):
    """Cria uma textura "pixelada" formada por quadradinhos (tiles) com 4 tonalidades

    - size: (w,h) em pixels da superfície resultante
    - base_color: (r,g,b) cor base
    - tile_size: lado (em px) de cada quadradinho
    - pattern: 'checker' (padrão 2x2 repetitivo) ou 'random' (escolha aleatória entre as 4 tonalidades)

    Retorna um Surface com SRCALPHA pronto para blitar / tilear.
    """
    w, h = size
    surf = pygame.Surface((w, h), pygame.SRCALPHA)

    # gerar 4 tonalidades a partir da cor base: leve escurecimento/clareamento
    shades = [
        _shade_color(base_color, 0.85),  # levemente escuro
        _shade_color(base_color, 1.0),   # base
        _shade_color(base_color, 1.15),  # levemente claro
        _shade_color(base_color, 1.35),  # mais claro
    ]

    gx_count = math.ceil(w / tile_size)
    gy_count = math.ceil(h / tile_size)

    for gy in range(gy_count):
        for gx in range(gx_count):
            # escolher índice entre 0..3
            if pattern == 'random':
                idx = (gx * 1103515245 + gy * 12345) & 3  # simples pseudo-determinístico (faster than random)
            else:  # checker padrão 2x2 repetitivo
                idx = (gx % 2) * 2 + (gy % 2)
            color = shades[idx]
            rect = pygame.Rect(gx * tile_size, gy * tile_size, tile_size, tile_size)
            surf.fill(color, rect)

    return surf.convert_alpha()


def wave_texture(size, base_color, wave_color=None, amplitude=6, wavelength=40, thickness=12, spacing=24, phase=0):
    """Cria uma textura com padrão de ondas senoidais.

    - size: (w,h) tamanho da superfície em pixels
    - base_color: (r,g,b) cor de fundo
    - wave_color: (r,g,b) cor das ondas (se None, usa tonalidade mais clara da base)
    - amplitude: altura das ondas
    - wavelength: comprimento de onda (distância entre picos)
    - thickness: espessura das faixas de onda
    - spacing: espaçamento vertical entre ondas
    - phase: deslocamento de fase (para animar)
    """
    w, h = size
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    surf.fill(base_color)

    if wave_color is None:
        # tonalidade levemente mais clara
        wave_color = _shade_color(base_color, 1.25)

    # passo horizontal para amostrar a curva (quanto menor, mais precisa)
    dx = max(1, int(max(1, wavelength) / 8))

    # desenha faixas centradas em múltiplos de `spacing`
    for center in range(-spacing, h + spacing, spacing):
        pts_top = []
        for x in range(0, w + 1, dx):
            # y da curva; convert para int
            y = int(center + amplitude * math.sin(2 * math.pi * (x / max(1, wavelength)) + phase))
            pts_top.append((x, y))
        # criar os pontos inferiores (top + thickness) em ordem inversa
        pts_bottom = [(x, y + thickness) for (x, y) in reversed(pts_top)]
        poly = pts_top + pts_bottom
        pygame.draw.polygon(surf, wave_color, poly)

    return surf.convert_alpha()