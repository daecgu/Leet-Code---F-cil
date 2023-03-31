def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.

    i = len(nums) -1
    while i >= 0 :
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        i -= 1
        """
    i=0
    j=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums

nums= [0, 3, 5, 6, 0, 5, 8, 0, 0, 1]
moveZeroes(nums)
print(nums)