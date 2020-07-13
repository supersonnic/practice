def find_dest(m):
    if not m:
        return True
    rows = len(m)
    cols = len(m[0])
    queue = [[0,0]]
    while queue:
        current = queue.pop(0)
        print(current)
        r, c = current[0], current[1]
        if current == [rows - 1, cols - 1]:
            return True
        if m[r][c] is None:
            if c + 1 < cols:
                if m[r][c + 1] is None:
                    queue.append([r, c + 1])
            if r + 1 < rows:
                if m[r + 1][c] is None:
                    queue.append([r + 1, c])
    return False

m=[
    [None, None, None, None, None, 1, 1, None, 1],
    [None, 1, None, None, 1, None, None, None, None],
    [None, None, 1, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 1, None]
]
print(find_dest(m))

m=[
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
]
print(find_dest(m))
