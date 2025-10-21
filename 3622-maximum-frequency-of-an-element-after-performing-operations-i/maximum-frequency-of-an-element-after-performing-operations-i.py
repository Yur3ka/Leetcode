class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        f = defaultdict(int)
        nums.sort()
        for i in range(len(nums)):
            f[nums[i]]+= 1
        ans = -float('inf')
        for i in range(nums[0],nums[-1]+1):
                l = bisect_left(nums,i-k)
                r = bisect_right(nums,i+k)
                m = f[i]
                ans = max(ans,min(m+numOperations,r-l))
            # print(ans,m+numOperations,l-r)
        return ans