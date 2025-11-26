# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Description:
# Given a string s, find the length of the longest substring without duplicate characters.
# Uses a sliding window approach with a set to track characters in the current substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0  # left pointer of sliding window
        longest = 0  # length of the longest substring found
        
        for right in range(len(s)):  # right pointer of sliding window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest