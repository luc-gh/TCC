import sys
import pygame
from constants import *
from graph import Graph

# Tela de jogo
def play(screen, graph: Graph, events):
    # Variáveis estáticas para manter estado entre chamadas
    if not hasattr(play, "turn"):
        play.turn = 0
        play.finished = False
        play.winner = None
    screen.fill(BG_COLOR)
    # Desenha grafo (faces preenchidas e arestas)
    graph.desenhar(screen, cor_arestas=SHAPES_COLOR, largura_arestas=1)
    # Indica turno atual na frente
    turno_text = f"Vez de: {player_names[play.turn]}"
    turno_surf = FONT_MEDIUM.render(turno_text, True, PLAYER_COLORS[play.turn])
    screen.blit(turno_surf, (20, 20))
    # Processa eventos
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if play.finished:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and PLAY_BUTTON.collidepoint(event.pos):
                # voltar ao menu
                play.turn = 0; play.finished = False; play.winner = None
                return False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                for idx, face in enumerate(graph.faces):
                    if graph._ponto_no_poligono(pos, face['vertices']) and face['color'] is None:
                        cor = PLAYER_COLORS[play.turn]
                        # checa faces adjacentes (compartilham aresta)
                        bloqueado = False
                        # gera arestas da face clicada
                        f_verts = face['vertices']
                        edges_f = set(tuple(sorted((f_verts[i], f_verts[(i+1)%len(f_verts)]))) for i in range(len(f_verts)))
                        for j, other in enumerate(graph.faces):
                            if j==idx or other['color'] is None: continue
                            # arestas da outra face
                            ov = other['vertices']
                            edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))
                            # se compartilham aresta
                            if edges_f & edges_o and other['color']==cor:
                                bloqueado = True; break
                        if not bloqueado:
                            graph.colorir_face(idx, cor)
                            play.turn = 1 - play.turn
                        break
    # Verifica jogadas possíveis
    if not play.finished:
        cor = PLAYER_COLORS[play.turn]; possible=False
        for idx, face in enumerate(graph.faces):
            if face['color'] is not None: continue
            # monta arestas
            verts = face['vertices']
            edges_f = set(tuple(sorted((verts[i], verts[(i+1)%len(verts)]))) for i in range(len(verts)))
            bloqueado=False
            for j, other in enumerate(graph.faces):
                if j==idx or other['color'] is None: continue
                ov = other['vertices']
                edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))
                if edges_f & edges_o and other['color']==cor:
                    bloqueado=True; break
            if not bloqueado:
                possible=True; break
        if not possible:
            play.finished=True; play.winner=1-play.turn
    # Quando finalizado, mostra mensagem e botão
    if play.finished:
        msg = f"{player_names[play.winner]} venceu!"
        msg_surf = FONT_LARGE.render(msg, True, PLAYER_COLORS[play.winner])
        # exibe mensagem de vitória no topo centralizado
        msg_rect = msg_surf.get_rect(midtop=(SCREEN_WIDTH//2, 20))
        screen.blit(msg_surf, msg_rect)
        color_btn = BUTTON_HOVER if PLAY_BUTTON.collidepoint(pygame.mouse.get_pos()) else BUTTON_COLOR
        pygame.draw.rect(screen, color_btn, PLAY_BUTTON, border_radius=8)
        label = FONT_MEDIUM.render("Voltar ao menu", True, TEXT_COLOR)
        screen.blit(label, label.get_rect(center=PLAY_BUTTON.center))
    pygame.display.update()
    return True
