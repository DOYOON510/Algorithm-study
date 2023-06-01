T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    array = [[0] * n for i in range(n)]
    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    row, col = 0, 0
    dist = 0
    for i in range(1, n * n + 1):
        array[row][col] = i
        row += dr[dist]
        col += dc[dist]
        if row < 0 or col < 0 or row >= n or col >= n or array[row][col] != 0:
            row -= dr[dist]
            col -= dc[dist]

            dist = (dist + 1) % 4
            row += dr[dist]
            col += dc[dist]
    print('#{}'.format(test_case))
    for i in array:
        print(*i)