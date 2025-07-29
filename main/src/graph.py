from planar_graph_convertion import *

class Graph:
    def __init__(self, shapes, min_face_area=20):
        self.shapes = shapes
        self.vertices = []
        self.edges = []
        self.faces = []
        self.min_face_area = min_face_area

        self._build_graph()

    def _build_graph(self):
        segments = extract_segments(shapes=self.shapes)
        self.vertices = find_intersections(segments=segments)
        self.edges = split_segments(segments=segments, vertices=self.vertices)
        self.faces = detect_faces(vertices=self.vertices, edges=self.edges)
