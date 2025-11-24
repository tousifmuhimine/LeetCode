# ------------------------------------------------------------
# Problem: Binary Prefix Divisible By 5
# Link: https://leetcode.com/problems/binary-prefix-divisible-by-5/
#
# Summary:
# You are given a binary array nums. For each prefix nums[0..i],
# interpret it as a binary number xi, and determine whether xi
# is divisible by 5. Return a list of booleans representing this.
#
# Approach:
# - Maintain a running value "current" that stores xi % 5.
# - For each new bit, update using: current = (current * 2 + bit) % 5
# - If current == 0, the number is divisible by 5.
# - This avoids constructing large numbers and runs in O(n).
# ------------------------------------------------------------

from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current = 0

        for bit in nums:
            current = (current * 2 + bit) % 5
            result.append(current == 0)

        return result
