class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        c = 0
        for char in s:
            if char == letter:
                c += 1
        return floor(c*100/n)