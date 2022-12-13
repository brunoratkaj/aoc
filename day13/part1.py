import ast


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


def solution():
    with open('input.txt', 'r') as file:
        curr_indice = 1
        sum_indices = 0
        while True:
            list1 = ast.literal_eval(file.readline().strip())
            list2 = ast.literal_eval(file.readline().strip())
            line3 = file.readline()

            is_right_order = compare_pairs(list1, list2)
            if is_right_order == 1:
                sum_indices += curr_indice

            if not line3:
                break

            curr_indice += 1
    print(sum_indices)

if __name__ == '__main__':
    solution()
