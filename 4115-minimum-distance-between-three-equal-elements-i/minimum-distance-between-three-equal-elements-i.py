class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        c = defaultdict(list)
        for i in range(len(nums)):
            c[nums[i]].append(i)
        
        hasG = False
        ans = float('inf')
        def minDis(a,b,c):
            return abs(a-b) + abs(a-c) + abs(b-c)
        
        for _,v in c.items():
            if len(v) < 3:
                continue
            hasG = True
            for i in range(0, len(v)-2):
                temp = minDis(v[i], v[i+1], v[i+2])
                ans = min(ans,temp)
        if not hasG:
            return -1
        return ans