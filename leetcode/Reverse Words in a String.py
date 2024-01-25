class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse_words = ' '.join(words[::-1])
        return reverse_words

sol = Solution()
s = "the sky is blue"
result = sol.reverseWords(s)
print(result)