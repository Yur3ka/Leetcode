class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        up = tops[0]
        down = bottoms[0]
        up_count = 1
        bottom_up_count = 0
        down_count = 1
        up_pos = 1
        down_pos = 1
        up_down_count = 0
        if up == down:
            bottom_up_count+=1
            up_down_count += 1
        for i in range(1,n):
            if tops[i] == up:
                up_count += 1
                up_pos += 1
            if bottoms[i] == up:
                bottom_up_count += 1
                if tops[i] != up:
                    up_count += 1
            if bottoms[i] == down:
                down_count += 1
                down_pos += 1
            if tops[i] == down:
                up_down_count += 1
                if bottoms[i] != down:
                    down_count += 1
        ans = float("inf")
        if up_count != n and down_count !=n:
            return -1
        if up_count == n:
            ans = min(ans,up_pos, n-up_pos,bottom_up_count,n-bottom_up_count)
        if down_count == n:
            ans = min(ans,down_pos,n-down_pos,up_down_count,n-up_down_count)
        # print(n,up_pos,down_pos,up_count,down_count,)
        # print(bottoms.count(1))
        return ans