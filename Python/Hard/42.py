def find_minimum(nums):
 min = nums[0]
 for i in range(1, len(nums)):
    if nums[i] > min:
        min = nums[i]
 return min
