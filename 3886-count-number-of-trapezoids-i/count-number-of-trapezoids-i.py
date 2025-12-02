class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        count = defaultdict(int)
        hz = []
        for p in points:
            count[p[1]] += 1
        for _,v in count.items():
            if v >=2:
                hz.append(v*(v-1)//2)
        ans = 0
        MOD = 10**9+7
        # print(hz)
        if len(hz) <= 1:
            return 0
        s = sum(hz)
        for i in range(len(hz)-1):
            s -= hz[i]
            ans += hz[i]*s
            ans %= MOD
        return ans