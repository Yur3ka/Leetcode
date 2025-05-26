class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        init = min(height[l],height[r])*(r-l)
        while r > l:
            if height[l] > height[r]:
                r -=1
            else:
                l+= 1
            init = max(init,min(height[l],height[r])*(r-l))
        return init