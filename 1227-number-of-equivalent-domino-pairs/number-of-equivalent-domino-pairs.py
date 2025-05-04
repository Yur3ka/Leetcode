class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        ans = 0
        for a,b in dominoes:
            if a > b:
                count[(a,b)] += 1
            else:
                count[(b,a)] += 1
        for _,v in count.items():
            ans += v*(v-1)//2
        return ans