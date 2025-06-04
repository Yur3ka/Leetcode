class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        curr1 = 0
        curr0 = 0
        l = 0
        for i in range(len(nums)):
            curr1 += 1
            if nums[i] == 1:
                res = max(res,curr1)
            else:
                curr0 += 1
                if curr0 <= k:
                    res = max(res,curr1)
                else:
                    while curr0 > k:
                        if nums[l] == 0:
                            curr0 -= 1
                        curr1 -= 1
                        l += 1
        return res