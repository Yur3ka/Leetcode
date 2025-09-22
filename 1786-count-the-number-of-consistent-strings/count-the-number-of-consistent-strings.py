class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al = set(allowed)
        ans = len(words)
        for word in words:
            for char in word:
                if char not in al:
                    ans -= 1
                    break
        return ans