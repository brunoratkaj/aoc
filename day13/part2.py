import ast
import itertools

TWO_IDX = 0
SIX_IDX = 0

def compare_pairs(list1, list2):
    if isinstance(list1, int) and isinstance(list2, list):
        list1 = [list1]
    elif isinstance(list1, list) and isinstance(list2, int):
        list2 = [list2]

    if isinstance(list1, int) and isinstance(list2, int):
        if list1 > list2:
            return -1
        if list1 == list2:
            return 0
        return 1

    if isinstance(list1, list) and isinstance(list2, list):
        ans = 1
        for el1, el2 in zip(list1, list2):
            ans = compare_pairs(el1, el2)
            if ans == 1:
                return 1
            if ans == -1:
                return -1
        
        if len(list1) > len(list2):
            return -1
        elif len(list1) == len(list2):
            return 0
        return 1


def sort_lists(ans):
    global TWO_IDX, SIX_IDX
    size = len(ans)
    for i in range(size):
        for j in range(0, size-i-1):
            is_right_order = compare_pairs(ans[j], ans[j + 1])
            if is_right_order == -1:
                ans[j], ans[j + 1] = ans[j + 1], ans[j]
                if ans[j] == [[2]]:
                    TWO_IDX = j
                elif ans[j + 1] == [[2]]:
                    TWO_IDX = j + 1
                if ans[j] == [[6]]:
                    SIX_IDX = j
                elif ans[j + 1] == [[6]]:
                    SIX_IDX = j + 1
                



def solution():
    with open('input.txt', 'r') as file:
        curr_indice = 1
        sum_indices = 0
        ans = []
        while True:
            list1 = ast.literal_eval(file.readline().strip())
            list2 = ast.literal_eval(file.readline().strip())
            line3 = file.readline()

            ans.append(list1)
            ans.append(list2)

            if not line3:
                break
    
    sort_lists(ans)
    print((TWO_IDX + 1) * (SIX_IDX + 1))


if __name__ == '__main__':
    solution()
