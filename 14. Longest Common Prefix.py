class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
            """
            
        # Loop through each character index of the first string
        for i in range(len(strs[0])):
            # Compare with the same index character in the other strings
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]