import heapq


def solution():
    h = []
    curr = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                curr += int(line)
            else:
                if len(h) < 3:
                    heapq.heappush(h, curr)
                else:
                    if curr > h[0]:
                        heapq.heappop(h)
                        heapq.heappush(h, curr)
                curr = 0
    print(sum(h))


if __name__ == '__main__':
    solution()
