import collections

DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def solution():
    grid = []
    start_row = curr_row = 0
    start_positions = set()
    with open('input.txt', 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
            start_cols = [i for i, height in enumerate(line) if height == 'a']
            for col in start_cols:
                start_positions.add((curr_row, col))
            if (col := line.rfind('S')) != -1:
                grid[curr_row][col] = 'a'
                start_positions.add((curr_row, col))
            curr_row += 1

    max_row = len(grid)
    max_col = len(grid[0])

    min_path = float('inf')
    for start_row, start_col in start_positions:
        queue = collections.deque([(start_row, start_col, 0)])
        seen = set((start_row, start_col))
        while queue:
            node = queue.popleft()
            row, col, count = node[0], node[1], node[2]
            if grid[row][col] == 'E':
                min_path = min(min_path, count)
                break
            for direction in DIRECTIONS:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row < 0 or new_row == max_row or new_col < 0 or new_col == max_col:
                    continue
                if grid[new_row][new_col] == 'a':
                    continue
                if (new_row, new_col) in seen:
                    continue
                if (grid[new_row][new_col] != 'E' and ord(grid[new_row][new_col]) - ord(grid[row][col]) > 1) or (grid[new_row][new_col] == 'E' and (ord('z') - ord(grid[row][col]) > 1)):
                    continue
                seen.add((new_row, new_col))
                queue.append((new_row, new_col, count + 1))
    return min_path

if __name__ == '__main__':
    print(solution())
