class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Luôn ưu tiên node 0 làm gốc nếu có thể
            if root_i == 0 or root_j == 0:
                if root_i == 0: self.parent[root_j] = 0
                else: self.parent[root_i] = 0
            else:
                self.parent[root_i] = root_j
                
    def reset(self, i):
        self.parent[i] = i

    def connected(self, i, j):
        return self.find(i) == self.find(j)

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        uf = UnionFind(n)
        
        # Ban đầu người 0 và firstPerson biết bí mật
        uf.union(0, firstPerson)
        
        # Sắp xếp cuộc họp theo thời gian
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        m = len(meetings)
        while i < m:
            curr_time = meetings[i][2]
            pool = set()
            
            # Gom tất cả cuộc họp cùng thời điểm
            j = i
            while j < m and meetings[j][2] == curr_time:
                u, v, t = meetings[j]
                uf.union(u, v)
                pool.add(u)
                pool.add(v)
                j += 1
            
            # Sau khi union hết các cặp cùng giờ, 
            # ai không thông với node 0 thì phải reset
            for person in pool:
                if not uf.connected(person, 0):
                    uf.reset(person)
            
            i = j
            
        # Trả về danh sách những người kết nối với node 0
        return [i for i in range(n) if uf.connected(i, 0)]