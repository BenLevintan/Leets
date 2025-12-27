class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        results = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                # Two-pointer approach for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for left and right pointers
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return results

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))       
print(Solution().fourSum(nums = [2,2,2,2,2], target = 8))  