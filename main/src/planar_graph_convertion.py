"""
Módulo para conversão de shapes em segmentos para grafo planar.
Implementa as funções extract_segments, find_intersections e split_segments conforme teoria de grafos planares.
"""
import math
from math import atan2


def _approximate_curve(cx, cy, a, b, resolution):
    """Aproxima curva elíptica (ou circular se a=b) por segmentos."""
    pts = [
        (cx + a * math.cos(i * 2*math.pi / resolution),
         cy + b * math.sin(i * 2*math.pi / resolution))
        for i in range(resolution+1)
    ]
    return list(zip(pts, pts[1:]))


# ETAPA 1:
def extract_segments(shapes, circle_resolution=32):
    """
    Dada uma lista de shapes ('tipo', dados), retorna lista de segmentos.
    Cada segmento é uma tupla ((x1, y1), (x2, y2)).
    Suporta 'rect', 'polygon', 'circle', 'ellipse'.
    """
    segments = []
    for typ, data in shapes:
        if typ == 'rect':
            rect = data
            pts = [(rect.x, rect.y),
                   (rect.x+rect.width, rect.y),
                   (rect.x+rect.width, rect.y+rect.height),
                   (rect.x, rect.y+rect.height)]
            segments.extend((pts[i], pts[(i+1)%4]) for i in range(4))
        elif typ == 'polygon':
            pts = data
            segments.extend((pts[i], pts[(i+1)%len(pts)]) for i in range(len(pts)))
        elif typ == 'circle':
            cx, cy, r = data
            segments.extend(_approximate_curve(cx, cy, r, r, circle_resolution))
        elif typ == 'ellipse':
            rect = data
            cx = rect.x + rect.width/2
            cy = rect.y + rect.height/2
            a = rect.width/2
            b = rect.height/2
            segments.extend(_approximate_curve(cx, cy, a, b, circle_resolution))
        else:
            raise ValueError(f"Tipo de shape desconhecido: {typ}")
    return segments


# ETAPA 2:
def find_intersections(segments, eps=1e-6):
    """
    Encontra todos os pontos de interseção entre pares de segmentos e inclui endpoints.
    Retorna lista de tuplas (x, y) únicas.
    """
    def sub(u, v): return u[0]-v[0], u[1]-v[1]
    def cross(u, v): return u[0]*v[1] - u[1]*v[0]

    pts = []
    # incluir endpoints de todos segmentos
    for a, b in segments:
        pts.append(a)
        pts.append(b)
    n = len(segments)
    # interseções par-a-par
    for i in range(n):
        p, q = segments[i]
        r = sub(q, p)
        for j in range(i+1, n):
            u, v = segments[j]
            s = sub(v, u)
            denom = cross(r, s)
            if abs(denom) < eps:
                continue
            qp = sub(u, p)
            t = cross(qp, s) / denom
            u_param = cross(qp, r) / denom
            if 0 <= t <= 1 and 0 <= u_param <= 1:
                inter = (p[0] + t*r[0], p[1] + t*r[1])
                pts.append(inter)
    # remover duplicatas numéricas
    unique = []
    for x, y in pts:
        if not any(abs(x-x2) < eps and abs(y-y2) < eps for x2, y2 in unique):
            unique.append((x, y))
    return unique


# ETAPA 3:
def split_segments(segments, vertices, eps=1e-6):
    """
    Dado lista de segmentos e vértices (x,y), subdivide cada segmento em subsegmentos entre vértices colineares.
    Retorna lista de arestas (pares de vértices).
    """
    def dot(u, v): return u[0]*v[0] + u[1]*v[1]
    def sub(u, v): return u[0]-v[0], u[1]-v[1]

    edges = []
    for p, q in segments:
        # coletar vértices que estão sobre o segmento "p" ⇾ "q"
        pts_on = []
        pq = sub(q, p)
        norm2 = dot(pq, pq)
        for v in vertices:
            pv = sub(v, p)
            # verificar colinearidade por cross==0 e que projeção está entre 0 e norm2
            if abs(pv[0]*pq[1] - pv[1]*pq[0]) < eps:
                t = dot(pv, pq) / norm2
                if -eps <= t <= 1+eps:
                    pts_on.append((t, v))
        # ordenar por parâmetro t e criar sub-arestas
        pts_on.sort(key=lambda x: x[0])
        for i in range(len(pts_on)-1):
            v1 = pts_on[i][1]
            v2 = pts_on[i+1][1]
            if v1 != v2:
                edges.append((v1, v2))
    # remover duplicatas (considerando arestas não orientadas)
    unique = set()
    final = []
    for a, b in edges:
        key = tuple(sorted((a, b)))
        if key not in unique:
            unique.add(key)
            final.append((a, b))
    return final


# ETAPA 4:
def detect_faces(vertices, edges, eps=1e-6):
    """
    Dado vértices [(x,y)] e arestas [(v1, v2)], retorna faces como listas de vértices em ciclo.
    Usa half-edge e ordenação angular para extrair ciclos de faces interiores.
    """
    # map coords to index
    vid = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    # build adjacency
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        ia, ib = vid[a], vid[b]
        adj[ia].append(ib)
        adj[ib].append(ia)
    # sort neighbors CCW
    sorted_adj = {}
    for i, neigh in adj.items():
        x0, y0 = vertices[i]
        sorted_adj[i] = sorted(neigh, key=lambda j: atan2(vertices[j][1]-y0, vertices[j][0]-x0))
    visited = set()
    faces = []
    # traverse half-edges
    for u in sorted_adj:
        for v in sorted_adj[u]:
            if (u, v) in visited:
                continue
            cycle = []
            start = (u, v)
            curr = start
            while True:
                u_curr, v_curr = curr
                visited.add(curr)
                cycle.append(u_curr)
                # find in v_curr's neighbor list index of u_curr
                neighs = sorted_adj[v_curr]
                idx = neighs.index(u_curr)
                # previous in list gives right-hand turn
                next_idx = (idx - 1) % len(neighs)
                w = neighs[next_idx]
                curr = (v_curr, w)
                if curr == start:
                    break
            # build face coords and compute signed area
            face_coords = [vertices[i] for i in cycle]
            area = 0
            m = len(face_coords)
            for i in range(m):
                x1, y1 = face_coords[i]
                x2, y2 = face_coords[(i+1) % m]
                area += x1*y2 - x2*y1
            area *= 0.5
            # keep only CCW small faces
            if area > eps:
                faces.append(face_coords)
    return faces
