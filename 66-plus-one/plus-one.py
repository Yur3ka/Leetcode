class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        remain = 1
        for i in range(len(digits)-1,-1,-1):
            curr = digits[i] + remain
            ans.append(curr%10)
            remain = curr // 10
        if remain != 0:
            ans.append(1)
        return ans[::-1]