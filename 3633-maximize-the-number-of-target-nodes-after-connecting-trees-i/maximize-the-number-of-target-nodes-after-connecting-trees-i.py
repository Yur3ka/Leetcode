class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        path1 = defaultdict(list)
        path2 = defaultdict(list)
        for u,v in edges1:
            path1[u].append(v)
            path1[v].append(u)
        for u,v in edges2:
            path2[u].append(v)
            path2[v].append(u)
        n = len(edges1)+1
        m = len(edges2)+1
        k1 = [0]*n
        k2 = [0]*m
        def bfs(path,store,length,k):
            for i in range(length):
                visited = set()
                res = 0
                queue = [(i,0)]
                while queue:
                    temp = queue.pop(0)
                    if temp[1] > k:
                        break
                    if temp[0] not in visited:
                        visited.add(temp[0])
                        if temp[1] <= k:
                            res += 1
                            for adj in path[temp[0]]:
                                queue.append((adj,temp[1]+1))
                store[i] = res
        bfs(path1,k1,n,k)
        bfs(path2,k2,m,k-1)
        addition = max(k2)
        ans = []
        for i in range(n):
            ans.append(k1[i]+addition)
        return ans