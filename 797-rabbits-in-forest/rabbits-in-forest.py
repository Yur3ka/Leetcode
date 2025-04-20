class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        for num in answers:
            count[num] += 1
        ans = 0
        for k,v in count.items():
            group = v //(k+1)
            if v % (k+1) != 0:
                group += 1
            ans += (k+1)*group
        return ans