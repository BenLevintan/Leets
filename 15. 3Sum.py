class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        zero_list = []
        seen = set()  # Set to track unique combinations
        
        # Sort nums first to make it easier to avoid duplicates
        nums.sort()
        
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # To ensure uniqueness, sort the combination and use it as a tuple
                    triplet = tuple([nums[i], nums[left], nums[right]])
                    
                    # Only add to the result if the triplet is not already in the set
                    if triplet not in seen:
                        seen.add(triplet)
                        zero_list.append([nums[i], nums[left], nums[right]])
                    
                    # Move both pointers after finding a valid triplet
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return zero_list
    
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))


# not final, need to solve for unique numbers and not any