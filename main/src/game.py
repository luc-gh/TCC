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
    if not hasattr(play, "turn"):
        play.turn = 0
        play.finished = False
        play.winner = None
    screen.fill(constants.BG_COLOR)

    # Desenha grafo (faces preenchidas e arestas)
    graph.desenhar(screen, cor_arestas=constants.SHAPES_COLOR, largura_arestas=1)

    # Indica turno atual na frente
    turno_text = f"Vez de: {constants.player_names[play.turn]}"
    turno_surf = constants.FONT_MEDIUM.render(turno_text, True, constants.PLAYER_COLORS[play.turn])
    screen.blit(turno_surf, (20, 20))
    # Verifica se jogador atual não tem jogadas; se sim, encerra jogo (último a jogar vence)
    # Função inline para verificar jogadas
    def player_can_move(idx):
        cor = constants.PLAYER_COLORS[idx]
        for face in graph.faces:
            if face['color'] is not None: continue
            # arestas da face
            verts = face['vertices']
            edges_f = set(tuple(sorted((verts[i], verts[(i+1)%len(verts)]))) for i in range(len(verts)))
            # verifica bloqueio por mesma cor em face adjacente
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

    if not player_can_move(play.turn):
        play.finished = True
        play.winner = (play.turn - 1) % constants.temporary_number_of_players
        # skip event processing, will draw vitória no bloco abaixo
        # ...existing code continues to draw end screen...
    # Processa eventos
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if play.finished:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and constants.PLAY_BUTTON.collidepoint(event.pos):
                # voltar ao menu
                play.turn = 0
                play.finished = False
                play.winner = None
                return False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("Vez de jogador:", play.turn)
                pos = event.pos
                for idx, face in enumerate(graph.faces):
                    if graph._ponto_no_poligono(pos, face['vertices']) and face['color'] is None:

                        cor = constants.PLAYER_COLORS[play.turn]

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
                                print("Jogador", play.turn, "não pode colorir a face", idx, "com a cor", cor, "porque está bloqueado por outra face.")
                                break

                        if not bloqueado:
                            graph.colorir_face(idx, cor)

                            # Lógica de turno
                            play.turn = (play.turn + 1) % constants.temporary_number_of_players

                        break
    # Quando finalizado, mostra mensagem no topo e botão
    if play.finished:
        msg = f"{constants.player_names[play.winner]} venceu!"
        msg_surf = constants.FONT_LARGE.render(msg, True, "#000000")

        # exibe mensagem de vitória no topo centralizado
        msg_rect = msg_surf.get_rect(midtop=(constants.SCREEN_WIDTH//2, 20))
        screen.blit(msg_surf, msg_rect)

        color_btn = constants.BUTTON_HOVER if constants.PLAY_BUTTON.collidepoint(pygame.mouse.get_pos()) else constants.BUTTON_COLOR
        pygame.draw.rect(screen, color_btn, constants.PLAY_BUTTON, border_radius=8)

        label = constants.FONT_MEDIUM.render("Voltar ao menu", True, constants.TEXT_COLOR)
        screen.blit(label, label.get_rect(center=constants.PLAY_BUTTON.center))
    pygame.display.update()
    return True
