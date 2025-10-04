class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check if negative
        if x < 0:
            return False
        
        reverse = 0
        temp = x

        # Create a reverse value of x
        while temp > 0:
            reverse += temp % 10
            reverse *= 10
            temp //= 10

        # Compare and return
        if reverse // 10 == x:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome(121))