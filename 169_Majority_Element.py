def majorityElement(nums):
        # n = len(nums)
        # m = n//2
        # has_map = {}
        # for i in range(0, n):
        #     if nums[i] in has_map:
        #         has_map[nums[i]] += 1
        #     else:
        #         has_map[nums[i]] = 1

        # for key, val in has_map.items():
        #     if val > m:
        #         return key        # Time: O(N)  Space: O(N)

        item = None
        count = 0
        for i in nums:
            if count == 0:
                item = i
            if i == item:
                count += 1
            else:
                count -= 1
        return item         # Time: O(N)  Space: O(1)

# Drive Code
nums = [2,2,1,1,1,2,2]      # Output: 2
print(majorityElement(nums))