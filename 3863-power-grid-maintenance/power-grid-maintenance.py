class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        grid = []
        visited = set()
        pos = [-1]*(c+1)
        k = 0
        for i in range(1,c+1):
            if i in visited:
                continue
            stack = [i]
            g = set()
            while stack:
                curr = stack.pop()
                if curr in visited: 
                    continue
                g.add(curr)
                visited.add(curr)
                for v in adj[curr]:
                    if v not in visited:
                        stack.append(v)
            g = list(g)
            heapq.heapify(g)
            grid.append(g)
            for station in g:
                pos[station] = k
            k += 1
        ans = []
        offline = set()
        for t,s in queries:
            if t == 2:
                offline.add(s)
            else:
                if s not in offline:
                    ans.append(s)
                else:
                    while grid[pos[s]] and grid[pos[s]][0] in offline:
                        heapq.heappop(grid[pos[s]])
                    if not grid[pos[s]]:
                        ans.append(-1)
                    else:
                        ans.append(grid[pos[s]][0])
        return ans 