class Solution(object):
    def threeSumClosestNaive(self, nums, target):
        """
        this is the naive solution with O(n^3) time complexity - exeeds time limit
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        closest_sum = float('inf')

        for i in range(len(sorted_nums) - 2):
            for j in range(i + 1, len(sorted_nums) - 1):
                for k in range(j + 1, len(sorted_nums)):
                    if abs(target - (sorted_nums[i] + sorted_nums[j] + sorted_nums[k])) < abs(target - closest_sum):
                        closest_sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

        return closest_sum
    

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        



sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
print(sol.threeSumClosest([0, 1, 2], 3))        # Output: 3
print(sol.threeSumClosest([1, 1, 1, 0], -100))  # Output: 2
print(sol.threeSumClosest([1, 2, 5, 10, 11], 12))  # Output: 13
print(sol.threeSumClosest([-3, -2, -5, 3, -4], -1))  # Output: -2
print(sol.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # Output: -2