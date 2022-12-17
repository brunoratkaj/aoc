
def snowflake_drop(row, col, max_row, max_col, cave):
    if cave[row + 1 ][col] != '#':
        return snowflake_drop(row + 1, col, max_row, max_col, cave)
    elif col - 1 >= 0 and cave[row + 1][col - 1] != '#':
        return snowflake_drop(row + 1, col - 1, max_row, max_col, cave)
    elif col + 1 <= max_col and cave[row + 1][col + 1] != '#':
        return snowflake_drop(row + 1, col + 1, max_row, max_col, cave)
    else:
        cave[row][col] = '#'
        return
    

def solution():
    max_row = max_col = float('-inf')
    min_row = min_col = float('inf')
    with open('input.txt', 'r') as file:
        coordinates = []
        for idx, line in enumerate(file):
            coordinates.append([])
            line = line.strip().split(' -> ')
            for i, coord in enumerate(line):
                coord = list(map(int, coord.split(',')))
                max_row = max(max_row, coord[1])
                max_col = max(max_col, coord[0])
                min_row = min(min_row, coord[1])
                min_col = min(min_col, coord[0])
                line[i] = coord
            coordinates[idx] = line

    cave = []
    max_row += 2
    max_col *= 2
    for i in range(max_row + 1):
        cave.append([])
        for j in range(max_col + 1):
            if i == max_row:
                cave[i].append('#')
            else:
                cave[i].append('.')

    for rock_line in coordinates:
        for idx in range(len(rock_line) - 1):
            if rock_line[idx][0] == rock_line[idx + 1][0]:
                add = 1 if (rock_line[idx][1] - rock_line[idx + 1][1] < 0) else -1
                for y in range (rock_line[idx][1], rock_line[idx + 1][1] + add, add):
                    cave[y][rock_line[idx][0]] = '#'
            else:
                add = 1 if (rock_line[idx][0] - rock_line[idx + 1][0] < 0) else -1
                for x in range (rock_line[idx][0], rock_line[idx + 1][0] + add, add):
                    cave[rock_line[idx][1]][x] = '#'

    count = 0
    while True:
        if cave[0][500] == '#':
            break
        else:
            snowflake_drop(0, 500, max_row, max_col, cave)
            # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in cave]))
            count += 1
    print(count)

if __name__ == '__main__':
    solution()
