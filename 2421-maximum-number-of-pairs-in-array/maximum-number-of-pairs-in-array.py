class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        pair = 0
        n = len(nums)
        for k,v in c.items():
            pair += v//2
        return [pair,n-pair*2]