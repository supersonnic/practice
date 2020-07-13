def bubble_sort(nums):
    sorted = False
    length = len(nums) - 1
    while not sorted:
        sorted = True
        for i in range(length):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted = False
    return nums
################################################################################
def better_bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    sorted = False
    length = len(nums) - 1
    while not sorted:
        sorted = True
        i = 0
        while i < length:
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                sorted = False
            i += 1
        length -= 1
    return nums
################################################################################
def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
        nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
################################################################################
def merge_sort(l, r, nums):
    def merge(l, m, r):
        t1, t2 = nums[l:m], nums[m+1:r]
        i, j , k = 0, 0, l
        while i < len(t1) and j < len(t2):
            if t1[i] < t2[j]:
                nums[l] = t1[i]
                i += 1
            else:
                nums[l] = t2[j]
                j += 1
            l += 1
        while i < len(t1):
            nums[l] = t1[i]
            i += 1
            l += 1
        while j < len(t2):
            nums[l] = t2[j]
            j += 1
            l += 1
    if l < r:
        mid = (l+r) // 2
        merge_sort(l, mid, nums)
        merge_sort(mid+1, r, nums)
        merge(l, mid, r)
    return nums
################################################################################
import random
def quick_sort(nums):
    if not nums:
        return
    pivot_index = random.randint(0, len(nums) - 1)
    pivot = nums[pivot_index]
    i, j = 0, len(nums) - 1
    while i != j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    quick_sort(nums[0:i])
    quick_sort(nums[i:])
    return nums
################################################################################
def radix_sort(nums):
    out = []
    for d in range(10):
        for i in range(len(nums)):
            if nums[i] % 10 *  == d:
                out.append(nums[i])
    return out
################################################################################


# print(bubble_sort([i for i in range(3000,0,-1)]))
# better_bubble_sort([i for i in range(3000,0,-1)])
# print(selection_sort([i for i in range(10,0,-1)]))
# print(selection_sort([i for i in range(3000,0,-1)]))
# print(quick_sort([10, 6, 11, 3, 4, 7]))
# quick_sort([i for i in range(3000,0,-1)])
print(radix_sort([98, 10, 13, 11, 22]))
