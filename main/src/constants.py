import pygame

# Inicialização
pygame.init()

# Dimensões
SCREEN_WIDTH = 880  # expanded 10%
SCREEN_HEIGHT = 660  # expanded 10%

# Scoreboard area
SCOREBOARD_WIDTH = int(SCREEN_WIDTH * 0.28)
SCOREBOARD_PADDING = 10

# Cores
BG_COLOR       = pygame.Color('#ffffff')
BUTTON_COLOR   = pygame.Color('#61afef')
BUTTON_HOVER   = pygame.Color('#528dcf')
TEXT_COLOR     = pygame.Color('#000000')
SHAPES_COLOR   = pygame.Color('#111111')

# Configuração de jogadores - ALTERE APENAS MAX_PLAYERS PARA AJUSTAR O JOGO
MAX_PLAYERS = 10
MIN_PLAYERS = 2

# Cores base dos jogadores (expandido para suportar até 10 jogadores)
_BASE_PLAYER_COLORS = [
    pygame.Color('#df1515'),  # Vermelho
    pygame.Color('#008000'),  # Verde
    pygame.Color('#000080'),  # Azul
    pygame.Color('#ffc30a'),  # Amarelo
    pygame.Color('#ff4d05'),  # Laranja
    pygame.Color('#800080'),  # Roxo
    pygame.Color('#5b1f00'),  # Marrom
    pygame.Color('#00ffff'),  # Ciano
    pygame.Color('#f000d0'),  # Rosa
    pygame.Color('#808080')   # Cinza
]

# Gera as cores e nomes baseado em MAX_PLAYERS
PLAYER_COLORS = _BASE_PLAYER_COLORS[:MAX_PLAYERS]
player_names = [f'Jogador {i+1}' for i in range(MAX_PLAYERS)]

# Estado do menu
temporary_number_of_players = MIN_PLAYERS
max_players = MAX_PLAYERS
min_players = MIN_PLAYERS

# Fonte
FONT_LARGE  = pygame.font.SysFont(None, 48)
FONT_MEDIUM = pygame.font.SysFont(None, 32)
FONT_SMALL  = pygame.font.SysFont(None, 20)
FONT_SUPER_SMALL = pygame.font.SysFont(None, 14)

# Retângulos das setas
LEFT_ARROW  = pygame.Rect(SCREEN_WIDTH // 2 - 50, 200, 30, 30)
RIGHT_ARROW = pygame.Rect(SCREEN_WIDTH // 2 + 50, 200, 30, 30)
PLAY_BUTTON = pygame.Rect((SCREEN_WIDTH // 2 - 100, 500), (200, 60))
