class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        curr = 0
        for w in word:
            curr = curr*10 + int(w)
            curr %= m
            if curr == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans