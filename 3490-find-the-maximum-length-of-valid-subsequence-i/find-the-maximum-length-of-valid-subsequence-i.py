class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        curr = nums[0]
        even = 0
        odd = 0
        for i in range(1,len(nums)):
            if (nums[i]-curr)%2==1:
                ans += 1
                curr = nums[i]
            if nums[i] %2==0:
                even += 1
            else:
                odd+= 1
        if nums[0] %2==0:
            even+= 1
        else:
            odd += 1
        return max(ans,even,odd)