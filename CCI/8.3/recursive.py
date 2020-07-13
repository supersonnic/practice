def magic_index(a):
    def travel(start, end):
        if not start > end:
            mid = (end + start) // 2
            if a[mid] == mid:
                return mid
            if a[mid] > mid:
                return travel(start, mid-1)
            else:
                return travel(mid+1, end)

    res = travel(0, len(a) - 1)
    if res is not None:
        return res

print(magic_index([12, 13, 14, 15, 16, 17]))
print(magic_index([0, 2, 4, 5, 6, 7, 33]))
print(magic_index([-4, 1, 12, 32, 42, 52]))
print(magic_index([-1, 0, 1, 2, 3, 5]))
