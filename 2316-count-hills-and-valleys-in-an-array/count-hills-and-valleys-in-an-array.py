class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nn = []
        for i in range(len(nums)):
            if not nn:
                nn.append(nums[i])
            if nums[i] == nn[-1]:
                continue
            else:
                nn.append(nums[i])
        ans = 0
        for i in range(1,len(nn)-1):
            if nn[i-1]<nn[i]>nn[i+1] or nn[i-1] > nn[i] < nn[i+1]:
                ans += 1
        return ans