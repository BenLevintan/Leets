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
        par_list = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                par_list.append(char)

            if char  == ")" or char == "]" or char == "}":
                if not par_list:
                    return False
                else:
                    last_par = par_list.pop()
                if last_par == "(" and char != ")":
                    return False
                elif last_par == "[" and char != "]":
                    return False
                elif last_par == "{" and char != "}":
                    return False
        
        return not par_list

    # Made with GPT - uses dict to keep pairs
    def Pythonic_isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack

    

sol = Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([)]"))
print(sol.isValid("{[}]"))
print(sol.isValid("((("))
print(sol.isValid(")))"))
print(sol.isValid(")("))