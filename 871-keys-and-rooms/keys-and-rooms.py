class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        # keys = set()
        visited = set()
        queue = [0]
        # opened = True
        while queue:
            # opened = False
            curr = queue.pop(0)
            if curr in visited: 
                continue
            visited.add(curr)
            for key in rooms[curr]:
                if key not in visited:
                    queue.append(key)
        return len(visited) == n