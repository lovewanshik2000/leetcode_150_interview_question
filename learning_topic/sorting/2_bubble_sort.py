# Bubble Sort (Adjacent swaps)

def bubble_sort(nums):

    n = len(nums)

    for i in range(n-2, -1,-1):
        is_swap = False
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            return nums, is_swap
    return nums, is_swap


# Driver Code
nums = [5,2,7,3,6,1,4,8,9,0]
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     # Best Case O(N)
print(bubble_sort(nums))

# Time Complexity: O(N^2) for AVG/Worst case but Best Case O(N)
# Space Complexity: O(1)