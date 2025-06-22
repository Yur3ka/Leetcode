class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        if not s:
            return []
        if n < k:
            return [s +fill*(k-n)]
        else:
            res.append(s[:k])
            return res + self.divideString(s[k:],k,fill)