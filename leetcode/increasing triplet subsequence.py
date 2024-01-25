from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 3:
            return []

        first = float("inf")
        second = float("inf")

        triplet = []

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                triplet = [first, second, num]
                break

        return triplet

# Example usage:
sol = Solution()
nums = [2, 1, 5, 0, 4, 6]
result = sol.increasingTriplet(nums)
print(result)