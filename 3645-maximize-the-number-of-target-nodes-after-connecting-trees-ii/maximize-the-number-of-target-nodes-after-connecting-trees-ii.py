class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def bfs(graph):
            visited = set()
            even = set()
            odd = set()
            queue =[(0,0)]
            while queue:
                curr = queue.pop(0)
                if curr[0] in visited:
                    continue
                visited.add(curr[0])
                if curr[1] % 2 == 0:
                    even.add(curr[0])
                else:
                    odd.add(curr[0])
                for adj in graph[curr[0]]:
                    queue.append((adj,curr[1]+1))
            n_even = len(even)
            n_odd = len(odd)
            res = []
            for i in visited:
                if i in even:
                    res.append(n_even)
                else:
                    res.append(n_odd)
            return res, n_even, n_odd
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
        res, _, _ = bfs(graph1)
        _, n_even2, n_odd2 = bfs(graph2)
        for i in range(len(res)):
            res[i] += max(n_even2,n_odd2)
        return res
                