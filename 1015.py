# Problem: Smallest Repunit Divisible by K
# Link: https://leetcode.com/problems/smallest-repunit-divisible-by-k/
# Explanation:
# We build numbers like 1, 11, 111... using remainder logic.
# If k is divisible by 2 or 5, no such repunit can divide it.
# Otherwise, keep adding '1' until remainder becomes 0.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length

        return -1
