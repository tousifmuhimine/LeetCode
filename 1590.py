# 1590. Make Sum Divisible by P
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        res = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - rem) % p

            if target in seen:
                res = min(res, i - seen[target])

            seen[prefix] = i

        return res if res < len(nums) else -1
