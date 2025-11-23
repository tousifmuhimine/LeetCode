# ------------------------------------------------------------
# Problem: Greatest Sum Divisible by Three
# Link: https://leetcode.com/problems/greatest-sum-divisible-by-three/
#
# Summary:
# Given an integer array, choose elements to maximize the sum
# such that the total sum is divisible by 3.
#
# Approach:
# Greedy strategy:
# - Compute total sum
# - Track numbers by remainder (1 and 2)
# - If total % 3 != 0, remove the smallest necessary value(s)
#   to make the sum divisible by 3
# ------------------------------------------------------------

class Solution(object):
    def maxSumDivThree(self, nums):
        total = sum(nums)

        # Lists for numbers by remainder
        r1 = []
        r2 = []

        for n in nums:
            if n % 3 == 1:
                r1.append(n)
            elif n % 3 == 2:
                r2.append(n)

        r1.sort()
        r2.sort()

        if total % 3 == 0:
            return total

        ans = 0
        if total % 3 == 1:
            # Option 1: remove smallest remainder-1
            option1 = total - (r1[0] if len(r1) >= 1 else float('inf'))
            # Option 2: remove two smallest remainder-2
            option2 = total - (r2[0] + r2[1] if len(r2) >= 2 else float('inf'))
            ans = max(option1, option2)
        else:  # total % 3 == 2
            # Option 1: remove smallest remainder-2
            option1 = total - (r2[0] if len(r2) >= 1 else float('inf'))
            # Option 2: remove two smallest remainder-1
            option2 = total - (r1[0] + r1[1] if len(r1) >= 2 else float('inf'))
            ans = max(option1, option2)

        return ans if ans != float('inf') else 0
