class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        ans = float("inf")
        res = -1
        def path(node, edge):
            visited = set()
            curr = 0
            path1 = {}
            while True:
                path1[node] = curr
                visited.add(node)
                node = edge[node]
                
                if node == -1 or node in visited:
                    break
                curr += 1
            return path1
        path1 = path(node1,edges)
        path2 = path(node2,edges)
        for k,v in path1.items():
            if k in path2:
                if max(path1[k], path2[k]) < ans:
                    ans = max(path1[k] , path2[k])
                    res = k
                elif max(path1[k] , path2[k]) == ans:
                    res = min(res,k)
        print(path1)
        print(path2)
        # for k,v in path2.items():
        #     if k in path1:
        #         ans = min(ans, path1[k]+path2[k])
        if ans != float("inf"):
            return res
        else:
            return -1
