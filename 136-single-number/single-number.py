class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        return curr
    # Sử dụng xor để đúng yêu cầu đề ra
    # Học sau ở BitMask
    
    