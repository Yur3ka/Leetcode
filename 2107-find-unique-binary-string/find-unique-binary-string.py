class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums[0])
        n = 2**length

        nums = set(nums)
        for i in range(n):
            bin_i = str(bin(i))[2:]
            bin_i = "0"*(length-len(bin_i)) + bin_i
            if bin_i not in nums:
                return bin_i