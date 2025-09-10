class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        dp = [0]*(n+1)
        lang = [set()]
        for i in range(len(languages)):
            lang.append(set(languages[i]))
        differ = []
        for u,v in friendships:
            common = lang[u] & lang[v]
            if len(common) == 0:
                differ.append([u,v])
        for i in range(1,n+1):
            teach = set()
            for u,v in differ:
                if i not in lang[u]:
                    # print(i,k,0,lang[k])
                    dp[i] += 1
                    lang[u].add(i)
                    teach.add(u)
                if i not in lang[v]:
                    # print(i,k,0,lang[k])
                    dp[i] += 1
                    lang[v].add(i)
                    teach.add(v)
            for f in teach:
                lang[f].remove(i)
        # print(dp)
        return min(dp[1:])