# Name: Chanwoo Ray Baae
# Course: Coding Quandaries
# Coding Quandary 16

import sys
from collections import defaultdict

def find_longest_path_from_node(start_node, traversed_edges):
    
    longest_path_from_this_node = 0
    
    for connected_node in graph[start_node]:
        edge = frozenset([start_node, connected_node])
        
        if edge not in traversed_edges:
            traversed_edges.add(edge)
            longest_path_from_this_node = max(longest_path_from_this_node, 1 + find_longest_path_from_node(connected_node, traversed_edges))
            traversed_edges.remove(edge)
    
    return longest_path_from_this_node


def main():
    while True:
        total_nodes, total_edges = map(int, sys.stdin.readline().split())
        if total_nodes == 0 and total_edges == 0: 
            break

        global graph
        graph = defaultdict(list)
        for _ in range(total_edges):
            node1, node2 = map(int, sys.stdin.readline().split())
            graph[node1].append(node2)
            graph[node2].append(node1)

        longest_path_in_graph = 0
        for node in range(total_nodes):
            longest_path_in_graph = max(longest_path_in_graph, find_longest_path_from_node(node, set()))

        print(longest_path_in_graph)


if __name__ == "__main__":
    main()

