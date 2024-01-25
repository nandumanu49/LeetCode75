from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1

        return count >= n

# Example usage:
sol = Solution()
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
result1 = sol.canPlaceFlowers(flowerbed1, n1)
print(result1)

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
result2 = sol.canPlaceFlowers(flowerbed2, n2)
print(result2)
