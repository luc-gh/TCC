import pygame
from planar_graph_convertion import extract_segments, find_intersections, split_segments, detect_faces

class Graph:
    def __init__(self, formas, area_minima_face=20):
        self.formas = formas
        self.area_minima_face = area_minima_face

        # Constrói grafo planar
        segmentos        = extract_segments(shapes=self.formas)
        self.vertices    = find_intersections(segmentos)
        self.arestas     = split_segments(segmentos, self.vertices)
        faces_brutas     = detect_faces(self.vertices, self.arestas)

        # Inicializa faces com cor padrão None (sem preenchimento)
        self.faces = []  # lista de dicts {'vertices': [...], 'color': pygame.Color or None}
        for lista_vertices in faces_brutas:
            area_face = 0
            quantidade_vertices = len(lista_vertices)
            for i in range(quantidade_vertices):
                x_vertice_inicial, y_vertice_inicial   = lista_vertices[i]
                x_vertice_seguinte, y_vertice_seguinte = lista_vertices[(i+1) % quantidade_vertices]
                area_face += x_vertice_inicial * y_vertice_seguinte - x_vertice_seguinte * y_vertice_inicial
            area_face = abs(area_face) * 0.5
            if area_face >= self.area_minima_face:
                self.faces.append({
                    'vertices': lista_vertices,
                    'color': None
                })

    def _ponto_no_poligono(self, ponto, vertices):
        """Testa se ponto dentro do polígono (ray-casting)."""
        x, y = ponto
        dentro = False
        total_vertices = len(vertices)
        for i in range(total_vertices):
            x_vertice_inicial, y_vertice_inicial   = vertices[i]
            x_vertice_seguinte, y_vertice_seguinte = vertices[(i+1) % total_vertices]
            if ((y_vertice_inicial > y) != (y_vertice_seguinte > y)) and \
               (x < (x_vertice_seguinte - x_vertice_inicial) * (y - y_vertice_inicial) / (y_vertice_seguinte - y_vertice_inicial) + x_vertice_inicial):
                dentro = not dentro
        return dentro

    def destacar_face_em(self, posicao, cor=None):
        """Altera cor da face que contém posicao. Padrão púrpura se cor None."""
        cor_alvo = pygame.Color('#ff00ff') if cor is None else cor
        for face in self.faces:
            if self._ponto_no_poligono(posicao, face['vertices']):
                face['color'] = cor_alvo
                break

    def colorir_face(self, indice_face, cor):
        """Altera cor da face específica. indice_face é índice em self.faces."""
        if 0 <= indice_face < len(self.faces):
            self.faces[indice_face]['color'] = pygame.Color(cor) if not isinstance(cor, pygame.Color) else cor

    def desenhar(self, superficie, cor_arestas=pygame.Color('black'), largura_arestas=1):
        """Desenha faces preenchidas (se color) e arestas."""
        # desenha faces
        for face in self.faces:
            if face['color']:
                pygame.draw.polygon(superficie, face['color'], face['vertices'])
        # desenha arestas
        for vertice_inicial, vertice_final in self.arestas:
            pygame.draw.line(superficie, cor_arestas, vertice_inicial, vertice_final, largura_arestas)
