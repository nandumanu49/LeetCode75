class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)

        # Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Iterate through the remaining subarrays
        for i in range(k, n):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        # Calculate the maximum average
        max_avg = max_sum / k

        return max_avg

# Example usage:
sol = Solution()
nums1 = [1, 12, -5, -6, 50, 3]
k1 = 4
print(sol.findMaxAverage(nums1, k1))  # Output: 12.75

nums2 = [5]
k2 = 1
print(sol.findMaxAverage(nums2, k2))  # Output: 5.0

