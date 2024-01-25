from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies among the kids
        max_candies = max(candies)

        # Check if each kid, with extra candies, can have the maximum number of candies
        result = [candy + extraCandies >= max_candies for candy in candies]

        return result


sol = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
result = sol.kidsWithCandies(candies, extraCandies)
print(result)
