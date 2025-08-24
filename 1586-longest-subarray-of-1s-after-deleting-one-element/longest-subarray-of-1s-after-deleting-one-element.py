class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        deleted = 0
        l = 0
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                res = max(res,count-(1-deleted))
            else:
                deleted += 1
                while deleted > 1:
                    if nums[l] == 1:
                        count -= 1
                    else:
                        deleted -= 1
                    l += 1
                res = max(res,count-(1-deleted))
        return res