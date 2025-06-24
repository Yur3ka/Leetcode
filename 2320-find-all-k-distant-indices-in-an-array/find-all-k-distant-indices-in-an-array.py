class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                low = max(l,i-k)
                high = min(len(nums),i+k+1)
                for j in range(low,high):
                    res.append(j)
                l = high
        return res
