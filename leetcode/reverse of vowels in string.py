class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_positions = [i for i, char in enumerate(s) if char in vowels]
        reversed_vowels = [s[i] for i in vowel_positions[::-1]]

        result = ''.join(
            char if char not in vowels else reversed_vowels.pop(0) for char in s
        )

        return result


# Example usage:
sol = Solution()
s = "aA"
result = sol.reverseVowels(s)
print(result)