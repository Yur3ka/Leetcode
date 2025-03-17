class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for number in nums:
            count[number] += 1
        for _,v in count.items():
            if v%2 == 1:
                return False
        return True