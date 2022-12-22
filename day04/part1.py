def solution():
    with open('input.txt', 'r') as file:
        count = 0
        for line in file:
            sec1, sec2 = line.split(',')
            x1, y1 = list(map(int, sec1.split('-')))
            x2, y2 = list(map(int, sec2.split('-')))
            if x1 <= x2:
                if y1 >= y2:
                    count += 1
                    continue
            if x1 >= x2:
                if y1 <= y2:
                    count += 1
        print(count)

if __name__ == '__main__':
    solution()
