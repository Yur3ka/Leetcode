class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        init = 0
        min_num = 0
        max_num = 0
        for number in differences:
            init = init + number
            min_num = min(min_num,init)
            max_num = max(max_num,init)
        diff = lower - min_num
        max_num = max_num + diff
        ans = upper - max_num +1
        return max(0,ans)