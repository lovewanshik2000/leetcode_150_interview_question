def removeDuplicates(nums):
    if not nums:
        return nums
    n = len(nums)
    k = 1

    for i in range(1,n):
        if nums[i] != nums[k-1]:
            nums[k] = nums[i]
            k += 1
    return k

# Driver code
nums = [0,0,1,1,1,2,2,3,3,4]        # Output: 5
print(removeDuplicates(nums))