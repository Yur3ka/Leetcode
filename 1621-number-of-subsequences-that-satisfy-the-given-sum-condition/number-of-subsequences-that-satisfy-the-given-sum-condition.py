class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9+7
        ans = 0
        l,r = 0, 0
        if nums[0] * 2 > target:
            return 0
        for i in range(len(nums)):
            if nums[i] + nums[0] > target:
                break
            r = i
        power_of2 = [1]*(r+2)
        for i in range(1,r+2):
            power_of2[i] = (power_of2[i-1]*2)%MOD
        while l <= r:
            if nums[l] * 2 > target:
                break
            while nums[l] + nums[r] > target:
                r-=1
            step = r-l
            ans += power_of2[step]
            ans %= MOD
            l+=1
        return ans
            
