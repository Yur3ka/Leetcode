import heapq
from collections import defaultdict

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # 1. Chuẩn bị danh sách ô đã sắp xếp theo giá trị (val, r, c)
        cells = []
        for r in range(m):
            for c in range(n):
                cells.append((grid[r][c], r, c))
        cells.sort()
        
        # 2. Khoảng cách: dist[t][r][c]
        # Sử dụng mảng 3D thay vì dict để tăng tốc độ truy cập
        dist = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        
        # pq lưu: (cost, t, r, c)
        pq = [(0, 0, 0, 0)]
        dist[0][0][0] = 0
        
        # pointer_t[t] theo dõi xem trong danh sách 'cells', 
        # chúng ta đã kích hoạt đến đâu cho teleport mức t -> t+1
        pointer_t = [0] * k 
        
        while pq:
            d, t, r, c = heapq.heappop(pq)
            
            if d > dist[t][r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return d
            
            # --- Di chuyển thông thường (Phải, Xuống) ---
            for dr, dc in [(0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if d + grid[nr][nc] < dist[t][nr][nc]:
                        dist[t][nr][nc] = d + grid[nr][nc]
                        heapq.heappush(pq, (dist[t][nr][nc], t, nr, nc))
            
            # --- Di chuyển Teleport (t -> t+1) ---
            if t < k:
                current_val = grid[r][c]
                # Chỉ xử lý nếu cost hiện tại thực sự tối ưu để mở khóa teleport
                # Chúng ta duyệt tiếp từ vị trí pointer_t[t] cũ
                while pointer_t[t] < len(cells) and cells[pointer_t[t]][0] <= current_val:
                    val, nr, nc = cells[pointer_t[t]]
                    # Teleport không tốn thêm cost, cost giữ nguyên là d
                    if d < dist[t+1][nr][nc]:
                        dist[t+1][nr][nc] = d
                        heapq.heappush(pq, (d, t+1, nr, nc))
                    pointer_t[t] += 1
                    
        return -1