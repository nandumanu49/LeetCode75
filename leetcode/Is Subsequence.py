class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers for both strings
        s_ptr, t_ptr = 0, 0

        # Iterate through the characters of both strings
        while s_ptr < len(s) and t_ptr < len(t):
            # If the characters match, move the s_ptr to the next character in s
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            # Move the t_ptr to the next character in t in any case
            t_ptr += 1

        # If s_ptr reached the end of s, then s is a subsequence of t
        return s_ptr == len(s)

# Example usage:
sol = Solution()

s1, t1 = "abc", "ahbgdc"
print(sol.isSubsequence(s1, t1))

s2, t2 = "axc", "ahbgdc"
print(sol.isSubsequence(s2, t2))