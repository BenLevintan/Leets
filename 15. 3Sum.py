class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        zero_list = []
        

        for i in nums:
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                        zero_list.append([nums[i] ,nums[j] ,nums[k]])

        return zero_list
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))