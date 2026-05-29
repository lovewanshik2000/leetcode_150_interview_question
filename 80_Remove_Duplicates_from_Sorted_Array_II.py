def removeDuplicates(nums):
        n = len(nums)
        if n <= 2:
            return n
        k = 2
        for i in range(2,n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k

# Drive code
nums = [1,1,1,2,2,3]    # Output: 5

print(removeDuplicates(nums))