import math
def sequence(nums):
    if len(nums) <= 1:
        return []
    start = 0
    sum = 0
    max_sum = -1 * math.inf
    for end in range(len(nums)):
        sum += nums[end]
        while start < end and sum < 0:
            sum -= nums[start]
            start += 1
        if sum > max_sum:
            max_sum = sum
            i, j = start, end
    return nums[i:j + 1]

print(sequence([-2, -8, -3, -2, -4, -10]))
