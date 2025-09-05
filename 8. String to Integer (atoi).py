class Solution(object):
    def myAtoi(self, s):
        i = 0
        num = 0
        n = len(s)
        negative = False

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Handle sign
        if i < n and s[i] == '-':
            negative = True
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Convert digits
        while i < n and s[i] >= '0' and s[i] <= '9':
            digit = int(s[i])
            # Check for overflow before adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MIN if negative else INT_MAX
            num = num * 10 + digit
            i += 1

        return -num if negative else num

    

sol = Solution()
print(sol.myAtoi("   -042"))