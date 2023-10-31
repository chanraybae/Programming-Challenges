# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 18

import heapq

class GraphEdge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __lt__(self, other_edge):
        return self.weight < other_edge.weight


class DisjointSetForest:
    def __init__(self, vertex_count):
        self.vertex_ranks = [0] * vertex_count
        self.parent_vertices = list(range(vertex_count))

    def find_parent(self, vertex):
        if self.parent_vertices[vertex] != vertex:
            self.parent_vertices[vertex] = self.find_parent(self.parent_vertices[vertex])
        return self.parent_vertices[vertex]

    def merge(self, vertex1, vertex2):
        root_vertex1 = self.find_parent(vertex1)
        root_vertex2 = self.find_parent(vertex2)

        if root_vertex1 != root_vertex2:
            if self.vertex_ranks[root_vertex1] < self.vertex_ranks[root_vertex2]:
                self.parent_vertices[root_vertex1] = root_vertex2
            else:
                self.parent_vertices[root_vertex2] = root_vertex1
                if self.vertex_ranks[root_vertex1] == self.vertex_ranks[root_vertex2]:
                    self.vertex_ranks[root_vertex1] += 1


def kruskals_algo(vertex_count, adjacency_matrix):
    graph_edges = []

    for i in range(vertex_count):
        for j in range(i+1, vertex_count):
            if adjacency_matrix[i][j] != float('inf'):
                graph_edges.append(GraphEdge(adjacency_matrix[i][j], i, j))

    graph_edges.sort()
    disjoint_set_forest = DisjointSetForest(vertex_count)

    tot_weight = 0
    mst_edges = []
    for edge in graph_edges:
        if disjoint_set_forest.find_parent(edge.start_vertex) != disjoint_set_forest.find_parent(edge.target_vertex):
            tot_weight += edge.weight
            disjoint_set_forest.merge(edge.start_vertex, edge.target_vertex)
            mst_edges.append(edge)

    print(tot_weight)
    for edge in sorted(mst_edges, key=lambda edge: (chr(edge.start_vertex + 65), chr(edge.target_vertex + 65))):
        print(''.join(sorted([chr(edge.start_vertex + 65), chr(edge.target_vertex + 65)])))


def main():
    # reading all lines first
    all_lines = []
    try:
        while True:
            all_lines.append(input())
    except EOFError:
        pass

    # processing each line
    line_index = 0
    while line_index < len(all_lines):
        number_of_vertices = int(all_lines[line_index])
        line_index += 1
        adjacency_matrix = []
        for _ in range(number_of_vertices):
            row = [float('inf') if n == '-1' else int(n) for n in all_lines[line_index].split()]
            adjacency_matrix.append(row)
            line_index += 1

        kruskals_algo(number_of_vertices, adjacency_matrix)

        # printing newline if more graphs to process
        if line_index < len(all_lines):
            print()


if __name__ == "__main__":
    main()
