class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i1 = 0
        i2 =0
        arr = []

        # Unite both arrays to one sorted array (ascending)
        while i1 + i2 < len(nums1) + len(nums2):
            if i1 >= len(nums1):
                arr.append(nums2[i2])
                i2 += 1
            elif i2 >= len(nums2):
                arr.append(nums1[i1])
                i1 += 1
            elif nums1[i1] < nums2[i2]:  # <-- fix is here
                arr.append(nums1[i1])
                i1 += 1
            else:
                arr.append(nums2[i2])
                i2 += 1

        # Calculate and return the meadian
        if len(arr) % 2 == 0:
            return ( arr[len(arr) // 2 - 1] + arr[len(arr) // 2] ) / 2   # returned int if used 2 instead of 2.0 (but only on leetcode)
        else:
            return arr[len(arr) // 2]
        

    # Optimized version with no joint array
    def findMedianSortedArrays2(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition for nums1
            j = half - i             # partition for nums2
            
            # Edge cases: if partition is 0 or at the end
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Valid partition
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return min(right1, right2)
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1


sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))