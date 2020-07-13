def find_dest(m):

    def travel(r, c):
        if not (r == rows or c == cols or m[r][c] == 1 or memo[r][c]):
            memo[r][c] = 1
            print(f"{[r, c]}")
            if [r, c] == [rows - 1, cols - 1]:
                return True
            return travel(r + 1, c) or travel(r, c + 1)

    if not m:
        return True
    rows = len(m)
    cols = len(m[0])
    memo = []
    for r in range(rows):
        memo.append([])
        for c in range(cols):
            memo[r].append(0)

    if travel(0, 0):
        return True
    return False



# m=[
#     [None, None, None, None, None, 1, 1, None, 1],
#     [None, 1, None, None, 1, None, None, None, None],
#     [None, None, 1, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, 1, None]
# ]
# print(find_dest(m))

# m=[
#     [None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None, None],
# ]
# print(find_dest(m))

m=[
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, 1],
    [None, None, None, None, None, None, None, 1, None],
]
print(find_dest(m))
