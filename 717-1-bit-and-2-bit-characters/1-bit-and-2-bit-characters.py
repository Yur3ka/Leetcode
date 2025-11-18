class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Các dạng bắt buộc phải là bit lẻ 0 ở cuối:
        # *00
        if len(bits) == 1: return True
        i = 0
        while i < len(bits)-1:
            if bits[i] == 0:
                i +=1
            else:
                i += 2
        return i == (len(bits)-1)