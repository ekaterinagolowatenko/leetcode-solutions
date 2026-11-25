from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        max_len = 0

        for start in range(len(nums)):
            p = 1
            g = 0
            l = 1

            for end in range(start, len(nums)):
                x = nums[end]

                p *= x
                g = gcd(g, x)
                l = lcm(l, x)

                if p == g * l:
                    max_len = max(max_len, end - start + 1)

        return max_len