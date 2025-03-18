class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0,0
        curr = 0
        length = 0
        ans = 0
        while r < n:
            if curr & nums[r] == 0:
                curr = curr ^ nums[r]
                length += 1
                ans = max(ans, length)
                r += 1
            else:
                while curr & nums[r] != 0:
                    curr = curr ^ nums[l]
                    l += 1
                    length -=1
        return ans