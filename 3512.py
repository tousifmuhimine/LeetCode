#3512. Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)%k==0:
            return 0
        count=0
        for i in range(len(nums)):
            if nums[i]!=k:
                while sum(nums)%k!=0:
                    nums[i]=nums[i]-1
                    count += 1
        return count
