# import sys
# sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    count = int(input())
    flat_lst = list(map(int, input().split()))
    while count > 0:
        max_index = flat_lst.index(max(flat_lst))
        min_index = flat_lst.index(min(flat_lst))
        flat_lst[max_index] -= 1
        flat_lst[min_index] += 1
        count -= 1
        if max(flat_lst) - min(flat_lst) == 1 or max(flat_lst) - min(flat_lst) == 0:
            print('#{} {}'.format(test_case, max(flat_lst) - min(flat_lst)))
            break
    print('#{} {}'.format(test_case, max(flat_lst) - min(flat_lst)))