class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        numCols = len(s)
        mat = [[None for _ in range(numCols)] for _ in range(numRows)]

        i = 0  # index in s
        row, col = 0, 0

        while i < len(s):
            # Go vertically down
            for row in range(numRows):
                if i >= len(s):
                    break
                mat[row][col] = s[i]
                i += 1
            row -= 1  # last row index

            # Go diagonally up-right
            for step in range(numRows - 2):
                if i >= len(s):
                    break
                row -= 1
                col += 1
                mat[row + 1][col] = s[i]
                i += 1

            col += 1  # next vertical block

        Solution.print_matrix(mat)

        # Build result string
        result = ''
        for r in range(numRows):
            for c in range(numCols):
                if mat[r][c] is not None:
                    result += mat[r][c]

        return result
    
    def print_matrix(mat):
        for row in mat:
            print(''.join(c if c is not None else '.' for c in row))
        print()  


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))

# Best solition:

# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1 or numRows >= len(s):
#             return s
# 
#         L = [''] * numRows
#         index, step = 0, 1
# 
#         for x in s:
#             L[index] += x
#             if index == 0:
#                 step = 1
#             elif index == numRows -1:
#                 step = -1
#             index += step
# 
#         return ''.join(L)