class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Bước 1: Nhân đôi chuỗi để giả lập việc quay vòng (Type 1)
        # Ví dụ: "11100" -> "1110011100"
        s = s + s
        
        # Mục tiêu: So sánh cửa sổ độ dài n với 2 chuỗi xen kẽ "0101..." và "1010..."
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "0" if i % 2 == 0 else "1"
            target2 += "1" if i % 2 == 0 else "0"
            
        ans = float('inf')
        diff1 = 0 # Số lần flip để s giống target1
        diff2 = 0 # Số lần flip để s giống target2
        
        # Bước 2: Dùng Sliding Window cỡ n trượt trên chuỗi s+s
        for i in range(len(s)):
            # Thêm phần tử mới vào bên phải cửa sổ
            if s[i] != target1[i]: diff1 += 1
            if s[i] != target2[i]: diff2 += 1
            
            # Nếu cửa sổ vượt quá độ dài n, loại bỏ phần tử cũ nhất bên trái
            if i >= n:
                if s[i - n] != target1[i - n]: diff1 -= 1
                if s[i - n] != target2[i - n]: diff2 -= 1
            
            # Khi cửa sổ đã đủ độ dài n, cập nhật kết quả tối ưu
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
                
        return ans