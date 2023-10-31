# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Coding Quandary 17

import heapq
import sys

def dijkstra(maze, start, rows, cols):
    directions = [(1,1,2), (-1,-1,2), (1,-1,2), (-1,1,2), (0,1,1), (1,0,1), (0,-1,1), (-1,0,1)]
    visited = [[False]*cols for _ in range(rows)]
    costs = [[float('inf')]*cols for _ in range(rows)]
    paths = [[-1]*cols for _ in range(rows)]
    costs[start[0]][start[1]] = 0
    paths[start[0]][start[1]] = [start[0]*cols + start[1]]
    heap = [(0, len(paths[start[0]][start[1]]), start, paths[start[0]][start[1]])]  # add length of path to heap

    while heap:
        current_cost, _, current_cell, path = heapq.heappop(heap)  # ignore path length here
        if visited[current_cell[0]][current_cell[1]]:
            continue
        visited[current_cell[0]][current_cell[1]] = True
        for dx, dy, d_cost in directions:
            new_x, new_y = current_cell[0] + dx, current_cell[1] + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y] and maze[new_x][new_y] != '1':
                new_cost = current_cost + d_cost
                if new_cost < costs[new_x][new_y]:
                    costs[new_x][new_y] = new_cost
                    new_path = path + [new_x*cols + new_y]
                    paths[new_x][new_y] = new_path
                    heapq.heappush(heap, (new_cost, len(new_path), (new_x, new_y), new_path))  # push length of path to heap
    return costs, paths

def main():
    while True:
        rows, cols = map(int, sys.stdin.readline().split())
        if rows == cols == 0: break
        maze = []
        ends = []
        for r in range(rows):
            row = sys.stdin.readline().split()
            maze.append(row)
            for c in range(cols):
                if row[c] == 'S':
                    start = (r,c)
                elif row[c] == 'E':
                    ends.append((r,c))
        costs, paths = dijkstra(maze, start, rows, cols)
        min_cost = min(costs[end[0]][end[1]] for end in ends)
        if min_cost == float('inf'):
            print("Cost: 0 Path: None")
        else:
            min_path = min((paths[end[0]][end[1]] for end in ends if costs[end[0]][end[1]] == min_cost), key=lambda path: path[-1])
            print("Cost:", min_cost, "Path:", " ".join(str(cell) for cell in min_path))

if __name__ == "__main__":
    main()
