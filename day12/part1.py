import collections

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def solution():
    grid = []
    start_row = curr_row = 0
    start_col = 0
    with open('input.txt', 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
            if (curr_col := line.rfind('S')) != -1:
                start_row = curr_row
                start_col = curr_col
                grid[start_row][start_col] = 'a'
            curr_row += 1

    max_row = len(grid)
    max_col = len(grid[0])
    queue = collections.deque([(start_row, start_col, 0)])
    seen = set((start_row, start_col))
    while queue:
        node = queue.popleft()
        row, col, count = node[0], node[1], node[2]
        if grid[row][col] == 'E':
            return count
        for direction in DIRECTIONS:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or new_row == max_row or new_col < 0 or new_col == max_col:
                continue
            if (new_row, new_col) in seen:
                continue
            if (grid[new_row][new_col] != 'E' and ord(grid[new_row][new_col]) - ord(grid[row][col]) > 1) or (grid[new_row][new_col] == 'E' and (ord('z') - ord(grid[row][col]) > 1)):
                continue
            seen.add((new_row, new_col))
            queue.append((new_row, new_col, count + 1))


if __name__ == '__main__':
    print(solution())
