# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 20

import sys


def find_hamiltonian_cycle(input_graph, start_vert):
    def path_recursion(current_path):
        if len(current_path) == len(input_graph):
            return current_path + [start_vert] if start_vert in input_graph[current_path[-1]] else None
        
        for next_vert in sorted(input_graph[current_path[-1]]):
            if next_vert not in current_path:
                new_path = current_path + [next_vert]
                extended_path = path_recursion(new_path)
                if extended_path:
                    return extended_path
        
        return None

    return path_recursion([start_vert])


def process_input(input_string):
    raw_graphs = input_string.strip().split('%')
    parsed_graphs = []
    
    for raw_graph in raw_graphs:
        lines = [line for line in raw_graph.strip().split('\n') if line]
        if lines:
            vert_count = int(lines[0])
            graph = {i+1: [] for i in range(vert_count)}
            
            for line in lines[1:]:
                vert1, vert2 = map(int, line.split())
                graph[vert1].append(vert2)
                graph[vert2].append(vert1)
            
            parsed_graphs.append(graph)
    
    return parsed_graphs


def format_output(output_list): # simple function to help with output list comp
    return '\n'.join(' '.join(map(str, cycle)) if cycle else 'None' for cycle in output_list)


def main():
    input_string = sys.stdin.read()
    parsed_graphs = process_input(input_string)
    hamiltonian_cycles = [find_hamiltonian_cycle(graph, 1) for graph in parsed_graphs]
    
    print(format_output(hamiltonian_cycles))


if __name__ == "__main__":
    main()

