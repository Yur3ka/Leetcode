class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        deep = 0
        stack = [(1, 0, 0)]  # node, parent, depth

        while stack:
            node, parent, depth = stack.pop()
            deep = max(deep, depth)

            for nei in graph[node]:
                if nei != parent:
                    stack.append((nei, node, depth + 1))

        return pow(2, deep - 1, MOD)