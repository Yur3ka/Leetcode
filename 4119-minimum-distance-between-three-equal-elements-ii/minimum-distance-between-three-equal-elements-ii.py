class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        c = defaultdict(list)
        for i in range(len(nums)):
            c[nums[i]].append(i)
        flag = False
        ans = float('inf')
        for _,v in c.items():
            if len(v) < 3:
                continue
            else:
                flag = True
                for i in range(len(v)-2):
                    temp = v[i+2] - v[i]
                    ans = min(2*temp,ans)
        if not flag:
            return -1
        return ans