class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        ans = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            ans += 1
            queue = [i]
            while queue:
                curr = queue.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for adj in graph[curr]:
                    if adj not in visited:
                        queue.append(adj)
        return ans