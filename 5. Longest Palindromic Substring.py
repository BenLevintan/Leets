class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_pol = s[0]  # Start with at least one character
        
        for i in range(len(s)):
            # Case 1: Even length palindrome
            j1, j2 = i, i + 1
            while j1 >= 0 and j2 < len(s) and s[j1] == s[j2]:
                if (j2 - j1 + 1) > len(max_pol):
                    max_pol = s[j1:j2 + 1]
                j1 -= 1
                j2 += 1

            # Case 2: Odd length palindrome
            j1, j2 = i - 1, i + 1
            while j1 >= 0 and j2 < len(s) and s[j1] == s[j2]:
                if (j2 - j1 + 1) > len(max_pol):
                    max_pol = s[j1:j2 + 1]
                j1 -= 1
                j2 += 1

        return max_pol
    
sol = Solution()
print("test")
print(sol.longestPalindrome("ababda"))