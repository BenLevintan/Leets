class Solution(object):
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


nums = [0,4,3,0]
target = 0
print(Solution().twoSum(nums, target))


# optimized solution:
class Solution(object):
    def twoSum_GPT(self, nums, target):
        # Dictionary to store the value and its index
        seen = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in seen:
                return seen[complement], i
            
            # Store the number and its index in the dictionary
            seen[num] = i