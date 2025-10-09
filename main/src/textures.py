import pygame
import math

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

def tiled_texture(size, texture):
    """Retorna um Surface do tamanho `size` preenchido com tiles de `texture`."""
    w, h = size
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    tw, th = texture.get_size()
    for x in range(0, w, tw):
        for y in range(0, h, th):
            surf.blit(texture, (x,y))
    return surf.convert_alpha()
