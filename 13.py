#13. Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        total=0
        prev=0
        for i in reversed(s):
            curr=roman_map[i]
            if curr<prev:
                total-=curr
            else:
                total+=curr
            prev=curr
        return total

                     