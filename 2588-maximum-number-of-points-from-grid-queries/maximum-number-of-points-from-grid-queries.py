class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        def min_travel(matrix):
            m, n = len(matrix), len(matrix[0])
            heap = []
            result = []

            # Min heap chứa các giá trị của ô và tọa độ
            heapq.heappush(heap, (matrix[0][0] + 1, 0, 0))  # (k, x, y), k = mat[0][0] + 1, điểm bắt đầu (0,0)
            visited = set()
            heaped = set()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Các hướng di chuyển: lên, xuống, trái, phải
            v = 0
            while heap:
                k, x, y = heapq.heappop(heap)
                stack = [(x, y)]  # Khởi tạo stack với tọa độ hiện tại
                # Đếm số ô có thể đi được với giá trị k
                while stack:
                    cx, cy = stack.pop()
                    if (cx, cy) in visited:
                        continue
                    visited.add((cx, cy))
                    v += 1
                    
                    for dx, dy in directions:
                        nx, ny = cx + dx, cy + dy

                        # Kiểm tra giới hạn ma trận và xem ô đó đã được thăm chưa
                        if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                            if matrix[nx][ny] >= k and (nx,ny) not in heaped:  # Kiểm tra nếu giá trị ô đó lớn hơn hoặc bằng giá trị hiện tại
                                heapq.heappush(heap, (matrix[nx][ny]+1, nx, ny))  # Giữ giá trị k cố định và thêm vào min heap
                                heaped.add((nx, ny))  # Đánh dấu ô đã được thêm vào heap
                            elif matrix[nx][ny] < k:
                                stack.append((nx, ny))  # Thêm ô vào stack để kiểm tra tiếp
                                # v += 1  # Tăng v nếu ô có thể di chuyển đến

                # Thêm số v vào kết quả
                if not heap or heap[0][0] != k:
                    result.append((k, v))
                # result.append((k,v))

            return (result)
        res = []
        travel = min_travel(grid)
        for num in queries:
            if num < travel[0][0]:
                res.append(0)
            else:
                index = bisect.bisect_left(travel,num,key= lambda x: x[0])
                if index == len(travel):
                    res.append(travel[-1][1])
                else:
                    if num == travel[index][0]:
                        res.append(travel[index][1])
                    else:
                        res.append(travel[index-1][1])
        return res