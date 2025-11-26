# LeetCode Problem 2435: Paths in Matrix Whose Sum Is Divisible by K
# Link: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
# 
# Problem Summary:
# Given an m x n grid and an integer k, count the number of paths from (0,0) 
# to (m-1,n-1) moving only down or right such that the sum of the path % k == 0.
# Return the count modulo 10^9 + 7.

from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j] % k
                for r in range(k):
                    prev_r = (r - val) % k
                    if i > 0:
                        dp[i][j][r] += dp[i-1][j][prev_r]
                    if j > 0:
                        dp[i][j][r] += dp[i][j-1][prev_r]
                    dp[i][j][r] %= MOD

        return dp[m-1][n-1][0]
