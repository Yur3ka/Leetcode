class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        pairs = 0
        left_over = 0
        for k,v in c.items():
            pairs += v//2
            left_over += v%2
        return [pairs, left_over]