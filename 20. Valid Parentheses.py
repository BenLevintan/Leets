# Basic idea: Use a stack stracture. 
# for each char in the string:
#   if it an open parenthesses:
#       add said parenthesses to the stack
#   otherwise:
#       if the coresponding open parenthesses from the stack:
#           remove said parenthesses
#       else:
#           return false
# if stack is empty: retrun true

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        