# Name: Chanwoo Ray Bae
# Courses: Coding Quandaries
# Coding Quandary 21
# Using Edmonds-Karp instead of F-Fulkerson
# Inspiration taken from info at https://cp-algorithms.com/graph/edmonds_karp.html#implementation
# Thanks Anna for TA-ing this sem!

from collections import deque


def breadth_first_search(network_graph, source_node, sink_node, parent_nodes):
    visited_nodes = [False]*len(network_graph)
    node_q = deque()

    node_q.append(source_node)
    visited_nodes[source_node] = True

    while node_q:
        curr_node = node_q.popleft()

        for index, val in enumerate(network_graph[curr_node]):
            if not visited_nodes[index] and val > 0:
                node_q.append(index)
                visited_nodes[index] = True
                parent_nodes[index] = curr_node

                if index == sink_node:
                    return True

    return False


def edmonds_karp_algo(network_graph, source_node, sink_node):
    parent_nodes = [-1]*len(network_graph)
    max_bandwidth = 0

    while breadth_first_search(network_graph, source_node, sink_node, parent_nodes):
        path_flow = float('Inf')
        temp_node = sink_node
        while(temp_node != source_node):
            path_flow = min(path_flow, network_graph[parent_nodes[temp_node]][temp_node])
            temp_node = parent_nodes[temp_node]

        max_bandwidth += path_flow

        flow_node = sink_node
        while(flow_node != source_node):
            up_node = parent_nodes[flow_node]
            network_graph[up_node][flow_node] -= path_flow
            network_graph[flow_node][up_node] += path_flow
            flow_node = parent_nodes[flow_node]

    return max_bandwidth


def main():
    network_counter = 0

    while True:
        num_nodes = int(input())
        if num_nodes == 0:
            break

        network_counter += 1
        source_node, sink_node, num_connections = map(int, input().split())
        network_graph = [[0]*num_nodes for _ in range(num_nodes)]

        for _ in range(num_connections):
            node1, node2, bandwidth = map(int, input().split())
            network_graph[node1-1][node2-1] += bandwidth
            network_graph[node2-1][node1-1] += bandwidth

        max_bandwidth = edmonds_karp_algo(network_graph, source_node-1, sink_node-1)
        print(f'Network {network_counter}: Bandwidth is {max_bandwidth}.')

if __name__ == "__main__":
    main()

