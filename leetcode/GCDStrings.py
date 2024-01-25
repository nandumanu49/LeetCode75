class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        # Ensure str1 is the longer string
        if len1 < len2:
            str1, str2 = str2, str1
            len1, len2 = len2, len1

        # Check all possible substrings of str2
        for i in range(len2, 0, -1):
            substring = str2[:i]
            if str1[:i] == substring and str2[:i] == substring and \
               str1.count(substring) * substring == str1 and \
               str2.count(substring) * substring == str2:
                return substring

        return ""

# Example usage:
sol = Solution()
str1 = "ABABAB"
str2 = "ABAB"
result = sol.gcdOfStrings(str1, str2)
print(result)  # Output: "AB"
