# Problem: Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        result = [0]

        def dfs(node, parent):
            total = values[node]

            for child in adj[node]:
                if child == parent:
                    continue
                total += dfs(child, node)

            if total % k == 0:
                result[0] += 1
                return 0

            return total

        dfs(0, -1)
        return result[0]
