class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        pos = defaultdict(list)
        for i in range(len(nums)):
            pos[nums[i]].append(i)
        for _,v in pos.items():
            for i in range(len(v)-1):
                for j in range(i+1,len(v)):
                    if (v[i]*v[j])%k == 0:
                        ans += 1
        return ans