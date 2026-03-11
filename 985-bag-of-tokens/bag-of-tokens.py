class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        point = 0
        tokens.sort()
        l,r = 0, len(tokens)-1
        while l <= r:
            move = False
            if tokens[l] <= power:
                point += 1
                power -= tokens[l]
                ans = max(ans,point)
                l += 1
                move = True
            elif tokens[l] > power and point > 0:
                point -= 1
                power += tokens[r]
                r -= 1
                move = True
            if not move:
                break
        return ans