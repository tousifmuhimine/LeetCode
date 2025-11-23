# ------------------------------------------------------------
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
#
# Summary:
# Given an array of integers `nums` and an integer `target`,
# return indices of the two numbers such that they add up to `target`.
# Each input has exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Approach:
# Brute-force / Nested loop:
# - Loop through each element in the array.
# - For each element, loop through the remaining elements.
# - Return the indices immediately when a pair sums to the target.
# ------------------------------------------------------------

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []