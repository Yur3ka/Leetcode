class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = 2**(len(nums))-1
        cache = [0]*(n+1)
        maxx = 0
        ans = 0
        for number in nums:
            maxx |= number
        for i in range(n+1):
            for j in range(len(nums)):
                if i ^ (1 << j) == 0:
                    cache[i] = nums[j]
                    break
                elif i & (1 << j) != 0:
                    cache[i] = cache[i^(1<<j)] | nums[j]
                    break
            if cache[i] == maxx:
                    ans += 1
        return ans