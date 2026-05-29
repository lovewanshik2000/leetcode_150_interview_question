def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j >=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    # return nums

# Driver code
nums = [5,6,2,4,8,7,3,1]
# Sort nums in place by calling insertion_sort function
insertion_sort(nums)
print("Output: ", nums)


# Time Complexity: O(N^2)
# Space Complexity: O(1)