from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                # Swap the non-zero element with the element at non_zero_index
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                # Move the non_zero_index to the next position
                non_zero_index += 1


# Example usage:
sol = Solution()

nums1 = [0, 1, 0, 3, 12]
sol.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
sol.moveZeroes(nums2)
print(nums2)  # Output: [0]
