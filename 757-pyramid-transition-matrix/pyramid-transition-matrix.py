class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # 1. Tạo map để tra cứu nhanh các cặp (A, B) -> [C, D...]
        allowed_map = defaultdict(list)
        for a, b, c in allowed:
            allowed_map[(a, b)].append(c)
        
        # 2. Memoization để tránh tính lại các trường hợp đã thất bại
        memo = {}

        def backtrack(current_row, next_row):
            # Base Case 1: Nếu tầng hiện tại chỉ còn 1 khối -> Đã lên đến đỉnh tháp -> Thành công
            if len(current_row) == 1:
                return True
            
            # Base Case 2: Nếu đã xây xong tầng tiếp theo (next_row)
            # (Độ dài next_row luôn bằng current_row - 1)
            if len(next_row) == len(current_row) - 1:
                # Chuyển next_row thành string để làm current_row cho đợt đệ quy tiếp theo
                return backtrack("".join(next_row), [])
            
            # Kiểm tra trong memo
            state = (current_row, tuple(next_row))
            if state in memo:
                return memo[state]

            # 3. Logic tìm khối tiếp theo
            index = len(next_row)
            # Lấy cặp khối đế bên dưới: (A, B)
            base_pair = (current_row[index], current_row[index+1])
            
            # Nếu cặp này có trong danh sách cho phép
            if base_pair in allowed_map:
                for top in allowed_map[base_pair]:
                    next_row.append(top) # Chọn thử khối 'top'
                    
                    # Đệ quy để tìm khối tiếp theo trong cùng hàng
                    if backtrack(current_row, next_row):
                        return True
                    
                    next_row.pop() # Backtrack (trả lại trạng thái cũ)
            
            # Nếu thử hết mà không được, lưu vào memo là thất bại
            memo[state] = False
            return False

        return backtrack(bottom, [])