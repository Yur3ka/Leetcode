class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        from collections import defaultdict, Counter
        
        adj = defaultdict(list)
        for u, v in allowedSwaps:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        ans = 0

        def diff(s, t):
            c1 = Counter(s)
            c2 = Counter(t)
            res = 0
            for k, v in c1.items():
                if k not in c2:
                    res += v
                else:
                    res += max(0, v - c2[k])
            return res

        for i in range(len(source)):
            if i in visited:
                continue

            stack = [i]
            temp = []

            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue

                visited.add(curr)
                temp.append(curr)

                for nei in adj[curr]:
                    if nei not in visited:
                        stack.append(nei)

            # 🔥 Tính diff SAU KHI xong component
            s = [source[j] for j in temp]
            t = [target[j] for j in temp]
            ans += diff(s, t)

        return ans