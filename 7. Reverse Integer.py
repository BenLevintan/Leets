# NOTE: This solutoin requires and artificial limit for 32bit signed intiger 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        # Raise a flag so we remember is the number is negative
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        result = 0
        i = 0

        while x != 0:
            digit = x % 10
            
            # Check for overflow before appending the next digit
            if result > MAX_INT // 10 or (result == MAX_INT // 10 and digit > 7):
                return 0
            
            result = result * 10 + digit
            x //= 10

        if result > abs(MIN_INT):
            return 0        

        # Check if we need to return a positive on negative number
        if is_negative == True:
            return int(result *-1)
        else:
            return int(result)
        
sol = Solution()
print(sol.reverse(-1230))