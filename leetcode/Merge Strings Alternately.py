class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result += word1[i] + word2[i]

        # If one word is longer than the other, add the remaining characters
        result += word1[min_len:] + word2[min_len:]

        return result


# Example usage:
sol = Solution()
word1 = "abc"
word2 = "pqr"
merged_result = sol.mergeAlternately(word1, word2)
print(merged_result)