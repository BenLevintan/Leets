class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        t9_mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }
        results = [""]

        for num in digits:
            new_results = []
            for message in results:
                for char in t9_mapping[num]:
                    new_results.append(message + char)
                
            results = new_results
        return results
    
print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("2"))

