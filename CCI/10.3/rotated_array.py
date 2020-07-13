def rotated_array(nums, num):
    print(f"Searching {nums} for {num}")
    length = len(nums)
    mid = length // 2
    if nums[mid] == num:
        return True
    if length != 1:
        if nums[mid] < nums[length - 1] and num <= nums[length - 1] and num > nums[mid]:
            print(f"Searching {nums[mid:]} for {num}")
            return rotated_array(nums[mid:], num)
        else:
            return rotated_array(nums[:mid], num)

print(rotated_array([10, 21, 3, 4, 5, 6, 8, 9], 8))
