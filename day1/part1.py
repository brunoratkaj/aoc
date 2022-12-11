

def solution():
    max_cal = 0
    curr = 0
    with open('input1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                curr += int(line)
            else:
                max_cal = max_cal if max_cal > curr else curr
                curr = 0
    print(max_cal)


if __name__ == '__main__':
    solution()





