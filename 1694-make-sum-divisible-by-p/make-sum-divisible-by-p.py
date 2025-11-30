class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0
        
        pre = 0
        seen = {0: -1}
        ans = len(nums)
        
        for i, x in enumerate(nums):
            pre = (pre + x) % p
            tgt = (pre - r) % p   # tìm prefix[i] sao cho prefix[j] - prefix[i] ≡ r
            
            if tgt in seen:
                ans = min(ans, i - seen[tgt])
            
            seen[pre] = i
        
        return ans if ans < len(nums) else -1
        