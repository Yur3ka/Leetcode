class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_index = [(num, i) for i, num in enumerate(nums)]
        
        nums_index.sort(key=lambda x: x[0], reverse=True)
        
        largest_k = nums_index[:k]
        
        largest_k.sort(key=lambda x: x[1])
        
        result = [num for num, index in largest_k]
        
        return result
