from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [0] * n

        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product

        # Calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

        # Calculate the final result
        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result

# Example usage:
sol = Solution()
nums = [1, 2, 3, 4]
result = sol.productExceptSelf(nums)
print(result)