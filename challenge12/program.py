# Name: Chanwoo Ray Bae
# Course: Coding Quandaries
# Quandary 12

def find_minimum_kakamora_and_path(grid, grid_size):
    dp_table = [[float("inf")] * grid_size for _ in range(grid_size)]
    movement_trace = [[None] * grid_size for _ in range(grid_size)]

    dp_table[0][0] = grid[0][0]

    for row in range(grid_size):
        for col in range(grid_size):
            # Horizontal
            if col > 0 and dp_table[row][col] > dp_table[row][col-1] + grid[row][col]:
                dp_table[row][col] = dp_table[row][col-1] + grid[row][col]
                movement_trace[row][col] = (row, col-1)

            # Vertical
            if row > 0 and dp_table[row][col] > dp_table[row-1][col] + grid[row][col]:
                dp_table[row][col] = dp_table[row-1][col] + grid[row][col]
                movement_trace[row][col] = (row-1, col)

            # Diagonal
            if row > 0 and col > 0 and dp_table[row][col] > dp_table[row-1][col-1] + grid[row][col]:
                dp_table[row][col] = dp_table[row-1][col-1] + grid[row][col]
                movement_trace[row][col] = (row-1, col-1)

    return reconstruct_path(grid, movement_trace, grid_size), dp_table[grid_size-1][grid_size-1]


def reconstruct_path(grid, movement_trace, grid_size):
    row, col = grid_size - 1, grid_size - 1
    path = []
    while (row, col) != (0, 0):
        path.append(grid[row][col])
        row, col = movement_trace[row][col]
    
    path.append(grid[0][0])
    return path[::-1]


def main():
    while True:
        grid_size = int(input())
        if grid_size == 0:
            break

        grid = [list(map(int, input().split())) for _ in range(grid_size)]

        path, min_kakamora = find_minimum_kakamora_and_path(grid, grid_size)

        print(min_kakamora)
        print(' '.join(map(str, path)))


if __name__ == "__main__":
    main()

