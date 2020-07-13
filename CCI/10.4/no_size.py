# Broken
def search_no_size(nums, num):
    i = 1
    while nums[i] != -1 and nums[i] < num:
        i *= 2
        print(f"i = {i}")
    return binary_search(nums[i // 2 : i + 1], num)

def binary_search(nums, num):
    length = len(nums)
    mid = length // 2
    if nums[mid] == num:
        return True
    if length != 1:
        if num <= nums[mid]:
            return binary_search(nums[:mid+1], num)
        else:
            return binary_search(nums[mid+1:], num)
    return False


a = [0, 3, 4, 6, 7, 9, 14, 16, 20, 21, 40, 44, 54, 55, -1, -1, -1]
a.extend([-1] * 100)
print(search_no_size(a, 55))
