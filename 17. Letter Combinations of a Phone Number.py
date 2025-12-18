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

        # Main loop that iterates through each digit in the input string
        for num in digits:
            if num not in t9_mapping:
                print("Invalid input")
                return
            new_results = []
            for message in results:
                for char in t9_mapping[num]:
                    # Concat the new char to the message and add it to the list
                    new_results.append(message + char)
                
            # Replace the values in 'results' (which are n length) with the new combinations (which are all n+1 length)
            results = new_results
        return results
    
print(Solution().letterCombinations("111"))
# print(Solution().letterCombinations("2"))

