class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        largest_area = 0

        while left < right:
            # Calculate the area
            area = (right - left) * min(height[left], height[right])
            largest_area = max(largest_area, area)

            # Move the pointer for the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return largest_area
    
    # Causes time limit exeession 
    def maxAreaNaive(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        largest_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                # Calculate the area
                area = (j - i) * min(height[i], height[j])
                
                if area > largest_area:
                    largest_area = area 
        
        return largest_area

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))