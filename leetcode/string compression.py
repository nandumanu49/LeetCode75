from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        def int_to_chars(num):
            if num == 1:
                return []
            else:
                return list(str(num))

        write_index = 0
        read_index = 0

        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0

            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1

            chars[write_index] = current_char
            write_index += 1

            compressed_count = int_to_chars(count)
            for digit in compressed_count:
                chars[write_index] = digit
                write_index += 1

        return write_index


# Example usage:
sol = Solution()

chars1 = ["a", "a", "b", "b", "c", "c", "c"]
result1 = sol.compress(chars1)
print(result1, chars1[:result1])

chars2 = ["a"]
result2 = sol.compress(chars2)
print(result2, chars2[:result2])

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
result3 = sol.compress(chars3)
print(result3, chars3[:result3])