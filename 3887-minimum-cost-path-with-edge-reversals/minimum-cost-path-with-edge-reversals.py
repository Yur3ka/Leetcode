class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w*2])
        dis = [[0,0]]
        visited = set()
        while dis:
            cost, node = heapq.heappop(dis)
            if node in visited:
                continue
            else:
                visited.add(node)
            if node == n-1:
                return cost
            for v,w in adj[node]:
                if v not in visited:
                    heapq.heappush(dis,[cost+w,v])
        return -1
