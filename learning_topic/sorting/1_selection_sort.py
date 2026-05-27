def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:   # Ascending order
            # if nums[j] > nums[min_idx]:     # Descending order
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums



# Drive code
nums = [4,7,1,8,2,5,9,3]
print(selection_sort(nums))


# Time Complexity: O(N^2)
# Space Complexity: O(1)