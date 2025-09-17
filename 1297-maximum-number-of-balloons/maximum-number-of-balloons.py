class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # ans = float('inf')
        c = Counter(text)
        for char in ['b','a','l','n','o']:
            if char not in c:
                return 0
        ans = min(c['b'],c['a'],c['n'],c['l']//2,c['o']//2)
        return ans