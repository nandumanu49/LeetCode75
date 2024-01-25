from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        num_count = {}

        for num in nums:
            complement = k - num

            if complement in num_count and num_count[complement] > 0:
                num_count[complement] -= 1
            else:
                num_count[num] = num_count.get(num, 0) + 1

        # Calculate the average of remaining values
        remaining_values = [key for key, count in num_count.items() for _ in range(count)]
        sum_remaining = sum(remaining_values)
        max_avg = sum_remaining / k if k != 0 else 0  # Avoid division by zero

        return max_avg

sol = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(sol.findMaxAverage(nums, k))
