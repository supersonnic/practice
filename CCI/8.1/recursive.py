def num_ways(n, ways):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if ways[n]:
        return ways[n]
    temp = num_ways(n-1, ways) + num_ways(n-2, ways) + num_ways(n-3, ways)
    ways[n] = temp
    return temp

print(num_ways(200, [None for i in range(201)]))
