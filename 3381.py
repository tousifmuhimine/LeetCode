# Problem: Maximum Subarray Sum With Length Divisible by K
# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
#
# Approach:
# Use prefix sums grouped by index mod k.
# For each prefix, subtract the smallest previous prefix with the same mod.

class Solution:
    def maxSubArrayWithLengthDivisibleByK(self, nums, k):
        prefix = 0
        best = float('-inf')

        # min prefix for each modulo group
        min_pref = {i: float('inf') for i in range(k)}
        min_pref[0] = 0  # prefix before starting

        for i, x in enumerate(nums):
            prefix += x
            mod = (i + 1) % k

            best = max(best, prefix - min_pref[mod])
            min_pref[mod] = min(min_pref[mod], prefix)

        return best
