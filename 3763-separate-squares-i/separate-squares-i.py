class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        low = float('inf')
        high = -float('inf')
        
        for x, y, l in squares:
            total_area += l * l
            low = min(low, y)
            high = max(high, y + l)
        
        # Chạy cố định 100 lần để đạt độ chính xác tối đa
        for _ in range(100):
            mid = (low + high) / 2
            below_area = 0
            
            for x, y, l in squares:
                if y >= mid:
                    # Hình vuông nằm hoàn toàn trên đường mid
                    continue
                elif y + l <= mid:
                    # Hình vuông nằm hoàn toàn dưới đường mid
                    below_area += l * l
                else:
                    # Đường mid cắt ngang hình vuông
                    below_area += (mid - y) * l
            
            if below_area < total_area / 2:
                low = mid
            else:
                high = mid
                
        return low