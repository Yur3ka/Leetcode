class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        m1 = min(basket1)
        m2 = min(basket2)
        total = defaultdict(int)
        for i in range(len(basket1)):
            c1[basket1[i]] += 1
            c2[basket2[i]] += 1
            total[basket1[i]] += 1
            total[basket2[i]] += 1
        for k,v in total.items():
            if v % 2 == 1:
                return -1
        ans = 0
        l1 = deque()
        l2 = deque()
        for k,v in c1.items():
            if v > total[k]//2:
                l1.extend([k]*(v-total[k]//2))
        for k,v in c2.items():
            if v > total[k]//2:
                l2.extend([k]*(v-total[k]//2))
        l2 = deque(sorted(l2))
        l1 = deque(sorted(l1))
        print(l1)
        print(l2)
        while l1:
            if l1[0] <= l2[0]:
                if l1[0] > m2*2:
                    ans += m2*2
                else:
                    ans += l1[0]
                m2 = min(m2,l1[0])
                l1.popleft()
                l2.pop()
            else:
                if l2[0] > m1*2:
                    ans += m1*2
                else:
                    ans += l2[0]
                m1 = min(m1,l2[0])
                # ans += l2[0]
                l1.pop()
                l2.popleft()
        return ans