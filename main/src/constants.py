import pygame

# Inicialização
pygame.init()

# Dimensões
SCREEN_WIDTH = 880  # expanded 10%
SCREEN_HEIGHT = 660  # expanded 10%

# Scoreboard area
SCOREBOARD_WIDTH = int(SCREEN_WIDTH * 0.3)
SCOREBOARD_PADDING = 10

# Cores
BG_COLOR       = pygame.Color('#ffffff')
BUTTON_COLOR   = pygame.Color('#61afef')
BUTTON_HOVER   = pygame.Color('#528dcf')
TEXT_COLOR     = pygame.Color('#000000')
SHAPES_COLOR   = pygame.Color('#111111')
PLAYER_COLORS  = [pygame.Color('#cf2c2f'),
                  pygame.Color('#45a309'),
                  pygame.Color('#05819b'),
                  pygame.Color('#a25c9c'),
                  pygame.Color('#f0a30a')]

# Fonte
FONT_LARGE  = pygame.font.SysFont(None, 48)
FONT_MEDIUM = pygame.font.SysFont(None, 32)
FONT_SMALL  = pygame.font.SysFont(None, 20)
FONT_SUPER_SMALL = pygame.font.SysFont(None, 14)

# Estado do menu
temporary_number_of_players = 2     # valor temporário antes de confirmar no botão
max_players = 5
min_players = 2

# Nomes personalizáveis (pode ser alterado antes de iniciar)
player_names = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4', 'Jogador 5']

# Retângulos das setas
LEFT_ARROW  = pygame.Rect(SCREEN_WIDTH // 2 - 50, 200, 30, 30)
RIGHT_ARROW = pygame.Rect(SCREEN_WIDTH // 2 + 50, 200, 30, 30)
PLAY_BUTTON = pygame.Rect((SCREEN_WIDTH // 2 - 100, 500), (200, 60))
