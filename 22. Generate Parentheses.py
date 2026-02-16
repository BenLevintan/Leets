class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_list = []

        def backtrack(current_string, open, closed):
            # Check if all parenthesis are used -> add to list
            if len(current_string) >= 2 * n:
                result_list.append(current_string)
                return

            if open < n:
                backtrack(current_string + "(", open + 1, closed)

            if closed < open:
                backtrack(current_string + ")", open, closed + 1)              
            

        backtrack("", 0, 0)
        return result_list


sol = Solution()
print(sol.generateParenthesis(2))