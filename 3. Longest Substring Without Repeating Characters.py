class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        max_substring = ""
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            
            # Update max_substring if we found a longer one
            if (right - left + 1) > len(max_substring):
                max_substring = s[left:right + 1]
        
        return len(max_substring)
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: "abc"
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: "b"
print(sol.lengthOfLongestSubstring("wpwdkewzxcvasdfqwer"))    # Output: "wke"