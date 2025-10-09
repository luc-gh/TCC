import sys
import pygame
import constants
from graph import Graph


def qualquer_pode_jogar(graph: Graph):
    for i, cor in enumerate(constants.PLAYER_COLORS):
        for face in graph.faces:

            # verifica se este jogador está ativo
            if i >= constants.temporary_number_of_players:
                break

            if face['color'] is not None:
                continue
            verts = face['vertices']
            edges_f = set(tuple(sorted((verts[k], verts[(k+1)%len(verts)]))) for k in range(len(verts)))
            bloqueado = False
            for other in graph.faces:
                if other['color'] is None or other is face:
                    continue
                ov = other['vertices']
                edges_o = set(tuple(sorted((ov[k], ov[(k+1)%len(ov)]))) for k in range(len(ov)))
                if edges_f & edges_o and other['color']==cor:
                    bloqueado = True
                    # Mensagem de indicação de bloqueio
                    break
            if not bloqueado:
                return True
    return False

# Tela de jogo
def play(screen, graph: Graph, events):

    # Variáveis estáticas para manter estado entre chamadas
    if not hasattr(play, "active_players"):
        play.active_players = list(range(constants.temporary_number_of_players))
        play.turn_pos = 0
        play.finished = False
        play.winner = None
        play.last_player = None
        # initialize strikes and timer
        play.strikes = {p: 0 for p in play.active_players}
        play.turn_start_time = pygame.time.get_ticks()
        play.timeout_message = None
        play.timeout_message_time = None

    screen.fill(constants.BG_COLOR)

    graph_area = pygame.Rect(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    prev_clip = screen.get_clip()
    screen.set_clip(graph_area)
    graph.desenhar(screen, cor_arestas=constants.SHAPES_COLOR, largura_arestas=3)  # Largura maior
    screen.set_clip(prev_clip)

    def player_can_move(idx):
        cor = constants.PLAYER_COLORS[idx]
        for face in graph.faces:
            if face['color'] is not None: continue
            verts = face['vertices']
            edges_f = set(tuple(sorted((verts[i], verts[(i+1)%len(verts)]))) for i in range(len(verts)))
            blocked = False
            for other in graph.faces:
                if other is face or other['color'] is None: continue
                ov = other['vertices']
                edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))
                if edges_f & edges_o and other['color'] == cor:
                    blocked = True; break
            if not blocked:
                return True
        return False

    # Elimina jogadores sem jogadas possíveis
    for p in play.active_players.copy():
        if not player_can_move(p):
            play.active_players.remove(p)

    # Ajusta turn_pos para ficar dentro do range atual de active_players
    if play.active_players:
        play.turn_pos %= len(play.active_players)

    # Verifica fim de jogo: se restar 1 ou nenhum jogador ativo
    if not play.finished and len(play.active_players) <= 1:
        play.finished = True
        if len(play.active_players) == 1:
            play.winner = play.active_players[0]
        else:
            # todos eliminados; último a jogar vence
            play.winner = play.last_player

    if not play.finished and play.active_players:
        current = play.active_players[play.turn_pos]
        now = pygame.time.get_ticks()
        elapsed = (now - play.turn_start_time) / 1000
        remaining = max(0, int(30 - elapsed))
        if remaining <= 0:
            play.strikes[current] += 1
            play.timeout_message = f"Vez perdida por {constants.player_names[current]}"
            play.timeout_message_time = now
            if play.strikes[current] >= 3:
                play.active_players.remove(current)
                if play.active_players:
                    play.turn_pos %= len(play.active_players)
                else:
                    play.turn_pos = 0
            else:
                play.turn_pos = (play.turn_pos + 1) % len(play.active_players)
            play.turn_start_time = now

        # Desenha placar lateral
        inicio_area_placar_x = constants.SCREEN_WIDTH - constants.SCOREBOARD_WIDTH + 25
        center_x = inicio_area_placar_x + constants.SCOREBOARD_WIDTH // 2
        padding = constants.SCOREBOARD_PADDING
        col_w = (constants.SCOREBOARD_WIDTH - padding * 2) // 4
        row_h = constants.FONT_MEDIUM.get_height() + 8

        # retângulo dinâmico ao redor do placar
        box_rect = pygame.Rect(
            inicio_area_placar_x + 30,                 # pos x
            padding,                                   # pos y
            constants.SCOREBOARD_WIDTH - 70,           # largura
            row_h * len(play.active_players) + 5       # altura (dinâmica conforme jogadores)
        )

        pygame.draw.rect(screen, constants.SHAPES_COLOR, box_rect, 2)
        for idx, p in enumerate(play.active_players):
            y = padding + 10 + idx * row_h
            x = inicio_area_placar_x + padding
            if p == current:
                arrow = constants.FONT_MEDIUM.render('>', True, constants.PLAYER_COLORS[p])
                screen.blit(arrow, (x+35, y-6))
            name = constants.FONT_SMALL.render(constants.player_names[p], True, constants.PLAYER_COLORS[p])
            screen.blit(name, (x + col_w, y))
            if p == current:
                timer = constants.FONT_SMALL.render(f"{remaining}s", True, constants.TEXT_COLOR)
                screen.blit(timer, (x + col_w * 2 + 15, y))
            strikes = constants.FONT_SMALL.render(f"{play.strikes.get(p,0)}/3", True, constants.TEXT_COLOR)
            screen.blit(strikes, (x + col_w * 3, y))

        if play.timeout_message and now - play.timeout_message_time <= 2000:
            msg_surf = constants.FONT_SMALL.render(play.timeout_message, True, constants.TEXT_COLOR)
            msg_rect = msg_surf.get_rect(center=(center_x, y + 40))  # mensagem temporizada abaixo do placar
            screen.blit(msg_surf, msg_rect)

    # Processa eventos
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if play.finished:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and constants.PLAY_BUTTON.collidepoint(event.pos):
                # voltar ao menu: reset static state so next game reinitializes
                for attr in ("active_players", "turn_pos", "finished", "winner"):
                    if hasattr(play, attr):
                        delattr(play, attr)
                return False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and play.active_players:
                current = play.active_players[play.turn_pos]
                print("Vez de jogador:", current)
                pos = event.pos
                for idx, face in enumerate(graph.faces):
                    if graph._ponto_no_poligono(pos, face['vertices']) and face['color'] is None:

                        cor = constants.PLAYER_COLORS[current]

                        # checa faces adjacentes (compartilham aresta)
                        bloqueado = False

                        # gera arestas da face clicada
                        f_verts = face['vertices']

                        # pega a lista de valores únicos de tuplas ordenadas que representam as arestas de uma face,
                        #  geradas a partir de cada par de vértices consecutivos (incluindo a conexão do último ao primeiro).
                        edges_f = set(tuple(sorted((f_verts[i], f_verts[(i+1)%len(f_verts)]))) for i in range(len(f_verts)))

                        for j, other in enumerate(graph.faces):
                             if j==idx or other['color'] is None:
                                 continue

                             # arestas da outra face
                             ov = other['vertices']

                             # coleção de valores únicos de tuplas ordenadas que representam as arestas da outra face,
                             #  geradas a partir de cada par de vértices consecutivos (incluindo a conexão do último ao primeiro).
                             edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))

                             # se compartilham aresta
                             if edges_f & edges_o and other['color']==cor:
                                 bloqueado = True

                                 # movimento inválido: incrementa strikes e mostra mensagem
                                 now2 = pygame.time.get_ticks()
                                 play.strikes[current] += 1
                                 play.timeout_message = f"Jogada inválida: {play.strikes[current]}/3"
                                 play.timeout_message_time = now2

                                 # elimina jogador se atingir 3 strikes
                                 if play.strikes[current] >= 3:
                                     play.active_players.remove(current)

                                     # ajusta turn_pos para ficar dentro do range atual de active_players
                                     if play.active_players:
                                         play.turn_pos %= len(play.active_players)
                                     else:
                                         play.turn_pos = 0
                                 # zera o temporizador para o jogador atual ou próximo
                                 play.turn_start_time = now2
                                 break  # exit adjacency loop

                        # depois de checar todas as faces adjacentes
                        if bloqueado:
                            break  # exit face loop after invalid

                        if not bloqueado:
                            graph.colorir_face(idx, cor)

                            # registra último jogador que fez jogada
                            play.last_player = current

                            # Avança para o próximo jogador ativo
                            play.turn_pos = (play.turn_pos + 1) % len(play.active_players)
                            play.turn_start_time = pygame.time.get_ticks()
                            play.timeout_message = None
                            play.timeout_message_time = None

                            # Exibe informações do jogo
                            print(f"Jogadores ativos: {', '.join(map(str, play.active_players))}")
                            print(f"Vez de jogador: {constants.player_names[current]} ({current})")

                            # Lista de faces possíveis para o jogador atual
                            possible_faces = []
                            cor = constants.PLAYER_COLORS[current]
                            for idx, face in enumerate(graph.faces):
                                if face['color'] is not None:
                                    continue

                                # gera arestas da face candidata
                                f_verts = face['vertices']
                                edges_f = set(
                                    tuple(sorted((f_verts[i], f_verts[(i + 1) % len(f_verts)])))
                                    for i in range(len(f_verts))
                                )

                                # verifica bloqueio por faces adjacentes da mesma cor
                                blocked = False
                                for other in graph.faces:
                                    if other['color'] is None:
                                        continue
                                    ov = other['vertices']
                                    edges_o = set(
                                        tuple(sorted((ov[i], ov[(i + 1) % len(ov)])))
                                        for i in range(len(ov))
                                    )
                                    if edges_f & edges_o and other['color'] == cor:
                                        blocked = True
                                        break

                                if not blocked:
                                    possible_faces.append(idx)

                            print(f"Possíveis jogadas (faces): {', '.join(map(str, possible_faces))}")

                        break
    # Quando finalizado, mostra mensagem no topo e botão
    if play.finished:
        msg = f"{constants.player_names[play.winner]} venceu!"
        msg_surf = constants.FONT_LARGE.render(msg, True, constants.PLAYER_COLORS[play.winner])

        # exibe mensagem de vitória no topo centralizado
        msg_rect = msg_surf.get_rect(midtop=(constants.SCREEN_WIDTH//2, 20))

        padding_x = 20
        padding_y = 10
        bg_rect = msg_rect.inflate(padding_x, padding_y)
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, border_radius=4)

        screen.blit(msg_surf, msg_rect)

        color_btn = constants.BUTTON_HOVER if constants.PLAY_BUTTON.collidepoint(pygame.mouse.get_pos()) else constants.BUTTON_COLOR
        pygame.draw.rect(screen, color_btn, constants.PLAY_BUTTON, border_radius=8)

        label = constants.FONT_MEDIUM.render("Voltar ao menu", True, constants.TEXT_COLOR)
        screen.blit(label, label.get_rect(center=constants.PLAY_BUTTON.center))
    pygame.display.update()
    return True
