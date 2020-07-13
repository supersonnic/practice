# We need to find the longest distance between a 0 and a 1. Each degree of
# separation represents and hour. So (max_distance * 1 hour) is the minimum
# wait time.
def minimumHours(rows, columns, grid):

    def find_distance(r, c, count):
        if c < columns - 1:
            if grid[r][c + 1]:
                return count + 1
            return find_distance(r, c + 1, count + 1)
        return -1

    max_distance = 0
    for r in range(rows):
        for c in range(columns):
            if not grid[r][c]:
                count = 0
                # max_distance = max(find_distance(r, c, count), max_distance)
                print(find_distance(r, c, count))
    return max_distance

print(minimumHours(3, 4, [[0, 0, 0, 1],[1, 1, 1, 1],[1, 1, 1, 1]]))
