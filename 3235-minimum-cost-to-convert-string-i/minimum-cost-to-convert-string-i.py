class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(changed)):
            adj[original[i]].append([changed[i],cost[i]])
        minCost = defaultdict(int)
        ans = 0

        def bfs(s,t):
            stack = [(0,s)]
            c = 0
            visited = set()
            while stack:
                curr, node = heapq.heappop(stack)
                if node in visited:
                    continue
                visited.add(node)
                if node == t:
                    return curr
                for des, value in adj[node]:
                    heapq.heappush(stack,(curr+value, des))
            return -1

        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            else:
                if minCost[(source[i],target[i])]:
                    ans += minCost[(source[i],target[i])]
                else:
                    c = bfs(source[i],target[i])
                    if c == -1:
                        return -1
                    minCost[(source[i],target[i])] = c
                    ans += c
        return ans